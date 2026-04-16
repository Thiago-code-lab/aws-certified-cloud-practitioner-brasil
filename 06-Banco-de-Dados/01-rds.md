# Amazon RDS

## O que é
Amazon RDS é um serviço gerenciado para bancos relacionais como MySQL, PostgreSQL, MariaDB, Oracle e SQL Server.

## Quando usar
- Aplicações transacionais com SQL e integridade referencial.
- Times que querem reduzir esforço operacional de patch, backup e alta disponibilidade.

## Pontos de prova
- Multi-AZ aumenta disponibilidade, não desempenho de leitura.
- Read Replicas melhoram leitura e podem ser promovidas para escrita em desastre.

## CLI útil
```bash
aws rds describe-db-instances
aws rds describe-orderable-db-instance-options --engine postgres
```

## Links
- https://docs.aws.amazon.com/rds/
---

Creditos autorais:
- Thiago Cardoso - https://www.linkedin.com/in/analyticsthiagocardoso
- Pedro Albertini - https://www.linkedin.com/in/pedroalbertini/
- Lucas Garcia - https://www.linkedin.com/in/lucas-del-puerto/