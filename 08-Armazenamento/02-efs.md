# Amazon EFS

## O que é
EFS é sistema de arquivos NFS totalmente gerenciado, escalável e compartilhado entre múltiplas instâncias.

## Quando usar
- Aplicações Linux com acesso concorrente ao mesmo filesystem.
- Conteúdo compartilhado entre instâncias e containers.

## Pontos de prova
- Serviço regional com alta disponibilidade multi-AZ.
- Cobrança por volume armazenado e classes de acesso.

## CLI útil
```bash
aws efs describe-file-systems
aws efs describe-mount-targets --file-system-id <id>
```
---

Creditos autorais:
- Thiago Cardoso - https://www.linkedin.com/in/analyticsthiagocardoso
- Pedro Albertini - https://www.linkedin.com/in/pedroalbertini/
- Lucas Garcia - https://www.linkedin.com/in/lucas-del-puerto/