# Precificação e Suporte

Módulo para decisão de custo: modelos de cobrança, visibilidade financeira e suporte.

## Foco do módulo
- On-Demand, Reserved/Savings e Spot.
- Budgets e Cost Explorer.
- Planos de suporte em nível introdutório.

## Revisão rápida
- On-Demand para carga variável.
- Spot para cargas tolerantes a interrupção.
- Budgets alerta desvio; Cost Explorer analisa tendência histórica.

## Sinais clássicos de prova
- "Alerta de gasto mensal" -> AWS Budgets.
- "Analisar custo passado e prever" -> Cost Explorer.
- "Reduzir custo de workload estável" -> Reserved/Savings.

## Erro comum
Comparar apenas preço por hora e ignorar custo total de operação: armazenamento, transferência, recuperação e suporte.

## O que memorizar
| Comparação | Regra mental de prova |
|---|---|
| On-Demand vs Spot | On-Demand sem compromisso; Spot com desconto e risco de interrupção |
| Budgets vs Cost Explorer | Budgets alerta limite; Cost Explorer analisa uso/custo no tempo |

## Ponte de consolidação
Ciclo recomendado de revisão: fundamentos -> segurança -> S3 -> custos.

## Continuidade
Trilha de arquitetura: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil
