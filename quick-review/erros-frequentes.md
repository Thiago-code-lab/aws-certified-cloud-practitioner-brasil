# Erros Frequentes

Lista curta para revisão corretiva. A ideia é reduzir erros recorrentes, não cobrir toda a certificação.

## Fundamentos
1. Confundir alta disponibilidade com alta performance.
2. Tratar Região e AZ como sinônimos.
3. Esquecer que responsabilidade compartilhada muda conforme o serviço, mas dados e permissões continuam críticos para o cliente.

## Segurança
4. Achar que a AWS configura IAM para o cliente.
5. Usar root como conta operacional.
6. Trocar CloudTrail por CloudWatch em perguntas de auditoria.

## S3 e armazenamento
7. Ignorar custo e tempo de recuperação em classes de arquivamento.
8. Tratar S3 como disco de instância.
9. Confundir versionamento com lifecycle.

## Custos
10. Escolher menor preço por hora sem olhar custo total.
11. Esquecer de configurar alertas com Budgets.
12. Usar Cost Explorer para estimativa prévia quando a pista aponta para Pricing Calculator.

## Correção prática
A cada bloco de questões, registre 3 erros recorrentes e revise apenas esses pontos por 15 minutos no mesmo dia.
