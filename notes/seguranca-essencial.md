# Segurança Essencial - Revisão de Prova

## Revisão rápida
- IAM controla identidades, permissões e roles.
- MFA reduz risco de credencial comprometida, mas não substitui menor privilégio.
- CloudTrail registra chamadas de API para auditoria.

## Sinal clássico de prova
Se aparecer "rastrear chamadas de API", a associação normal é CloudTrail.

## Erro comum
Assumir que a AWS define permissões da conta para o cliente.

## O que memorizar
| Comparação | Regra mental |
|---|---|
| IAM User vs Role | User é persistente; Role é temporária/assumida |
| MFA vs política IAM | MFA autentica melhor; política autoriza ou nega |

## Pergunta de validação
Uma aplicação precisa acessar outro serviço AWS sem guardar chaves permanentes. Qual recurso de IAM deve vir à mente?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
IAM Role com permissões mínimas para a tarefa.

</details>
