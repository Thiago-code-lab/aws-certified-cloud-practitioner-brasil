# Amazon EBS

## O que é
EBS é armazenamento em bloco para instâncias EC2, com baixa latência e opção de snapshots.

## Quando usar
- Disco de sistema e bancos em EC2.
- Workloads que exigem persistência de dados em bloco.

## Pontos de prova
- EBS é associado a uma AZ.
- Snapshot do EBS é salvo no S3 de forma gerenciada.

## CLI útil
```bash
aws ec2 describe-volumes
aws ec2 describe-snapshots --owner-ids self
```
---

Creditos autorais:
- Thiago Cardoso - https://www.linkedin.com/in/analyticsthiagocardoso
- Pedro Albertini - https://www.linkedin.com/in/pedroalbertini/
- Lucas Garcia - https://www.linkedin.com/in/lucas-del-puerto/