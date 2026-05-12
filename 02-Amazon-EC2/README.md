# Amazon EC2

Módulo de computação virtual com foco em instâncias, modelos de compra e decisões básicas de disponibilidade.

## Foco do módulo
- Instâncias EC2, AMI, tipos de instância e pares de chave.
- EBS como volume de bloco para instâncias.
- Auto Scaling e Elastic Load Balancing em nível introdutório.

## Revisão rápida
- EC2 é computação como serviço: você escolhe capacidade, sistema e configuração.
- EBS é armazenamento de bloco persistente, diferente de S3.
- Auto Scaling ajusta quantidade de instâncias; Load Balancer distribui tráfego.

## Sinais clássicos de prova
- "Servidor virtual na nuvem" -> Amazon EC2.
- "Volume para anexar a uma instância" -> Amazon EBS.
- "Distribuir tráfego entre instâncias" -> Elastic Load Balancing.

## Erro comum
Confundir aumentar o tamanho de uma instância com alta disponibilidade. Escala vertical melhora capacidade; alta disponibilidade exige redundância.

## O que memorizar
| Comparação | Regra mental de prova |
|---|---|
| EC2 vs Lambda | EC2 = servidor gerenciado pelo cliente; Lambda = execução sem servidor |
| EBS vs S3 | EBS = bloco para instância; S3 = objetos via API |

## Ponte para o próximo módulo
Depois de entender computação, revise segurança: quem pode criar, acessar e auditar esses recursos.

## Continuidade
Trilha de arquitetura: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil
