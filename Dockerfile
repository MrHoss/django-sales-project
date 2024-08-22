FROM python:3.10-slim

WORKDIR /app

# Instale as dependências do sistema necessárias para compilar e instalar o mysqlclient
# Atualiza a lista de pacotes e instala os pacotes necessários
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/list

COPY requirements.txt .

# Atualiza o pip para a versão mais recente e instala as dependências Python
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Cria as migrações do Django para criar/atualizar o esquema do banco de dados
RUN python manage.py makemigrations

RUN chmod +x wait-for-it.sh

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
