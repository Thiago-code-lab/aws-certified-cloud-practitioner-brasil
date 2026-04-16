# AWS Backup

## O que é
AWS Backup centraliza políticas e execução de backups para múltiplos serviços AWS.

## Quando usar
- Padronizar retenção e conformidade entre contas e serviços.
- Automatizar planos de backup e restore.

## Pontos de prova
- Serviço orientado por policy.
- Ajuda em governança de proteção de dados.

## CLI útil
```bash
aws backup list-backup-plans
aws backup list-recovery-points-by-backup-vault --backup-vault-name Default
```
---

Creditos autorais:
- Thiago Cardoso - https://www.linkedin.com/in/analyticsthiagocardoso
- Pedro Albertini - https://www.linkedin.com/in/pedroalbertini/
- Lucas Garcia - https://www.linkedin.com/in/lucas-del-puerto/