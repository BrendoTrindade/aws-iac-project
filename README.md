# AWS Infrastructure as Code (IaC) Project

Este projeto demonstra a implementação de uma infraestrutura completa na AWS usando práticas modernas de DevOps e IaC.

## Objetivos do Projeto

- Implementar uma aplicação Flask em containers Docker
- Criar uma infraestrutura completa na AWS usando Terraform
- Estabelecer um pipeline de CI/CD com GitHub Actions
- Demonstrar boas práticas de DevOps e IaC

## Arquitetura

O projeto utiliza os seguintes serviços AWS:
- Amazon ECS (Elastic Container Service) para orquestração de containers
- Amazon ECR (Elastic Container Registry) para armazenamento de imagens Docker
- Application Load Balancer para distribuição de tráfego
- VPC com subnets públicas e privadas
- IAM roles e policies para segurança

## Estrutura do Projeto

```
aws-iac-project/
├── .github/
│   └── workflows/
│       └── main.yml           # Pipeline CI/CD
├── app/
│   ├── src/
│   │   └── app.py            # Aplicação Flask
│   ├── tests/
│   │   └── test_app.py       # Testes unitários
│   ├── Dockerfile            # Build da imagem Docker
│   └── requirements.txt      # Dependências Python
└── terraform/
    ├── backend.tf            # Configuração do backend Terraform
    ├── ecs.tf               # Configuração do ECS
    ├── iam.tf               # Roles e políticas IAM
    ├── main.tf              # Recursos principais (VPC, etc)
    ├── outputs.tf           # Outputs da infraestrutura
    ├── variables.tf         # Variáveis do Terraform
    └── terraform.tfstate    # Estado do Terraform (local)
```

## Como Executar

### Pré-requisitos

- AWS CLI configurado
- Terraform instalado
- Docker instalado
- Python 3.x instalado

### Configuração Local

1. Clone o repositório:
```bash
git clone [https://github.com/BrendoTrindade/aws-iac-project.git]
cd aws-iac-project
```

2. Configure o ambiente Python:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
pip install -r app/requirements.txt
```

3. Execute os testes:
```bash
cd app
python -m pytest
```

### Deploy na AWS

1. Inicialize o Terraform:
```bash
cd terraform
terraform init
```

2. Revise o plano de infraestrutura:
```bash
terraform plan
```

3. Aplique a infraestrutura:
```bash
terraform apply
```

4. Após a confirmação do deploy, a URL do Application Load Balancer estará disponível nos outputs.

## Segurança

- Todos os recursos são criados dentro de uma VPC privada
- Uso de security groups para controle de acesso
- IAM roles com permissões mínimas necessárias
- Secrets do GitHub Actions para credenciais AWS

## Custos

Este projeto utiliza recursos AWS que podem gerar custos. Para evitar cobranças indesejadas:

1. Sempre destrua os recursos quando não estiver usando:
```bash
terraform destroy
```

2. Monitore seus gastos no AWS Cost Explorer
3. Configure alertas de billing

## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Contato

- LinkedIn: [Seu Nome]([https://linkedin.com/in/seu-perfil](https://www.linkedin.com/in/brendo-trindade/))
- Email: brendofut44l@gmail.com
