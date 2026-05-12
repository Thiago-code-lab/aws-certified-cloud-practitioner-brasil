# Computação Serverless

Módulo para reconhecer serviços sem servidor e padrões simples orientados a eventos.

## Foco do módulo
- AWS Lambda para execução de código sob demanda.
- API Gateway como entrada para APIs.
- SQS e SNS como integração desacoplada.

## Revisão rápida
- Lambda executa código sem provisionar servidor.
- API Gateway expõe APIs e pode acionar Lambda.
- SQS enfileira mensagens; SNS publica notificações para assinantes.

## Sinais clássicos de prova
- "Executar código curto em resposta a evento" -> AWS Lambda.
- "Criar endpoint de API gerenciado" -> Amazon API Gateway.
- "Desacoplar componentes com fila" -> Amazon SQS.

## Erro comum
Escolher EC2 para tarefas event-driven simples quando o enunciado pede menor operação.

## O que memorizar
| Comparação | Regra mental de prova |
|---|---|
| Lambda vs EC2 | Lambda = evento sem servidor; EC2 = servidor configurável |
| SQS vs SNS | SQS = fila; SNS = publicação/notificação |

## Ponte para o próximo módulo
Depois de serverless, revise armazenamento geral: escolha correta entre objeto, bloco e arquivo.

## Continuidade
Trilha de arquitetura: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil
