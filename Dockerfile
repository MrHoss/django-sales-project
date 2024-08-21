# Use a imagem base do Python
FROM python:3.10-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Instale as dependências do sistema necessárias para o mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copie o arquivo requirements.txt para o container
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código para o container
COPY . .

# Exponha a porta (opcional, dependendo do seu projeto)
EXPOSE 8000

# Comando para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
