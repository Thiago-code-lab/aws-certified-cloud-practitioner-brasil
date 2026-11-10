# Revisão por Domínio - IAM e Segurança

Use este bloco quando os erros envolverem acesso, auditoria, criptografia ou responsabilidade do cliente.

## Revisão rápida
- Root deve ser protegido com MFA e evitado no uso diário.
- IAM User é identidade persistente; IAM Role é assumida temporariamente.
- CloudTrail registra chamadas de API para auditoria.
- KMS centraliza chaves de criptografia gerenciadas.

## Sinais clássicos de prova
- Se aparecer "quem fez o quê na conta", pense em CloudTrail.
- Se aparecer "acesso temporário entre serviços", pense em IAM Role.
- Se aparecer "relatórios de compliance da AWS", pense em AWS Artifact.

## O que memorizar
| Comparação | Regra mental |
|---|---|
| IAM User vs Role | User = longo prazo; Role = acesso assumido |
| MFA vs política IAM | MFA autentica; política autoriza |
| CloudTrail vs CloudWatch | Auditoria de API vs métricas/logs operacionais |

## Próxima revisão
Depois deste bloco, avance para [armazenamento](./armazenamento.md): permissões e dados aparecem juntos em muitas questões.

---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
