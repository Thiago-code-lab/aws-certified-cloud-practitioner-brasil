# Simulado Completo - Revisão Final CLF-C02

Este simulado curto foi desenhado para treino final com foco em tomada de decisão básica.

## Questão 1
Uma empresa precisa escalar rapidamente durante picos e reduzir recursos após o pico. Qual benefício da nuvem melhor descreve isso?

A) Imutabilidade
B) Elasticidade
C) Isolamento físico dedicado
D) Latência fixa

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** B

**Explicação:**
Elasticidade é ajuste de capacidade conforme demanda.

**Por que a alternativa C está errada:**
Dedicado físico não é o benefício principal desse cenário.

</details>

---

## Questão 2
Qual serviço é mais apropriado para trilha de auditoria de ações na conta?

A) CloudTrail
B) S3
C) EBS
D) Athena

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:**
CloudTrail registra eventos e chamadas de API.

**Por que a alternativa B está errada:**
S3 armazena objetos, não é trilha de auditoria por si só.

</details>

---

## Questão 3
Qual opção representa melhor banco relacional gerenciado na AWS?

A) DynamoDB
B) RDS
C) ElastiCache
D) S3

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** B

**Explicação:**
RDS é serviço relacional gerenciado.

**Por que a alternativa A está errada:**
DynamoDB é NoSQL.

</details>

---

## Questão 4
Qual serviço auxilia no acompanhamento e previsão de custos?

A) Cost Explorer
B) KMS
C) Route 53
D) ECS

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:**
Cost Explorer é voltado a análise de custos e uso.

**Por que a alternativa C está errada:**
Route 53 é serviço de DNS.

</details>

---

## Questão 5
No modelo de responsabilidade compartilhada, quem define política de senha dos usuários IAM?

A) AWS
B) Cliente
C) AWS Support
D) Parceiro de treinamento

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** B

**Explicação:**
Configuração de identidade e acesso do cliente é responsabilidade do cliente.

**Por que a alternativa A está errada:**
AWS não define política interna de conta do cliente.

</details>

---

## Questão 6
Qual serviço é usado para hospedar objetos e conteúdo estático?

A) S3
B) Aurora
C) EC2 Auto Scaling
D) IAM

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:**
S3 é armazenamento de objetos e base comum para conteúdo estático.

**Por que a alternativa D está errada:**
IAM trata identidade, não hospedagem de arquivos.

</details>

---

## Questão 7
Qual estratégia costuma aumentar disponibilidade de aplicação web?

A) Uma instância em uma única AZ
B) Múltiplas AZs
C) Sem backup
D) Sem monitoramento

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** B

**Explicação:**
Múltiplas AZs reduzem impacto de falhas locais.

**Por que a alternativa A está errada:**
Um único ponto de falha diminui disponibilidade.

</details>

---

## Questão 8
Para executar função sem gerenciar servidor, a escolha mais direta é:

A) Lambda
B) EC2
C) Redshift
D) Direct Connect

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:**
Lambda é serviço serverless para execução de código.

**Por que a alternativa B está errada:**
EC2 exige gestão de instâncias.

</details>

---

## Questão 9
Qual prática de segurança é recomendada para conta root?

A) Compartilhar credencial com equipe
B) Desativar MFA
C) Ativar MFA e reduzir uso
D) Criar chaves de acesso para automação

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** C

**Explicação:**
Root deve ter MFA e uso restrito.

**Por que a alternativa D está errada:**
Chaves permanentes de root são alto risco.

</details>

---

## Questão 10
Qual ferramenta envia alerta quando o custo ultrapassa limite definido?

A) AWS Budgets
B) AWS Artifact
C) AWS Config
D) CloudFront

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:**
Budgets gera alertas de custo, uso e forecast.

**Por que a alternativa C está errada:**
Config avalia conformidade de recursos, não orçamento financeiro.

</details>

