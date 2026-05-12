# Deck Fundamentos de Nuvem

## Card 01
**Pergunta:** Se a prova citar “aumentar e reduzir recursos conforme a demanda muda”, qual conceito ela quer testar?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Elasticidade. O sinal de memorização é ajuste dinâmico: recursos sobem em pico e descem quando a demanda cai.

</details>

## Card 02
**Pergunta:** Escalabilidade é a mesma coisa que elasticidade?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Não. Escalabilidade é a capacidade de crescer sem perder desempenho; elasticidade é ajustar capacidade automaticamente ao volume real de uso.

</details>

## Card 03
**Pergunta:** Em uma questão sobre baixa latência para usuários brasileiros, a primeira decisão costuma envolver o quê?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Escolha de Região. A Região define proximidade geográfica, residência de dados e impacto direto na latência.

</details>

## Card 04
**Pergunta:** O que uma Zona de Disponibilidade representa na infraestrutura global da AWS?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Um ou mais data centers isolados dentro de uma Região. AZs diferentes reduzem impacto de falhas locais.

</details>

## Card 05
**Pergunta:** Quando a resposta mais provável é Multi-AZ, qual pista o enunciado normalmente dá?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Continuidade durante falha de um data center ou componente local. Multi-AZ é pista forte para alta disponibilidade dentro da mesma Região.

</details>

## Card 06
**Pergunta:** Qual benefício da nuvem troca investimento inicial em hardware por pagamento operacional?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Trocar CAPEX por OPEX. Em vez de comprar capacidade antes, a empresa paga recursos conforme usa.

</details>

## Card 07
**Pergunta:** “Provisionar ambiente em minutos” aponta para qual vantagem central da nuvem?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Agilidade. A nuvem reduz tempo de espera por infraestrutura e acelera experimentos, testes e lançamentos.

</details>

## Card 08
**Pergunta:** No modelo de responsabilidade compartilhada, o que fica “da nuvem” e o que fica “na nuvem”?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
A AWS protege a infraestrutura da nuvem. O cliente protege o que coloca na nuvem: dados, identidades, permissões e configurações.

</details>

## Card 09
**Pergunta:** Alta disponibilidade e tolerância a falhas são sinônimos perfeitos?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Não. Alta disponibilidade busca manter o serviço acessível; tolerância a falhas enfatiza continuar operando mesmo quando componentes falham.

</details>

## Card 10
**Pergunta:** Qual é a ideia por trás de “economias de escala” em nuvem?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
A AWS opera em escala massiva e repassa eficiência de custos aos clientes por meio de preços e serviços compartilhados.

</details>

## Card 11
**Pergunta:** Se a empresa quer parar de adivinhar capacidade futura, qual princípio de nuvem resolve melhor?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Capacidade sob demanda. O foco é reduzir superprovisionamento e subprovisionamento, ajustando recursos quando necessário.

</details>

## Card 12
**Pergunta:** Erro de prova: escolher Multi-Region sempre que aparecer “alta disponibilidade”. Qual é o ajuste correto?

<details>
<summary><strong>Ver resposta</strong></summary>

**Resposta:**
Para CLF-C02, Multi-AZ costuma ser a resposta suficiente para alta disponibilidade regional. Multi-Region entra quando há desastre regional, latência global ou requisitos geográficos.

</details>
