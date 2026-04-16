# Amazon Aurora

## O que é
Aurora é um banco relacional compatível com MySQL e PostgreSQL, com arquitetura distribuída em armazenamento e alta performance.

## Quando usar
- Workloads que precisam de alta disponibilidade com failover rápido.
- Sistemas que exigem desempenho superior ao RDS tradicional.

## Pontos de prova
- Aurora replicas compartilham armazenamento e costumam ter menor atraso de replicação.
- Aurora Serverless v2 ajuda em carga variável.

## CLI útil
```bash
aws rds describe-db-clusters
aws rds describe-db-instances --filters Name=engine,Values=aurora-postgresql
```

## Links
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/
---

Creditos autorais:
- Thiago Cardoso - https://www.linkedin.com/in/analyticsthiagocardoso
- Pedro Albertini - https://www.linkedin.com/in/pedroalbertini/
- Lucas Garcia - https://www.linkedin.com/in/lucas-del-puerto/