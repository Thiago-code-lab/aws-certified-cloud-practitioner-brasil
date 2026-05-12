# Deck Amazon S3

## Card 01
**Pergunta:** No S3, o que é armazenado dentro de um bucket?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Objetos. Cada objeto combina dados, metadados e uma chave única dentro do bucket.

</details>

## Card 02
**Pergunta:** Qual número mental ajuda a lembrar a durabilidade do S3?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Onze noves de durabilidade: 99,999999999%. A prova usa isso para reforçar preservação de objetos, não ausência total de indisponibilidade.

</details>

## Card 03
**Pergunta:** Versionamento protege melhor contra qual acidente operacional?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Sobrescrita ou exclusão acidental de objetos. Ele permite recuperar versões anteriores quando habilitado no bucket.

</details>

## Card 04
**Pergunta:** Quando lifecycle é a resposta mais provável?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Quando o enunciado pede movimentar objetos automaticamente para classes mais baratas ou expirar dados antigos.

</details>

## Card 05
**Pergunta:** Dados acessados com frequência e sem padrão claro devem começar em qual classe?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
S3 Standard. É a escolha padrão para acesso frequente, baixa latência e alta disponibilidade.

</details>

## Card 06
**Pergunta:** Para dados raramente acessados, mas que precisam voltar rápido, qual família de classes faz sentido?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
S3 Standard-IA ou S3 One Zone-IA. A escolha depende do requisito de disponibilidade e do risco aceito.

</details>

## Card 07
**Pergunta:** Se a recuperação pode levar minutos ou horas e o objetivo é arquivamento barato, qual pista aparece?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Glacier. Para retenção muito longa e acesso raríssimo, a prova pode apontar para Glacier Deep Archive.

</details>

## Card 08
**Pergunta:** Site estático no S3 exige só enviar arquivos HTML?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Não. É preciso habilitar static website hosting, configurar documento de índice/erro e ajustar leitura pública ou distribuição via CloudFront.

</details>

## Card 09
**Pergunta:** Qual controle moderno deve ser preferido a ACLs individuais para acesso em buckets?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Políticas IAM e bucket policies. ACLs são menos indicadas para governança ampla em ambientes atuais.

</details>

## Card 10
**Pergunta:** S3 serve como disco de boot de uma instância EC2?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Não. S3 é armazenamento de objetos via API. Para volume de bloco de EC2, memorize Amazon EBS.

</details>

## Card 11
**Pergunta:** Qual recurso ajuda usuários distantes a enviar objetos para S3 com menor impacto de latência?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
S3 Transfer Acceleration, usando a rede de borda da AWS para acelerar transferências em cenários específicos.

</details>

## Card 12
**Pergunta:** S3 Intelligent-Tiering resolve qual dúvida comum de armazenamento?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Quando o padrão de acesso é desconhecido ou muda com o tempo. Ele move objetos entre camadas de acesso para otimizar custo automaticamente.

</details>
