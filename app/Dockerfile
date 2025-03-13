FROM python:3.12-slim

WORKDIR /app

# Copiar todo o conteúdo do diretório app
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt pytest

# Adicionar o diretório src ao PYTHONPATH
ENV PYTHONPATH=/app/src

EXPOSE 80

# Comando para executar testes
CMD ["pytest", "tests/test_app.py", "-v"]
