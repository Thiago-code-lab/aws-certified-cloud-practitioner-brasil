# Security Groups E Nacl

Security Groups e Network ACLs filtram tráfego em camadas diferentes da VPC.

- **Security Group:** atua no recurso, é stateful e possui apenas regras de permissão.
- **NACL:** atua na subnet, é stateless e aceita permissão e negação.
- Security Groups são o controle principal para instâncias e interfaces.
- **Dica de prova:** bloqueio explícito por subnet aponta para NACL.

Aprofundamento em arquitetura AWS: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil



> Recurso complementar: se quiser conectar este fundamento com pipelines e analytics na AWS, veja o curso Engenharia de Dados na AWS: https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9

---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
