# AWS X-Ray

## O que é
Serviço de tracing distribuído para analisar latência e dependências entre componentes de aplicação.

## Quando usar
- Diagnóstico de performance em microsserviços.
- Investigação de gargalos e falhas em chamadas distribuídas.

## Pontos de prova
- Complementa métricas e logs com rastreamento de requisições.
- Útil para observabilidade fim a fim.

## CLI útil
```bash
aws xray get-service-graph --start-time 2026-01-01T00:00:00Z --end-time 2026-01-01T01:00:00Z
```
---

Creditos autorais:
- Thiago Cardoso - https://www.linkedin.com/in/analyticsthiagocardoso
- Pedro Albertini - https://www.linkedin.com/in/pedroalbertini/
- Lucas Garcia - https://www.linkedin.com/in/lucas-del-puerto/