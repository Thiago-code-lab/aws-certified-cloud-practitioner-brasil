# Domínio 3 - Cloud Technology and Services (60 questões)

1. Qual serviço executa código sem gerenciar servidores?  
A) Lambda B) EC2 C) EBS D) VPC
2. Qual serviço é banco NoSQL totalmente gerenciado?  
A) DynamoDB B) Aurora C) Redshift D) Neptune
3. Qual serviço é armazenamento de objetos?  
A) S3 B) EFS C) EBS D) FSx
4. Qual serviço distribui conteúdo global com baixa latência?  
A) CloudFront B) Route 53 C) SQS D) Kinesis
5. Qual serviço de fila desacopla componentes?  
A) SQS B) SNS C) SES D) EventBridge
6. Qual serviço pub/sub envia notificações para múltiplos assinantes?  
A) SNS B) SQS C) API Gateway D) Step Functions
7. Qual serviço relacional gerenciado da AWS?  
A) RDS B) DynamoDB C) ElastiCache D) Timestream
8. Qual serviço de cache em memória?  
A) ElastiCache B) Redshift C) Athena D) Glue
9. Qual serviço de data warehouse?  
A) Redshift B) Aurora C) RDS D) DocumentDB
10. Qual serviço faz migração de bancos com CDC?  
A) AWS DMS B) DataSync C) Snowball D) Glue
11. Qual serviço serverless para contêineres no ECS/EKS?  
A) Fargate B) Batch C) EC2 D) Lightsail
12. Qual serviço orquestra workflows serverless com estados?  
A) Step Functions B) EventBridge C) SNS D) SQS
13. Qual serviço roteia eventos entre sistemas?  
A) EventBridge B) Route 53 C) CloudTrail D) X-Ray
14. Qual serviço de API gerenciada?  
A) API Gateway B) App Mesh C) Route 53 D) WAF
15. Qual opção de orquestração de contêineres baseada em Kubernetes?  
A) EKS B) ECS C) Fargate D) App Runner
16. Qual opção de orquestração de contêineres nativa AWS?  
A) ECS B) EKS C) ECR D) Lambda
17. EBS é melhor descrito como:  
A) Bloco para EC2 em uma AZ B) Objeto global C) CDN D) Fila
18. EFS é melhor descrito como:  
A) File system NFS regional B) Banco relacional C) DNS D) Cache only
19. FSx é melhor para:  
A) Filesystems especializados gerenciados B) API pública C) Balanceamento L7 D) Filas
20. Storage Gateway é:  
A) Ponte híbrida entre on-premises e AWS storage B) Firewall web C) DNS D) IAM
21. Snow Family é usada para:  
A) Transferência física de grandes volumes B) Logs de API C) Criptografia D) Deploy CI/CD
22. AWS Backup serve para:  
A) Gestão centralizada de backups B) DNS failover C) Cache de sessão D) CDN
23. Route 53 é:  
A) DNS gerenciado B) Banco NoSQL C) Data warehouse D) SIEM
24. Direct Connect é:  
A) Conexão dedicada entre on-premises e AWS B) VPN pública C) NAT D) CDN
25. Site-to-Site VPN é:  
A) Túnel criptografado via internet B) Link físico dedicado C) CDN D) Firewall L7
26. VPC Endpoint permite:  
A) Acesso privado a serviços AWS sem internet B) Executar Lambda C) Criar RDS D) Fazer ETL
27. NAT Gateway é usado para:  
A) Saída internet de subnet privada B) Entrada direta em banco C) DNS privado D) Criptografia
28. Internet Gateway é usado para:  
A) Conectar VPC à internet B) Filtrar SQL injection C) Criar snapshots D) Rodar containers
29. ALB atua em qual camada?  
A) L7 B) L3 C) L2 D) Física
30. NLB é mais adequado para:  
A) Alto desempenho L4 B) Regras HTTP avançadas C) Cache objeto D) NoSQL
31. CloudWatch é usado para:  
A) Métricas, logs e alarmes B) Compra de instância reservada C) DNS D) Criação de bucket
32. CloudTrail é usado para:  
A) Auditoria de chamadas de API B) Escalar instâncias C) Gerar certificados D) Balancear tráfego
33. AWS Config é usado para:  
A) Avaliar conformidade de configurações B) Distribuir conteúdo C) Enviar e-mails D) Gerar dashboards BI
34. Systems Manager Session Manager ajuda em:  
A) Acesso remoto seguro a instâncias B) CDN C) DNS D) ETL
35. Compute Optimizer ajuda em:  
A) Rightsizing de recursos B) Geração de certificados C) Criação de APIs D) Migração física
36. Trusted Advisor entrega:  
A) Recomendações de boas práticas B) Tabelas NoSQL C) Orquestração de workflow D) Treinamento ML
37. Qual serviço para documentos compatível com MongoDB?  
A) DocumentDB B) Neptune C) DynamoDB D) RDS
38. Qual serviço para grafos?  
A) Neptune B) Redshift C) Aurora D) ElastiCache
39. Athena é usado para:  
A) Consultar dados no S3 com SQL B) Rodar contêiner C) Fazer DNS D) Criar IAM users
40. Glue é usado para:  
A) ETL gerenciado B) Web firewall C) VPN D) Storage em bloco
41. Kinesis é usado para:  
A) Streaming de dados em tempo real B) DNS autoritativo C) Backup central D) Banco relacional
42. EMR é usado para:  
A) Processamento big data (Hadoop/Spark) B) WAF C) IAM D) API Gateway
43. OpenSearch Service é usado para:  
A) Busca e analytics de logs/texto B) DNS C) Queue D) Snapshot EC2
44. App Runner é:  
A) Serviço para deploy simplificado de apps web em contêiner B) Banco de dados C) CDN D) Firewall
45. ECR é usado para:  
A) Repositório de imagens de contêiner B) Trilha de auditoria C) DNS D) Data warehouse
46. Parameter Store armazena:  
A) Configurações/segredos simples B) Imagens de contêiner C) Objetos S3 D) Eventos
47. Qual serviço para envio de e-mail transacional?  
A) SES B) SNS C) SQS D) Kinesis
48. Qual serviço para mensageria gerenciada compatível com brokers?  
A) Amazon MQ B) IAM C) EC2 D) EBS
49. Qual serviço para aplicações web/móvel com GraphQL gerenciado?  
A) AppSync B) API Gateway only C) Route53 D) Shield
50. Qual serviço ajuda rastreamento distribuído de requisições?  
A) X-Ray B) Config C) Budgets D) IAM
51. Qual serviço de CI/CD orquestra pipeline?  
A) CodePipeline B) CodeBuild C) CodeDeploy D) CodeCommit
52. Qual serviço de build gerenciado?  
A) CodeBuild B) CodeDeploy C) CodeArtifact D) CloudTrail
53. Qual serviço de deploy automatizado?  
A) CodeDeploy B) CodeBuild C) Budgets D) Route53
54. CloudFormation é:  
A) Infraestrutura como código declarativa B) Banco relacional C) Cache distribuído D) Serviço de e-mail
55. CDK é:  
A) Abstração de IaC em linguagens de programação B) DNS C) SIEM D) VPN
56. SAM é focado em:  
A) Aplicações serverless B) Banco NoSQL C) CDN D) DDoS
57. Amplify é focado em:  
A) Desenvolvimento/hospedagem web-mobile B) Auditoria API C) DNS D) Fila
58. Qual serviço ajuda gerenciamento de custos por uso?  
A) Cost Explorer B) Route53 C) EKS D) MQ
59. Qual combinação suporta arquitetura event-driven?  
A) EventBridge + Lambda + SQS/SNS B) RDS + EBS only C) Route53 + ACM only D) EC2 standalone only
60. Qual escolha é mais adequada para app sem gerenciar servidor, com triggers?  
A) AWS Lambda B) EC2 C) ECS on EC2 manual D) Bare metal
