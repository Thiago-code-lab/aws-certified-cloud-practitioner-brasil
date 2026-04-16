# Domínio 5 - Combined Practice and Integrated Scenarios (60 questões)

1. Em um cenário com pico imprevisível de acesso web, qual combinação é mais escalável?  
A) ALB + Auto Scaling + Multi-AZ B) EC2 única C) Banco on-prem apenas D) Sem monitoramento

2. Para reduzir custo de ambiente de testes noturno, qual ação é melhor?  
A) Agendar desligamento B) Duplicar instâncias C) Aumentar tamanho D) Remover alarmes

3. Para auditoria de ações na conta AWS, qual serviço é essencial?  
A) CloudTrail B) CloudFront C) Route 53 D) SQS

4. Para proteger credenciais de acesso à AWS, qual prática é correta?  
A) MFA + IAM Identity Center B) Chave root compartilhada C) Senha simples D) Sem rotação

5. Aplicação precisa armazenar arquivos estáticos globalmente com baixa latência. Melhor opção?  
A) S3 + CloudFront B) EBS C) DynamoDB D) SQS

6. Banco relacional com alta disponibilidade gerenciada em AWS deve usar:  
A) RDS Multi-AZ B) EC2 manual C) DynamoDB D) S3

7. Workload tolera interrupção e busca menor custo de compute. Opção indicada:  
A) Spot Instances B) Reserved sem análise C) Dedicated Host D) On-demand máximo

8. Para desacoplar microsserviços assíncronos, escolha adequada:  
A) SQS B) Route 53 C) WAF D) ACM

9. Requisito: notificar vários sistemas simultaneamente ao ocorrer evento. Use:  
A) SNS B) SQS C) EBS D) EFS

10. Arquitetura serverless orientada a eventos combina melhor:  
A) EventBridge + Lambda B) EC2 fixa C) RDS only D) NAT only

11. Para governança de múltiplas contas, recurso central:  
A) AWS Organizations B) IAM User root C) CloudShell D) App Runner

12. Controle financeiro por área de negócio exige:  
A) Tags e orçamento por centro de custo B) Uma conta sem padrão C) Sem relatórios D) Sem alertas

13. Requisito de DNS altamente disponível na AWS:  
A) Route 53 B) CloudTrail C) Inspector D) Athena

14. Acesso privado de VPC ao S3 sem internet pública:  
A) VPC Endpoint B) Internet Gateway C) NAT Gateway D) Transit sem rota

15. Para mitigar ataques DDoS básicos em aplicações AWS:  
A) AWS Shield Standard B) Route 53 only C) EBS snapshot D) IAM group

16. Para bloquear SQL injection e XSS em app web:  
A) AWS WAF B) CloudWatch C) Budgets D) Kinesis

17. Melhor ferramenta para custos históricos e tendências:  
A) Cost Explorer B) Pricing Calculator C) Trusted Advisor only D) ACM

18. Estimativa de custo antes de criar ambiente novo:  
A) Pricing Calculator B) CloudTrail C) Config D) IAM

19. Para acompanhar conformidade de configurações, usar:  
A) AWS Config B) CloudFront C) S3 Transfer D) SES

20. Para recomendações de rightsizing, usar:  
A) Compute Optimizer B) CodeCommit C) AppSync D) Rekognition

21. Logs, métricas e alarmes centralizados:  
A) CloudWatch B) IAM C) KMS D) Route53

22. Armazenamento de objetos durável para backup e data lake:  
A) Amazon S3 B) EBS C) EFS only D) Instance Store

23. File system compartilhado Linux em múltiplas AZs:  
A) EFS B) EBS C) S3 D) Glacier Vault Lock

24. Data warehouse analítico gerenciado:  
A) Redshift B) DynamoDB C) ElastiCache D) DocumentDB

25. Banco NoSQL serverless para baixa latência:  
A) DynamoDB B) Aurora C) RDS D) Neptune

26. Consulta SQL direta em dados no S3:  
A) Athena B) EMR only C) MQ D) SNS

27. ETL gerenciado serverless para catálogo e transformação:  
A) AWS Glue B) Lambda@Edge C) WAF D) EC2 bare metal

28. Transferir grandes dados físicos de on-prem para AWS:  
A) Snowball B) DataSync only C) SQS D) Route53

29. Conexão dedicada e privada com baixa variação para datacenter:  
A) Direct Connect B) Internet pública C) Site-to-Site somente D) NAT

30. Para acesso remoto seguro a instâncias sem abrir SSH público:  
A) Session Manager B) Bastion aberto C) Telnet D) FTP

31. Modelo de responsabilidade compartilhada: cliente é responsável por:  
A) Configuração e dados B) Segurança física do datacenter C) Hardware do host D) Energia

