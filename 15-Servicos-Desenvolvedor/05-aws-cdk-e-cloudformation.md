# AWS CDK e AWS CloudFormation

## O que são
CloudFormation define infraestrutura como código por templates declarativos. CDK permite modelar infraestrutura em linguagens de programação e sintetizar templates.

## Quando usar
- Provisionamento padronizado e reproduzível.
- Governança de infraestrutura por versionamento.

## Pontos de prova
- Ambos seguem IaC; CDK é camada de abstração sobre CloudFormation.
- Mudanças controladas por stack e revisão.

## CLI útil
```bash
aws cloudformation list-stacks
aws cloudformation describe-stacks --stack-name MinhaStack
```
---

Creditos autorais:
- Thiago Cardoso - https://www.linkedin.com/in/analyticsthiagocardoso
- Pedro Albertini - https://www.linkedin.com/in/pedroalbertini/
- Lucas Garcia - https://www.linkedin.com/in/lucas-del-puerto/