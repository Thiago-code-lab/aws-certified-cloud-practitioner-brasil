# User Data E Metadata

User data e instance metadata ajudam a automatizar e identificar instâncias EC2, mas têm finalidades diferentes.

- **User data:** script fornecido no lançamento, usado para instalar e iniciar a aplicação.
- **Metadata:** dados consultados pela instância, como ID, rede e credenciais temporárias da função IAM.
- Prefira funções IAM a chaves permanentes armazenadas no user data.
- **Dica de prova:** inicialização automática aponta para user data; dados da própria instância apontam para metadata.

Aprofundamento em arquitetura AWS: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil


---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
