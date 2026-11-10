# Lab 03 Cloudwatch Basico

Este laboratório pratica métricas, dashboards e alarmes no Amazon CloudWatch.

## Objetivo

Visualizar uma métrica de um recurso existente e criar um alarme de baixo risco para entender o fluxo de monitoramento.

## Passos

1. Abra o CloudWatch e localize métricas de um recurso de laboratório, como uma instância EC2.
2. Selecione uma métrica, ajuste o período e compare os valores no gráfico.
3. Crie um alarme com limite simples e poucas avaliações.
4. Configure uma notificação somente se houver um tópico SNS de teste confirmado.
5. Registre o que representa o estado `OK`, `ALARM` e `INSUFFICIENT_DATA`.

## Verificação

O alarme deve refletir a métrica escolhida. Não force carga cara apenas para mudar seu estado.

## Limpeza

Exclua o alarme, o dashboard opcional e os recursos usados no teste.

Arquitetura: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil
IA na AWS: https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil


---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
