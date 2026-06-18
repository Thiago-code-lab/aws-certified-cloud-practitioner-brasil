# Armazenamento

Módulo para comparar tipos de armazenamento sem aprofundar além do nível CLF-C02.

## Foco do módulo
- S3 para objetos.
- EBS para bloco.
- EFS para arquivo compartilhado.

## Revisão rápida
- Objeto é acessado por API e combina dados + metadados.
- Bloco é usado como volume por instâncias.
- Arquivo compartilhado atende múltiplos clientes com sistema de arquivos.

## Sinais clássicos de prova
- "Armazenar objetos, imagens, backups ou logs" -> Amazon S3.
- "Disco persistente para EC2" -> Amazon EBS.
- "Sistema de arquivos compartilhado entre instâncias Linux" -> Amazon EFS.

## Erro comum
Usar S3 como resposta para qualquer armazenamento. A prova diferencia objeto, bloco e arquivo.

## O que memorizar
| Comparação | Regra mental de prova |
|---|---|
| S3 vs EBS | S3 = objetos; EBS = bloco para EC2 |
| EBS vs EFS | EBS = volume individual; EFS = arquivo compartilhado |

## Ponte para o próximo módulo
Com storage entendido, avance para monitoramento e governança: como observar, auditar e controlar o ambiente.

## Continuidade
Trilha de arquitetura: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil

---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
