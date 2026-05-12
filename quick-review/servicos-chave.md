# Serviços-Chave

Mapa compacto para revisar associações de prova sem transformar a revisão em catálogo completo.

## Fundamentos
- Região: localização geográfica, latência e residência de dados.
- AZ: isolamento local para alta disponibilidade.
- Responsabilidade compartilhada: AWS protege a infraestrutura; cliente protege dados, acessos e configurações.
- Sinal de prova: se o enunciado falar de isolamento físico local, normalmente aponta para AZ.

## IAM e segurança
- IAM: identidade, autenticação e autorização.
- CloudTrail: trilha de auditoria de chamadas de API.
- KMS: chaves de criptografia.
- Artifact: documentos e relatórios de compliance.
- Sinal de prova: se aparecer "quem fez o quê na conta", a associação mais comum é CloudTrail.

## S3 e armazenamento
- S3: armazenamento de objetos.
- EBS: volume de bloco para EC2.
- EFS: sistema de arquivos compartilhado.
- Lifecycle: redução de custo ao longo do tempo.
- Sinal de prova: se falar em dados raramente acessados por anos, pense em Glacier.

## Custos e precificação
- Budgets: alerta de limite.
- Cost Explorer: análise histórica e tendência.
- Pricing Calculator: estimativa antes do uso.
- Spot: custo baixo com interrupção.
- Sinal de prova: se o workload tolera interrupção, Spot costuma ser a melhor pista.

## Comparações rápidas
| Comparação | Uso em prova |
|---|---|
| Região vs AZ | Região = geografia; AZ = isolamento para disponibilidade |
| IAM User vs Role | User = identidade persistente; Role = acesso temporário |
| CloudWatch vs CloudTrail | CloudWatch observa operação; CloudTrail audita API |
| S3 vs EBS | S3 = objetos; EBS = bloco para instância |
| S3 Standard vs Glacier | Standard = acesso frequente; Glacier = arquivamento |
| On-Demand vs Spot | On-Demand = flexibilidade; Spot = economia com interrupção |
| Budgets vs Cost Explorer | Budgets = alerta; Cost Explorer = análise |

## Dica final
Quando duas alternativas parecerem corretas, prefira a que resolve o cenário com menor complexidade operacional e melhor alinhamento ao enunciado.
