# AWS Infrastructure as Code (IaC) Project com CI/CD

Este projeto implementa uma infraestrutura completa na AWS usando Terraform, com uma aplicação Flask containerizada e um pipeline CI/CD totalmente automatizado usando GitHub Actions.

## 🎯 Funcionalidades Implementadas

- **Infraestrutura Automatizada**: VPC, Subnets, Security Groups - tudo como código
- **Pipeline CI/CD**: Integração e deploy contínuos com GitHub Actions
- **Containerização**: Aplicação Flask em containers Docker
- **Alta Disponibilidade**: Múltiplas AZs com subnets públicas e privadas
- **Segurança**: Security groups e IAM roles com menor privilégio

## 🏗️ Arquitetura

A arquitetura foi projetada seguindo as melhores práticas da AWS:

- **VPC** (10.0.0.0/16)
  - 2 Subnets Públicas (10.0.1.0/24 e 10.0.2.0/24)
  - 2 Subnets Privadas (10.0.3.0/24 e 10.0.4.0/24)
  - Internet Gateway para acesso público
  - Security Groups para ALB e containers

## 📁 Estrutura do Projeto

### `/app` - Aplicação Flask
- `src/app.py`: Aplicação principal com endpoints:
  ```python
  @app.route('/health')
  def health_check():
      return jsonify({'status': 'healthy'})

  @app.route('/')
  def hello():
      return jsonify({
          'environment': 'development',
          'message': 'Hello from DevOps Project!'
      })
  ```

- `tests/test_app.py`: Testes unitários com pytest
- `Dockerfile`: Configuração para desenvolvimento e testes
- `requirements.txt`: Dependências Python (Flask 2.3.3 e Gunicorn 21.2.0)

### `/terraform` - Infraestrutura como Código
- `main.tf`: Configuração da VPC e recursos de rede
  ```hcl
  resource "aws_vpc" "main" {
    cidr_block           = "10.0.0.0/16"
    enable_dns_hostnames = true
    enable_dns_support   = true
  }
  ```

- `variables.tf`: Variáveis configuráveis (região, ambiente, ECR)
- `outputs.tf`: Outputs importantes (IDs de VPC, subnets, security groups)

### `/.github/workflows` - Pipeline CI/CD
- `main.yml`: Workflow do GitHub Actions
  ```yaml
  name: CI/CD Pipeline
  on:
    push:
      branches: [ main, master ]
  ```

## 🚀 Como Usar Este Projeto

### Pré-requisitos

1. AWS CLI instalado e configurado
2. Terraform instalado (v5.0+)
3. Docker instalado
4. Python 3.12+
5. Conta GitHub

### Configuração Inicial

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/aws-iac-project.git
   cd aws-iac-project
   ```

2. Configure as credenciais AWS:
   ```bash
   aws configure
   ```

3. Configure as secrets no GitHub:
   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_REGION

### Deploy Local da Aplicação

1. Crie e ative o ambiente virtual:
   ```bash
   cd app
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Execute os testes:
   ```bash
   pytest tests/
   ```

3. Execute com Docker:
   ```bash
   docker build -t flask-app .
   docker run -p 80:80 flask-app
   ```

### Deploy na AWS

1. Inicialize o Terraform:
   ```bash
   cd terraform
   terraform init
   ```

2. Revise o plano:
   ```bash
   terraform plan
   ```

3. Aplique a infraestrutura:
   ```bash
   terraform apply
   ```

## 🔒 Segurança

### Security Groups
- ALB: Aceita tráfego HTTP (porta 80)
- Tasks: Aceita tráfego apenas do ALB na porta 5000

### Network
- Subnets privadas para containers
- Subnets públicas apenas para o ALB
- Internet Gateway para acesso público

## 💰 Considerações de Custo

Componentes que geram custos:
1. **VPC**: Custos mínimos (NAT Gateway se usado)
2. **ALB**: ~$0.0225/hora
3. **ECR**: $0.10/GB/mês

Para evitar custos:
```bash
cd terraform
terraform destroy
```

## 🔍 Monitoramento

- Logs da aplicação via stdout/stderr
- Métricas do ALB
- Health checks na rota `/health`

## 🤝 Contribuindo

1. Fork o projeto
2. Crie sua feature branch (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📝 Notas de Versão

- **v1.0.0** (13/03/2025)
  - Implementação inicial com VPC e networking
  - Aplicação Flask básica
  - Pipeline CI/CD com GitHub Actions

## 📫 Contato

Brendo Trindade - [LinkedIn](seu-linkedin) - seu.email@exemplo.com

## 📜 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes
