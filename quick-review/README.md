# Revisão Rápida - CLF-C02

Use este bloco para sessões de 20 a 30 minutos, com foco por domínio. Ele não substitui os flashcards: aqui a ideia é diagnosticar lacunas rapidamente antes de voltar ao módulo certo.

## Revisão por domínio
| Domínio | Revisão curta | Quando usar |
|---|---|---|
| Fundamentos de nuvem | [fundamentos.md](./fundamentos.md) | Quando errar Região, AZ, elasticidade ou responsabilidade compartilhada |
| IAM e segurança | [seguranca.md](./seguranca.md) | Quando errar identidade, permissões, auditoria ou compliance |
| S3 e armazenamento | [armazenamento.md](./armazenamento.md) | Quando errar S3, EBS, EFS, classes ou lifecycle |
| Custos e precificação | [custos.md](./custos.md) | Quando errar Budgets, Cost Explorer, Spot, suporte ou modelos de preço |

## Fluxo sugerido
1. Execute o [checklist de véspera](./checklist-vespera.md).
2. Revise o domínio com maior erro usando os arquivos acima.
3. Consulte [serviços-chave](./servicos-chave.md) para comparação rápida.
4. Releia [erros frequentes](./erros-frequentes.md) antes de resolver novas questões.

## Mini treino diagnóstico

### Questão 1
Uma aplicação precisa continuar disponível se um data center isolado da Região falhar. Qual desenho atende melhor ao nível CLF-C02?

A) Multi-AZ  
B) Usuário root com MFA  
C) S3 Glacier Deep Archive  
D) AWS Budgets

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Explicação:**
Multi-AZ distribui recursos entre Zonas de Disponibilidade e é a associação mais direta para alta disponibilidade regional.

</details>

### Questão 2
Uma equipe quer permitir que uma aplicação em EC2 acesse um bucket S3 sem armazenar access keys no servidor. Qual opção é mais adequada?

A) IAM Role para a instância  
B) AWS Artifact  
C) Plano de suporte Developer  
D) S3 Lifecycle

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Explicação:**
IAM Role fornece credenciais temporárias e permissões controladas para a aplicação, reduzindo risco operacional.

</details>

### Questão 3
Arquivos de log devem ser mantidos por anos, quase nunca acessados, e podem levar horas para recuperação. Qual escolha é mais coerente?

A) S3 Glacier Deep Archive  
B) S3 Standard  
C) EBS gp3  
D) EC2 On-Demand

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Explicação:**
Glacier Deep Archive é voltado a retenção longa, acesso raríssimo e custo baixo, aceitando recuperação mais demorada.

</details>

### Questão 4
Antes de lançar uma arquitetura, a empresa quer estimar mensalmente quanto ela deve custar. Qual ferramenta usar?

A) AWS Pricing Calculator  
B) AWS CloudTrail  
C) Amazon GuardDuty  
D) S3 Transfer Acceleration

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta correta:** A

**Explicação:**
Pricing Calculator estima custo planejado antes do uso. Para analisar gasto já ocorrido, a associação seria Cost Explorer.

</details>
