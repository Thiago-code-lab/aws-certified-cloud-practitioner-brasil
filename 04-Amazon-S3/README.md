# Amazon S3

Módulo de armazenamento de objetos com foco em durabilidade, classes e custo.

## Foco do módulo
- Objetos, buckets e políticas de acesso.
- Versionamento e lifecycle.
- Classes de armazenamento e cenários típicos.

## Revisão rápida
- S3 é objeto, não bloco para boot de EC2.
- Versionamento reduz risco de exclusão acidental.
- Lifecycle move dados para classe mais barata conforme padrão de acesso.

## Sinais clássicos de prova
- "Site estático simples" -> S3 static website hosting.
- "Dados raramente acessados por anos" -> Glacier/Deep Archive.
- "Controle de acesso em escala" -> IAM policy + bucket policy.

## Erro comum
Escolher classe apenas pelo menor preço por GB e ignorar custo/tempo de recuperação.

## O que memorizar
| Comparação | Regra mental de prova |
|---|---|
| S3 Standard vs S3 Glacier | Standard para acesso frequente; Glacier para arquivo e acesso raro |
| Versionamento vs Lifecycle | Versionamento protege histórico; Lifecycle otimiza custo ao longo do tempo |

## Ponte para o próximo módulo
Depois de S3, avance para custos: como precificar uso, prever gasto e evitar surpresas.

## Continuidade
Trilha de arquitetura: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil
