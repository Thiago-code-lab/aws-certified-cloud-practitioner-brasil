# Domínio 2 - Security and Compliance (60 questões)

1. Qual serviço registra chamadas de API para auditoria?  
A) CloudTrail B) CloudWatch C) Budgets D) Route 53

2. Qual serviço gerencia usuários, grupos e políticas de acesso?  
A) IAM B) KMS C) GuardDuty D) Inspector

3. Qual recurso do IAM concede permissões temporárias para serviços AWS?  
A) IAM Role B) Access key estática C) Security Group D) NACL

4. Qual prática é recomendada para conta root?  
A) Habilitar MFA e restringir uso B) Compartilhar senha C) Usar em tarefas diárias D) Desativar trilhas

5. Qual serviço gerencia chaves criptográficas na AWS?  
A) KMS B) ACM C) SSM D) CloudFront

6. Qual serviço armazena segredos com rotação automática?  
A) Secrets Manager B) Parameter Store apenas C) Artifact D) CloudTrail

7. Qual serviço ajuda na detecção inteligente de ameaças?  
A) GuardDuty B) Cost Explorer C) Budgets D) Route 53

8. Qual serviço avalia postura de segurança e recomendações?  
A) Security Hub B) S3 C) Lambda D) EBS

9. Qual serviço ajuda a avaliar conformidade de configurações?  
A) AWS Config B) CloudFront C) API Gateway D) SNS

10. Security Group é melhor descrito como:  
A) Firewall stateful em nível de recurso B) DNS gerenciado C) Serviço de custo D) Registro de API

11. NACL é melhor descrito como:  
A) Controle stateless em nível de subnet B) IAM policy C) Log de auditoria D) Balanceador

12. Qual serviço protege contra DDoS por padrão?  
A) AWS Shield Standard B) WAF C) GuardDuty D) Inspector

13. Qual serviço protege aplicações web contra SQLi/XSS?  
A) AWS WAF B) KMS C) IAM D) Macie

14. No modelo compartilhado, classificar dados é responsabilidade de:  
A) Cliente B) AWS sempre C) Provedor de internet D) Marketplace

15. Criptografia em repouso significa:  
A) Dados armazenados criptografados B) Dados em trânsito HTTPS C) Logs sem retenção D) Tokenização manual

16. Criptografia em trânsito significa:  
A) Dados protegidos durante tráfego de rede B) Dados salvos em disco C) Dados públicos D) Backup sem TLS

17. Qual serviço fornece certificados TLS gerenciados?  
A) AWS Certificate Manager B) IAM C) SQS D) ECS

18. Qual ação implementa princípio de menor privilégio?  
A) Permitir apenas ações necessárias B) Política admin para todos C) Sem MFA D) Usuário root para apps

19. Qual é o benefício de roles para serviços?  
A) Credenciais temporárias e mais seguras B) Senhas fixas em código C) Menos rastreabilidade D) Sem rotação

20. CloudTrail responde melhor qual pergunta?  
A) Quem fez o quê, quando B) Quanto custou por serviço C) Qual throughput atual D) Qual latência CDN

21. Qual serviço centraliza findings de segurança?  
A) Security Hub B) Cost Explorer C) Glue D) Athena

22. Qual serviço descobre dados sensíveis em S3?  
A) Amazon Macie B) AWS Budgets C) CloudHSM D) WAF

23. Qual prática melhora governança de acesso?  
A) Revisão periódica de permissões B) Compartilhar usuários C) Chaves sem rotação D) Sem trilhas

24. Qual recurso do IAM evita credenciais de longo prazo em EC2?  
A) Instance profile com role B) Usuário IAM local C) Access key hardcoded D) Root key

25. Qual opção é exemplo de autenticação multifator?  
A) MFA no login B) Apenas senha forte C) IP fixo D) CIDR privado

26. Qual serviço ajuda em análise de vulnerabilidades em workloads?  
A) Amazon Inspector B) Amazon Kendra C) Amazon Rekognition D) CodeBuild

27. Qual prática reduz risco de exposição de dados?  
A) Criptografar e restringir acesso B) Bucket público por padrão C) Sem logs D) Sem versionamento

28. O que significa “defense in depth”?  
A) Controles em múltiplas camadas B) Um único firewall C) Sem IAM D) Apenas antivírus

29. Qual serviço permite auditoria de compliance por regras?  
A) AWS Config Rules B) Route 53 health checks C) ALB D) Auto Scaling

30. Qual cenário é melhor para Secrets Manager?  
A) Senhas de banco e rotação B) Conteúdo estático público C) DNS records D) Cache de sessão

31. Qual serviço disponibiliza relatórios de conformidade AWS?  
A) AWS Artifact B) CloudWatch C) X-Ray D) S3 Inventory

