# Deck Segurança e IAM

## Card 01
**Pergunta:** Qual conta deve ser protegida com MFA e evitada no uso diário?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
A conta root. Ela tem privilégios amplos e deve ficar reservada para tarefas excepcionais que exigem root.

</details>

## Card 02
**Pergunta:** Em IAM, qual diferença de prova entre usuário e role?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Usuário representa uma identidade persistente. Role é assumida temporariamente por usuários, serviços ou contas, sem credenciais permanentes próprias.

</details>

## Card 03
**Pergunta:** “Least privilege” deve aparecer como qual decisão prática?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Permitir somente ações necessárias, nos recursos necessários, pelo tempo necessário. Permissão ampla por conveniência é sinal de resposta errada.

</details>

## Card 04
**Pergunta:** Um app em EC2 precisa ler objetos no S3. Qual abordagem é mais adequada que salvar chaves no servidor?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Anexar uma IAM Role à instância EC2 com permissões mínimas para o bucket necessário.

</details>

## Card 05
**Pergunta:** Qual serviço registra chamadas de API para responder “quem fez o quê, quando e de onde”?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
AWS CloudTrail. Ele é a associação clássica para auditoria de ações na conta AWS.

</details>

## Card 06
**Pergunta:** AWS Shield, WAF e Security Groups protegem exatamente a mesma coisa?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Não. Shield ajuda contra DDoS, WAF filtra tráfego web HTTP/HTTPS e Security Groups controlam tráfego de rede em recursos como EC2.

</details>

## Card 07
**Pergunta:** Qual serviço centraliza criação e controle de chaves de criptografia?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
AWS KMS. Memorize como o serviço gerenciado de chaves para criptografia integrada a serviços AWS.

</details>

## Card 08
**Pergunta:** Se a prova pedir documentos de conformidade e relatórios de auditoria da AWS, qual serviço aparece?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
AWS Artifact. Ele fornece acesso a relatórios e acordos relacionados a compliance da AWS.

</details>

## Card 09
**Pergunta:** O cliente pode delegar à AWS a classificação dos próprios dados?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Não. Classificação, governança, retenção e proteção dos dados do cliente continuam sendo responsabilidade do cliente.

</details>

## Card 10
**Pergunta:** Qual erro é mais perigoso: política explícita de Deny ou Allow amplo demais?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Allow amplo demais aumenta superfície de risco. Em IAM, um Deny explícito normalmente prevalece e bloqueia acesso.

</details>

## Card 11
**Pergunta:** GuardDuty deve ser lembrado como firewall, antivírus ou detecção de ameaças?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Detecção de ameaças. Ele analisa eventos e sinais para apontar comportamento suspeito na conta.

</details>

## Card 12
**Pergunta:** Erro comum de prova: “MFA substitui políticas IAM bem definidas”. Por que está errado?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
MFA fortalece autenticação, mas não define autorização. Acesso correto ainda depende de políticas, roles e menor privilégio.

</details>
