# Segurança e Conformidade

Módulo focado no que mais cai em prova: identidade, acesso, auditoria e responsabilidade.

## Foco do módulo
- IAM: usuários, grupos, roles e políticas.
- MFA e menor privilégio.
- Auditoria com CloudTrail e base de compliance.

## Revisão rápida
- Root deve ser restrito e protegido com MFA.
- IAM controla autenticação e autorização.
- CloudTrail responde "quem fez o quê" via eventos de API.

## Sinais clássicos de prova
- "Rastrear chamadas de API" -> CloudTrail.
- "Conceder acesso temporário entre serviços" -> IAM Role.
- "Aplicar acesso mínimo necessário" -> princípio de menor privilégio.

## Erro comum
Achar que habilitar IAM sozinho resolve conformidade. Prova cobra conjunto de controles, incluindo log e governança.

## O que memorizar
| Comparação | Regra mental de prova |
|---|---|
| IAM User vs IAM Role | User = identidade de longo prazo; Role = permissão assumida, inclusive temporária |
| Root vs IAM Admin | Root para tarefas excepcionais; IAM Admin para operação diária |

## Ponte para o próximo módulo
Com acesso e controles definidos, o passo natural é revisar armazenamento, especialmente S3.

## Continuidade
Trilha de arquitetura: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil
