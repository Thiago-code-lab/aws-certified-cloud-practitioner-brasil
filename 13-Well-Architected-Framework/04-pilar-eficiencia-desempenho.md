# ?? Pilar: Efici�ncia de Desempenho

## ?? O que �?
Busca o melhor uso de recursos para atender requisitos de desempenho com elasticidade e baixa lat�ncia.

## ?? Analogia Simples
� escolher ve�culo e rota ideais para cada entrega, ajustando em tempo real conforme tr�nsito.

## ??? Como funciona
Princ�pios: sele��o correta de recursos, revis�o cont�nua, monitoramento e trade-offs arquiteturais.

```text
Medi��o de desempenho -> Ajuste de arquitetura -> Melhor lat�ncia/custo
```

## ?? Casos de Uso Comuns
- Uso de CloudFront para entrega global
- Caching com ElastiCache
- Escolha de inst�ncias adequadas por workload

## ?? Modelo de Pre�o
Boas decis�es de performance evitam overprovisioning e reduzem custo.

## ?? Comandos CLI �teis
```bash
aws cloudfront list-distributions
aws ec2 describe-instance-types --instance-types t3.micro c7g.large
```

## ?? Links Oficiais
- https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/
- https://aws.amazon.com/products/compute/
---

Creditos autorais:
- Thiago Cardoso - https://www.linkedin.com/in/analyticsthiagocardoso
- Pedro Albertini - https://www.linkedin.com/in/pedroalbertini/
- Lucas Garcia - https://www.linkedin.com/in/lucas-del-puerto/