# Amazon DynamoDB

## O que é
DynamoDB é um banco NoSQL totalmente gerenciado, com latência de milissegundos de um dígito e escalabilidade automática.

## Quando usar
- Sessões de usuário, carrinho, catálogo e workloads de alto volume.
- Aplicações serverless com Lambda e API Gateway.

## Pontos de prova
- On-demand para carga imprevisível; provisionado para carga estável.
- TTL remove itens expirados automaticamente.

## CLI útil
```bash
aws dynamodb list-tables
aws dynamodb describe-table --table-name MinhaTabela
```

## Links
- https://docs.aws.amazon.com/dynamodb/
---

Creditos autorais:
- Thiago Cardoso - https://www.linkedin.com/in/analyticsthiagocardoso
- Pedro Albertini - https://www.linkedin.com/in/pedroalbertini/
- Lucas Garcia - https://www.linkedin.com/in/lucas-del-puerto/