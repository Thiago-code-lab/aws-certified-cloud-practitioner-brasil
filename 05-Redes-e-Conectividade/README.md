# Redes e Conectividade

Módulo para reconhecer os serviços de rede mais cobrados no nível Cloud Practitioner.

## Foco do módulo
- VPC, sub-redes, Security Groups e NACLs.
- Route 53, CloudFront e conectividade híbrida em alto nível.
- Conceitos de rede pública, privada e borda.

## Revisão rápida
- VPC isola logicamente recursos de rede na AWS.
- Security Group atua no nível do recurso; NACL atua no nível da sub-rede.
- CloudFront aproxima conteúdo do usuário por edge locations.

## Sinais clássicos de prova
- "DNS gerenciado" -> Amazon Route 53.
- "Entregar conteúdo com baixa latência global" -> Amazon CloudFront.
- "Conexão dedicada entre datacenter e AWS" -> AWS Direct Connect.

## Erro comum
Tratar Security Group e NACL como iguais. Security Group é stateful; NACL é stateless.

## O que memorizar
| Comparação | Regra mental de prova |
|---|---|
| Security Group vs NACL | SG protege recurso; NACL protege sub-rede |
| Route 53 vs CloudFront | Route 53 resolve DNS; CloudFront entrega conteúdo |

## Ponte para o próximo módulo
Com rede entendida, avance para banco de dados: onde a aplicação guarda dados estruturados e como isso afeta operação.

## Continuidade
Trilha de arquitetura: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil
