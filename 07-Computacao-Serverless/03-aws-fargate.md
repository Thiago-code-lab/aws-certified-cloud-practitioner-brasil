# AWS Fargate

## O que é
Fargate é a opção de execução serverless para containers em ECS e EKS.

## Quando usar
- Containers sem gerenciar EC2 para cluster.
- Workloads de microsserviços com variação de carga.

## Pontos de prova
- Você paga por vCPU e memória alocadas.
- Ideal para reduzir overhead operacional de infraestrutura.

## CLI útil
```bash
aws ecs list-clusters
aws ecs list-services --cluster MeuCluster
```

## Links
- https://docs.aws.amazon.com/fargate/
---

Creditos autorais:
- Thiago Cardoso - https://www.linkedin.com/in/analyticsthiagocardoso
- Pedro Albertini - https://www.linkedin.com/in/pedroalbertini/
- Lucas Garcia - https://www.linkedin.com/in/lucas-del-puerto/