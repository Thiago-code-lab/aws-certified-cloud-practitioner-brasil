# AWS Storage Gateway

## O que é
Serviço híbrido que conecta datacenter on-premises a armazenamento AWS com protocolos padrão.

## Quando usar
- Migração gradual para cloud sem interromper sistemas locais.
- Backup e arquivamento com integração ao S3 e outros serviços.

## Pontos de prova
- Suporta cenários de arquivo, volume e fita virtual.
- Reduz latência local com cache on-premises.

## CLI útil
```bash
aws storagegateway list-gateways
aws storagegateway list-local-disks --gateway-arn <arn>
```
---

Creditos autorais:
- Thiago Cardoso - https://www.linkedin.com/in/analyticsthiagocardoso
- Pedro Albertini - https://www.linkedin.com/in/pedroalbertini/
- Lucas Garcia - https://www.linkedin.com/in/lucas-del-puerto/