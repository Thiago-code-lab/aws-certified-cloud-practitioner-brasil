# AWS Database Migration Service (AWS DMS)

## O que é
AWS DMS migra dados entre bancos com baixa interrupção, suportando cenários homogêneos e heterogêneos.

## Quando usar
- Migração para a AWS com downtime mínimo.
- Replicação contínua para transição gradual.

## Pontos de prova
- DMS move dados; conversão de esquema é normalmente feita com AWS SCT.
- Full load e CDC podem ser combinados.

## CLI útil
```bash
aws dms describe-replication-instances
aws dms describe-replication-tasks
```

## Links
- https://docs.aws.amazon.com/dms/
---

Creditos autorais:
- Thiago Cardoso - https://www.linkedin.com/in/analyticsthiagocardoso
- Pedro Albertini - https://www.linkedin.com/in/pedroalbertini/
- Lucas Garcia - https://www.linkedin.com/in/lucas-del-puerto/