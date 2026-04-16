# AWS Health Dashboard

## O que é
Painel que mostra eventos de saúde da AWS e impactos potenciais nos recursos da sua conta.

## Quando usar
- Acompanhar incidentes regionais e manutenções programadas.
- Priorizar resposta operacional em eventos de serviço.

## Pontos de prova
- Visão personalizada da conta, diferente da visão pública de status.
- Apoia comunicação de incidentes.

## CLI útil
```bash
aws health describe-events --filter services=EC2
```
---

Creditos autorais:
- Thiago Cardoso - https://www.linkedin.com/in/analyticsthiagocardoso
- Pedro Albertini - https://www.linkedin.com/in/pedroalbertini/
- Lucas Garcia - https://www.linkedin.com/in/lucas-del-puerto/