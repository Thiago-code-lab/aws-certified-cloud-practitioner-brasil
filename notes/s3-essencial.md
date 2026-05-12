# S3 Essencial - Revisão de Prova

## Revisão rápida
- S3 é armazenamento de objetos, não volume de bloco.
- Versionamento ajuda contra exclusão ou sobrescrita acidental.
- Lifecycle otimiza custo com transição e expiração automática.

## Sinal clássico de prova
Se o enunciado falar em arquivamento de longo prazo com acesso raro, a pista costuma ser Glacier.

## Erro comum
Usar S3 como se fosse disco de sistema operacional de EC2.

## O que memorizar
| Comparação | Regra mental |
|---|---|
| S3 Standard vs Glacier | Standard para uso frequente; Glacier para arquivo |
| Versionamento vs Lifecycle | Recuperar versões vs automatizar ciclo de vida |

## Pergunta de validação
Um bucket recebe relatórios mensais e deve mover arquivos antigos para armazenamento mais barato sem ação manual. Qual recurso usar?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
S3 Lifecycle.

</details>