32. Para criptografar dados em repouso em vários serviços:  
A) KMS B) IAM only C) Route53 D) SQS DLQ

33. Prática de segurança para usuários humanos:  
A) IAM Identity Center + grupos/permissões B) Chaves de acesso estáticas C) Root diário D) Sem MFA

34. Cenário de app global, estático e barato:  
A) S3 static + CloudFront B) EC2 pesada C) RDS-only D) EBS-only

35. Quando usar Multi-AZ em banco?  
A) Alta disponibilidade e failover B) Reduzir latência global C) Diminuir domínio DNS D) Evitar backup

36. Para workflow com etapas e retries visuais:  
A) Step Functions B) SQS C) SNS D) IAM

37. Melhor opção para pipeline CI/CD AWS nativo:  
A) CodePipeline + CodeBuild + CodeDeploy B) CloudTrail + IAM C) Route53 + WAF D) S3 + EFS only

38. Para container image registry gerenciado:  
A) ECR B) ECS C) EKS D) EC2

39. Execução de containers sem gerenciar servidor:  
A) Fargate B) EC2 manual C) Lightsail DB D) DynamoDB

40. Para eventos de aplicações SaaS e AWS centralizados:  
A) EventBridge B) SNS only C) SQS only D) Route53

41. Aplicação precisa cache de sessão de baixa latência:  
A) ElastiCache B) S3 C) Glacier D) Athena

42. Para enviar e-mail transacional em escala:  
A) SES B) SNS C) SQS D) Kinesis

43. Banco de grafos para relações complexas:  
A) Neptune B) RDS C) DynamoDB D) Redshift

44. Busca textual e analytics de logs:  
A) OpenSearch Service B) Aurora C) Glue D) SES

45. Para documentação e visibilidade de custos executivos:  
A) Dashboards e revisões periódicas B) Sem KPI C) Revisão anual única D) Sem dono

46. Melhor estratégia para reduzir custo em cargas estáveis:  
A) Savings Plans/RI com análise B) Spot para tudo C) On-demand fixo D) Sem monitorar

47. Recurso para ação automática ao atingir orçamento (quando suportado):  
A) Budget Actions B) CloudTrail Insights C) WAF rule D) NAT policy

48. Em incidentes, fonte de verdade de chamadas API:  
A) CloudTrail B) CloudWatch Logs apenas C) SNS D) S3 inventory

49. Para compliance e trilha de configuração histórica:  
A) AWS Config B) IAM Access Analyzer C) Shield D) EC2

50. Melhor prática para menor privilégio:  
A) Políticas mínimas necessárias B) Admin para todos C) Root compartilhado D) Sem revisão

51. Estratégia de DR com objetivo de menor RTO em geral:  
A) Planejamento com múltiplas estratégias e testes B) Sem backup C) Apenas snapshot anual D) Sem runbook

52. Para proteger dados sensíveis no S3 de exclusão acidental:  
A) Versionamento + MFA Delete (quando aplicável) B) Bucket público C) Sem políticas D) Sem logs

53. Para separar ambientes e limites de segurança/custo:  
A) Multi-account strategy B) Uma conta única sem OU C) Root em equipe D) Sem tagging

54. Para detectar anomalias de custo (conceito finops):  
A) Monitoramento contínuo e alertas B) Revisão semestral C) Sem baseline D) Sem histórico

55. Aplicação com picos em horários fixos: abordagem ideal de custo/escala:  
A) Auto Scaling + agendamento quando cabível B) Capacidade máxima fixa C) Sem métricas D) Sem alarmes

56. Para autenticação centralizada de colaboradores, melhor serviço/conceito:  
A) IAM Identity Center B) IAM user compartilhado C) Chave root D) ACL pública

57. Benefício principal da nuvem em inovação:  
A) Agilidade para experimentar e iterar B) CapEx alto obrigatório C) Provisionamento lento D) Hardware próprio obrigatório

58. Para latência global menor em API pública, considerar:  
A) CloudFront + arquitetura regional adequada B) Apenas uma instância distante C) Sem cache D) Só VPN

59. Para accountability de custos por time/produto:  
A) Tags obrigatórias + showback/chargeback B) Sem classificação C) Custos agregados únicos D) Sem governança

60. Qual resumo melhor representa prontidão para CLF-C02?  
A) Entender valor de nuvem, segurança, tecnologia e custos integrados B) Decorar apenas siglas C) Ignorar finanças D) Ignorar responsabilidade compartilhada
---

Creditos autorais:
- Thiago Cardoso - https://www.linkedin.com/in/analyticsthiagocardoso
- Pedro Albertini - https://www.linkedin.com/in/pedroalbertini/
- Lucas Garcia - https://www.linkedin.com/in/lucas-del-puerto/