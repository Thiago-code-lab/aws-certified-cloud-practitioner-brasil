# Lab 01 Iam Inicial

Este laboratório pratica identidades, grupos, políticas, MFA e menor privilégio no AWS IAM.

## Objetivo

Criar um usuário de estudo com acesso ao console por meio de um grupo, sem utilizar a conta-raiz nas tarefas diárias.

## Passos

1. Entre com a conta-raiz apenas para ativar MFA e revisar os contatos da conta.
2. No IAM, crie um grupo administrativo para o laboratório e associe a política apropriada ao ambiente de estudo.
3. Crie um usuário, adicione-o ao grupo e habilite acesso ao console.
4. Entre com o novo usuário e confirme que o acesso esperado funciona.
5. Revise o relatório de credenciais e remova credenciais que não serão usadas.

## Verificação

- A conta-raiz possui MFA.
- O usuário recebe permissões pelo grupo, não por várias políticas diretas.
- Não existem access keys sem necessidade.

## Limpeza

Remova o usuário e o grupo se a conta não continuar sendo usada para estudos.

Arquitetura: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil
IA na AWS: https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil


---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
