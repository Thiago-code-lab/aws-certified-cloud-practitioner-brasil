# Questões Domínio 2 - Segurança e Conformidade

## Questão 1
No modelo de responsabilidade compartilhada, quem configura permissões IAM da conta?

A) AWS
B) Cliente
C) Parceiro de faturamento
D) Auditor externo

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** B

**Explicação:**
O cliente é responsável por identidade e permissões na conta.

**Por que a alternativa A está errada:**
A AWS protege a infraestrutura, não define políticas do cliente.

</details>

---

## Questão 2
Qual prática segue o princípio de menor privilégio?

A) Dar acesso administrador para todo time
B) Dar somente permissões necessárias por função
C) Compartilhar usuário root
D) Remover MFA para facilitar login

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** B

**Explicação:**
Menor privilégio reduz superfície de risco.

**Por que a alternativa A está errada:**
Acesso total generalizado amplia risco operacional.

</details>

---

## Questão 3
Qual serviço é mais associado a auditoria de ações na conta AWS?

A) AWS CloudTrail
B) Amazon Route 53
C) AWS Budgets
D) Amazon EFS

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:**
CloudTrail registra chamadas de API e eventos de governança.

**Por que a alternativa B está errada:**
Route 53 é DNS, não trilha de auditoria.

</details>

---

## Questão 4
Para proteger segredos de aplicação (senhas/chaves), qual combinação é mais comum?

A) S3 público + ACL aberta
B) Secrets Manager + IAM
C) EC2 sem criptografia
D) Snapshot manual local

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** B

**Explicação:**
Secrets Manager centraliza e protege segredos com controle de acesso.

**Por que a alternativa A está errada:**
Exposição pública de dados sensíveis é prática insegura.

</details>

---

## Questão 5
Qual medida aumenta segurança da conta root?

A) Compartilhar senha com equipe
B) Ativar MFA
C) Desativar logs
D) Criar chaves de acesso permanentes para root

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** B

**Explicação:**
MFA adiciona segunda camada de autenticação.

**Por que a alternativa D está errada:**
Chaves permanentes de root aumentam risco severo.

</details>

---

## Questão 6
Qual serviço ajuda a detectar ameaças com análise contínua?

A) Amazon GuardDuty
B) AWS Snowball
C) Amazon SQS
D) AWS Artifact

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:**
GuardDuty identifica comportamentos suspeitos e possíveis ameaças.

**Por que a alternativa C está errada:**
SQS é fila de mensagens, não detecção de ameaça.

</details>