32. Qual prática melhora segurança operacional?  
A) Centralizar logs e alertas B) Desligar monitoramento C) Evitar patching D) Sem backup

33. Qual risco de usar credenciais estáticas no código-fonte?  
A) Vazamento e comprometimento B) Melhor performance C) Menor custo D) Maior observabilidade

34. Qual recurso limita acesso por condição (ex: IP, MFA)?  
A) IAM policy conditions B) Route tables C) SNS topics D) SQS queues

35. Qual serviço ajuda a proteger contas multi-account em escala?  
A) AWS Organizations + SCPs B) EC2 Auto Scaling C) CloudFront D) EFS

36. SCP no AWS Organizations faz o quê?  
A) Define limites máximos de permissões B) Substitui IAM local C) Cria backups D) Gera certificados

37. Qual prática fortalece identidade humana?  
A) SSO centralizado + MFA B) Conta compartilhada C) Root no dia a dia D) Senha única sem MFA

38. Qual prática fortalece identidade de workload?  
A) Roles temporárias B) Chave fixa embutida C) Root access D) NACL aberto

39. Qual opção descreve confidencialidade de dados?  
A) Somente autorizados acessam dados B) Dados sempre disponíveis C) Dados íntegros sem alteração D) Dados com baixa latência

40. Qual opção descreve integridade de dados?  
A) Dados não alterados indevidamente B) Dados públicos C) Dados com custo baixo D) Dados sem backup

41. Qual opção descreve disponibilidade em segurança?  
A) Acesso quando necessário por usuários autorizados B) Acesso irrestrito sempre C) Sem autenticação D) Sem redundância

42. Qual ação em incident response é essencial?  
A) Detectar, conter, erradicar e recuperar B) Ignorar alertas C) Desligar logs D) Excluir trilhas

43. Qual serviço pode acionar automações de resposta?  
A) EventBridge integrado com Lambda/SSM B) S3 static website C) Route 53 only D) ACM only

44. Qual prática reduz superfície de ataque de rede?  
A) Regras mínimas em SG/NACL B) Abrir todas as portas C) Expor banco público D) Desativar firewall

45. Qual boa prática para buckets S3 sensíveis?  
A) Bloqueio de acesso público + criptografia B) Acesso público total C) Sem política D) Sem versionamento

46. Qual serviço ajuda a gerenciar postura de segurança de forma central?  
A) Security Hub B) Cloud9 C) Lightsail D) SES

47. Qual benefício do CloudTrail em investigações?  
A) Trilhas de auditoria detalhadas B) Estimativa de custo C) Aceleração de rede D) Escalabilidade automática

48. Qual controle evita exclusão acidental de recursos críticos por API?  
A) Políticas IAM/SCP restritivas B) Sem MFA C) Sem logs D) Bucket público

49. Qual prática suporta compliance contínuo?  
A) Config Rules + remediação automática B) Auditoria anual única C) Sem baseline D) Sem tagging

50. Qual prática é recomendada para chaves KMS?  
A) Rotação e políticas mínimas B) Compartilhar chave universal C) Sem monitorar uso D) Sem backup de chave

51. Qual camada o WAF protege principalmente?  
A) Camada de aplicação (L7) B) Camada física C) Camada de link D) Camada de energia

52. Qual camada o Shield protege principalmente?  
A) Mitigação DDoS de rede/aplicação B) Criptografia de disco C) IAM user lifecycle D) DNS routing

53. Qual prática ajuda na rastreabilidade de ações administrativas?  
A) CloudTrail habilitado em todas as regiões B) Somente logs locais C) Sem retenção D) Sem timestamp

54. Qual serviço oferece análise de postura e recomendações de segurança/custos?  
A) Trusted Advisor B) Polly C) Rekognition D) Bedrock

55. Qual ação reduz risco de privilege escalation?  
A) Revisar políticas amplas e remover wildcards desnecessários B) Dar admin para acelerar C) Usar root em automação D) Ignorar logs IAM

56. Qual prática melhora proteção de dados pessoais (LGPD)?  
A) Minimização, criptografia e controle de acesso B) Publicação ampla C) Coleta irrestrita D) Sem retenção definida

57. Qual artefato ajuda auditorias externas?  
A) Relatórios no AWS Artifact B) Alarmes do CloudWatch apenas C) DNS records D) AMIs públicas

58. Qual objetivo de um plano de resposta a incidentes?  
A) Reduzir impacto e tempo de recuperação B) Eliminar necessidade de segurança C) Aumentar custo D) Evitar monitoramento

59. Qual prática de segurança é alinhada ao exame CLF-C02?  
A) Least privilege + MFA + logging B) Root sem MFA C) Sem trilhas D) Sem criptografia

60. Qual combinação melhora maturidade de segurança na AWS?  
A) IAM forte + criptografia + detecção + resposta B) Apenas firewall C) Apenas antivírus D) Apenas backup
