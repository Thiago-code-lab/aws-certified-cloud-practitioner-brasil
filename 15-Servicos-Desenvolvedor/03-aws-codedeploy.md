# AWS CodeDeploy

## O que é
Serviço para automação de deploy em EC2, Lambda e ECS.

## Quando usar
- Releases com estratégia controlada e rollback automatizado.
- Padronização de implantação entre ambientes.

## Pontos de prova
- Suporta deploy gradual e validações.
- Ajuda a reduzir risco de indisponibilidade em release.

## CLI útil
```bash
aws deploy list-applications
aws deploy list-deployment-groups --application-name MinhaApp
```
---

Creditos autorais:
- Thiago Cardoso - https://www.linkedin.com/in/analyticsthiagocardoso
- Pedro Albertini - https://www.linkedin.com/in/pedroalbertini/
- Lucas Garcia - https://www.linkedin.com/in/lucas-del-puerto/