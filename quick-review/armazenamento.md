# Revisão por Domínio - S3 e Armazenamento

Use este bloco quando os erros envolverem S3, classes de armazenamento, backup ou tipo de volume.

## Revisão rápida
- S3 armazena objetos em buckets.
- EBS é bloco persistente para EC2.
- EFS é sistema de arquivos compartilhado.
- Lifecycle move ou expira objetos automaticamente para controlar custo.

## Sinais clássicos de prova
- Se aparecer "objeto, backup, log ou site estático", pense em S3.
- Se aparecer "disco para instância EC2", pense em EBS.
- Se aparecer "arquivo compartilhado por múltiplas instâncias", pense em EFS.
- Se aparecer "retenção longa e acesso raro", pense em Glacier.

## O que memorizar
| Comparação | Regra mental |
|---|---|
| S3 Standard vs Glacier | Acesso frequente vs arquivamento |
| S3 vs EBS | Objeto via API vs bloco para EC2 |
| Versionamento vs Lifecycle | Recuperar histórico vs otimizar ciclo de vida |

## Próxima revisão
Depois deste bloco, avance para [custos](./custos.md): storage quase sempre envolve custo, retenção e recuperação.
