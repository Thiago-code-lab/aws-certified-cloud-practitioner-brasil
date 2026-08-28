# Lab 02 Site Estatico S3

Este laboratório mostra como o S3 armazena objetos e pode entregar um site composto apenas por HTML, CSS e imagens.

## Objetivo

Criar um bucket, enviar uma página simples e entender a diferença entre acesso privado, endpoint de website e distribuição segura por CloudFront.

## Passos

1. Crie um bucket em uma Região próxima e mantenha o bloqueio de acesso público ativado.
2. Envie um arquivo `index.html` sem dados sensíveis.
3. Observe que um objeto privado não pode ser aberto anonimamente.
4. Para um teste didático, revise a configuração de website estático e as permissões exigidas.
5. Em uma arquitetura real, prefira CloudFront com acesso privado ao bucket para HTTPS e cache.

## Verificação

Confirme que a página correta é retornada pelo endpoint escolhido e que nenhum objeto além do necessário está exposto.

## Limpeza

Exclua os objetos, a distribuição de teste se criada e, por fim, o bucket.

Arquitetura: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil
IA na AWS: https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil


---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
