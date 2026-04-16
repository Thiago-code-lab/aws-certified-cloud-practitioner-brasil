# AWS Step Functions

## O que é
Serviço de orquestração de fluxos com máquina de estados para coordenar múltiplos serviços.

## Quando usar
- Processos com várias etapas, retries e validações.
- Workflows serverless com Lambda, ECS, SNS, SQS e outros.

## Pontos de prova
- Visualização de fluxo e tratamento de erro são diferenciais.
- Evita lógica de orquestração complexa no código da aplicação.

## CLI útil
```bash
aws stepfunctions list-state-machines
aws stepfunctions list-executions --state-machine-arn <arn>
```

## Links
- https://docs.aws.amazon.com/step-functions/
---

Creditos autorais:
- Thiago Cardoso - https://www.linkedin.com/in/analyticsthiagocardoso
- Pedro Albertini - https://www.linkedin.com/in/pedroalbertini/
- Lucas Garcia - https://www.linkedin.com/in/lucas-del-puerto/