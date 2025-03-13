# DevOps Project with AWS and Terraform

Este projeto demonstra a implementação de uma infraestrutura como código (IaC) usando AWS e Terraform, com um pipeline de CI/CD usando GitHub Actions.

## Arquitetura

- **Aplicação**: Flask API em Python
- **Containerização**: Docker
- **CI/CD**: GitHub Actions
- **Infraestrutura**: AWS (VPC, Subnets, Security Groups) gerenciada com Terraform

## Estrutura do Projeto

```
aws-iac-project/
├── .github/workflows/    # Pipeline CI/CD
├── app/                  # Aplicação Flask
│   ├── src/             # Código fonte
│   ├── tests/           # Testes
│   ├── Dockerfile       # Containerização
│   └── requirements.txt # Dependências
└── terraform/           # Infraestrutura como Código
    ├── main.tf
    ├── variables.tf
    └── outputs.tf
```

## Executando Localmente

1. Clone o repositório:
```bash
git clone <repository-url>
cd aws-iac-project
```

2. Execute a aplicação com Docker Compose:
```bash
docker-compose up
```

3. Acesse a aplicação:
- http://localhost:80/ - Mensagem de boas-vindas
- http://localhost:80/health - Status da aplicação

## Executando os Testes

```bash
docker-compose run --rm test
```

## Deploy

1. Configure as credenciais AWS como secrets no GitHub:
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY

2. Faça push para a branch main:
```bash
git add .
git commit -m "Update application"
git push origin main
```

O pipeline do GitHub Actions irá:
1. Executar os testes
2. Construir e publicar a imagem Docker no ECR
3. Aplicar a infraestrutura com Terraform

## Infraestrutura AWS

- VPC (10.0.0.0/16)
- 2 Subnets Públicas
- 2 Subnets Privadas
- Internet Gateway
- Security Groups para ALB e ECS
