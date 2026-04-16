# ?? Pilar: Confiabilidade

## ?? O que �?
Trata da capacidade do sistema continuar operando e se recuperar de falhas rapidamente.

## ?? Analogia Simples
� um hospital com gerador, redund�ncia e plano de conting�ncia testado.

## ??? Como funciona
Princ�pios: recupera��o autom�tica, testes de falha, escala horizontal e automa��o de mudan�as.

```text
Falha detectada -> Failover/Auto Recovery -> Servi�o continua dispon�vel
```

## ?? Casos de Uso Comuns
- Multi-AZ para banco de dados
- Auto Scaling para picos de demanda
- Failover DNS com health checks

## ?? Modelo de Pre�o
Redund�ncia aumenta custo, mas reduz impacto financeiro de indisponibilidade.

## ?? Comandos CLI �teis
```bash
aws autoscaling describe-auto-scaling-groups
aws route53 list-health-checks
```

## ?? Links Oficiais
- https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/
- https://docs.aws.amazon.com/route53/
---

Creditos autorais:
- Thiago Cardoso - https://www.linkedin.com/in/analyticsthiagocardoso
- Pedro Albertini - https://www.linkedin.com/in/pedroalbertini/
- Lucas Garcia - https://www.linkedin.com/in/lucas-del-puerto/