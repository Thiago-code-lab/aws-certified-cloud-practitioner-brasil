# Banco de Dados

Módulo para diferenciar os principais serviços de dados no nível introdutório do CLF-C02.

## Foco do módulo
- Amazon RDS para bancos relacionais gerenciados.
- DynamoDB para NoSQL chave-valor/documento.
- Redshift para análise e data warehouse.

## Revisão rápida
- RDS reduz trabalho operacional de bancos relacionais.
- DynamoDB aparece quando a pista é NoSQL, baixa latência e escala gerenciada.
- Redshift é associado a analytics e data warehouse.

## Sinais clássicos de prova
- "Banco relacional gerenciado" -> Amazon RDS.
- "NoSQL serverless com baixa latência" -> Amazon DynamoDB.
- "Análise em grande volume de dados estruturados" -> Amazon Redshift.

## Erro comum
Escolher RDS apenas por conhecer SQL quando o enunciado pede escala NoSQL ou acesso chave-valor.

## O que memorizar
| Comparação | Regra mental de prova |
|---|---|
| RDS vs DynamoDB | RDS = relacional; DynamoDB = NoSQL gerenciado |
| RDS vs Redshift | RDS = transacional; Redshift = análise |

## Ponte para o próximo módulo
Depois de dados, avance para serverless: como executar código e integrar eventos com menos operação.

## Continuidade
Trilha de arquitetura: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil
