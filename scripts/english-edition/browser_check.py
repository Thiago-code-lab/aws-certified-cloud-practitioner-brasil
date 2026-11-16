"""Render the real landing page and every original Markdown equivalent in Chromium."""
from __future__ import annotations
import json
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit
from playwright.sync_api import sync_playwright
from validate import AUDIT, MARKDOWN, ROOT, read_json

STYLE = 'body{max-width:960px;margin:32px auto;padding:0 20px;font:16px/1.6 system-ui;color:#172033}img{max-width:100%;height:auto}table{border-collapse:collapse;display:block;overflow:auto}th,td{border:1px solid #cbd5e1;padding:8px}pre{overflow:auto;background:#f1f5f9;padding:16px}details{padding:12px;border:1px solid #cbd5e1;margin:12px 0}a{color:#075dba}'

class StudyHandler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        relative = unquote(urlsplit(self.path).path).lstrip('/')
        path = (ROOT/relative).resolve()
        if path.is_relative_to(ROOT) and path.suffix == '.md' and path.is_file():
            body = MARKDOWN.render(path.read_text(encoding='utf-8-sig'))
            html = f'<!doctype html><html lang="en-US"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{path.stem}</title><style>{STYLE}</style></head><body>{body}</body></html>'
            payload = html.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type','text/html; charset=utf-8')
            self.send_header('Content-Length',str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return
        if relative == 'favicon.ico':
            self.send_response(204)
            self.end_headers()
            return
        super().do_GET()

    def log_message(self, format: str, *args: object) -> None:
        return

def run() -> dict[str,object]:
    server = ThreadingHTTPServer(('127.0.0.1',0),partial(StudyHandler,directory=str(ROOT)))
    thread = threading.Thread(target=server.serve_forever,daemon=True)
    thread.start()
    base = f'http://127.0.0.1:{server.server_port}'
    screenshots = AUDIT/'screenshots'
    screenshots.mkdir(exist_ok=True)
    errors: list[str] = []
    local_failures: list[str] = []
    external_failures: list[str] = []
    layouts = []
    rendered = []
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            context = browser.new_context()
            page = context.new_page()
            page.on('pageerror',lambda error: errors.append(str(error)))
            page.on('console',lambda msg: errors.append(msg.text) if msg.type == 'error' else None)
            def response_status(response: object) -> None:
                if response.status >= 400:
                    (local_failures if response.url.startswith(base) else external_failures).append(f'{response.status}: {response.url}')
            page.on('response',response_status)
            page.on('requestfailed',lambda request: (local_failures if request.url.startswith(base) else external_failures).append(f'{request.failure}: {request.url}'))
            for name,width,height in [('desktop',1440,1000),('tablet',768,1024),('mobile',390,844)]:
                page.set_viewport_size({'width':width,'height':height})
                page.goto(base+'/index.html',wait_until='networkidle')
                page.locator('footer').scroll_into_view_if_needed()
                page.wait_for_timeout(850)
                overflow = page.evaluate('document.documentElement.scrollWidth > window.innerWidth')
                module_count = page.locator('a.mod-link').count()
                for href in ['#modules','#caf','#waf','#practice']:
                    assert page.locator(href).count() == 1, href
                if name == 'desktop':
                    page.locator('.nav-links a[href="#modules"]').click()
                    assert page.evaluate('location.hash') == '#modules'
                page.evaluate('window.scrollTo(0,0)')
                page.wait_for_timeout(500)
                page.screenshot(path=str(screenshots/f'portal-{name}.png'),full_page=True)
                layouts.append({'name':name,'width':width,'height':height,'horizontal_overflow':overflow,'module_links':module_count,'status':'passed' if not overflow and module_count==18 else 'failed'})
            # Follow an actual module card using the preview handler's Markdown rendering.
            page.locator('a.mod-link').first.click()
            assert '01-Introduction-to-Cloud-Computing/README.md' in page.url
            assert page.locator('h1').count() >= 1
            for row in read_json(AUDIT/'source-inventory.json')['files']:
                if row['file_type'] != '.md':
                    continue
                response = page.goto(base+'/'+row['target_path'],wait_until='domcontentloaded')
                headings = page.locator('h1,h2,h3,h4,h5,h6').count()
                assert response and response.status==200 and headings>0, row['target_path']
                for details in page.locator('details').all():
                    assert details.locator('summary').count()==1, row['target_path']
                    details.locator('summary').click()
                    assert details.get_attribute('open') is not None
                rendered.append({'path':row['target_path'],'headings':headings,'details':page.locator('details').count(),'status':'passed'})
            samples = [('README.md','readme'),('16-Practice-Exams-and-Questions/10-question-practice-exam.md','practice-exam'),('17-Glossary/README.md','glossary')]
            page.set_viewport_size({'width':1280,'height':900})
            for path,name in samples:
                page.goto(base+'/'+path,wait_until='networkidle')
                page.locator('details').evaluate_all('(nodes)=>nodes.forEach(node=>node.open=true)')
                page.screenshot(path=str(screenshots/f'{name}.png'),full_page=True)
            for diagram in ['basic-architecture.svg','security-flow.svg']:
                page.goto(base+'/diagrams/'+diagram,wait_until='load')
                page.screenshot(path=str(screenshots/diagram.replace('.svg','.png')))
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
    return {'status':'passed' if not errors and not local_failures and all(x['status']=='passed' for x in layouts) else 'failed','browser':'Chromium via Playwright','method':'Real local HTTP server; Markdown rendered by markdown-it-py for preview; external resources were not mocked.','layouts':layouts,'markdown_documents_rendered':len(rendered),'markdown_results':rendered,'browser_errors':errors,'local_asset_failures':local_failures,'external_resource_failures':external_failures,'screenshots_directory':'docs/english-edition/screenshots','limitations':['The preview renderer is not GitHub\'s production renderer.','No AWS lab resources were provisioned.']}

if __name__=='__main__':
    result=run()
    (AUDIT/'browser-test-results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='markdown_results'},indent=2))
    raise SystemExit(0 if result['status']=='passed' else 1)
