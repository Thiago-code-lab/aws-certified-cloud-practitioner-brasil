# Monitoramento e Governança

Módulo para revisar observabilidade, auditoria e controle organizacional em nível inicial.

## Foco do módulo
- CloudWatch para métricas, logs e alarmes.
- CloudTrail para auditoria de API.
- AWS Organizations e Tags para governança básica.

## Revisão rápida
- CloudWatch observa desempenho e comportamento operacional.
- CloudTrail registra ações na conta para auditoria.
- Tags ajudam a organizar custo, dono e ambiente.

## Sinais clássicos de prova
- "Criar alarme de métrica" -> Amazon CloudWatch.
- "Quem chamou uma API" -> AWS CloudTrail.
- "Gerenciar várias contas" -> AWS Organizations.

## Erro comum
Confundir CloudWatch com CloudTrail. CloudWatch monitora operação; CloudTrail audita ações.

## O que memorizar
| Comparação | Regra mental de prova |
|---|---|
| CloudWatch vs CloudTrail | Métricas/logs operacionais vs trilha de auditoria |
| Tags vs Organizations | Tags organizam recursos; Organizations organiza contas |

## Ponte para o próximo módulo
Depois de governança, revise custos: monitoramento só vira controle quando gasto e alertas entram no ciclo.

## Continuidade
Trilha de arquitetura: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil
