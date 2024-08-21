# Use a imagem base do Python 3.10 (versão slim para uma imagem menor)
FROM python:3.10-slim

# Defina o diretório de trabalho no container
# Isso significa que todos os comandos subsequentes serão executados dentro desse diretório
WORKDIR /app

# Instale as dependências do sistema necessárias para compilar e instalar o mysqlclient
# Atualiza a lista de pacotes e instala os pacotes necessários
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/list

# Copia o arquivo requirements.txt do diretório local para o container
COPY requirements.txt .

# Atualiza o pip para a versão mais recente e instala as dependências Python
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação para o container
COPY . .

# Cria as migrações do Django para criar/atualizar o esquema do banco de dados
RUN python manage.py makemigrations

# Permite que o script wait-for-it.sh seja executado
RUN chmod +x wait-for-it.sh

# Expõe a porta 8000 (opcional)
# Isso permite que a porta 8000 seja acessível fora do container
EXPOSE 8000

# Comando padrão para rodar o servidor Django
# O wait-for-it.sh garante que o banco de dados esteja pronto antes de iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
