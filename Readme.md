# Instruções para Iniciar a Aplicação com Docker

Este documento fornece instruções para construir e executar a aplicação usando Docker e Docker Compose. A aplicação está configurada com Django e Django REST Framework (DRF).

## Requisitos

- [Docker](https://docs.docker.com/get-docker/) (versão recomendada 27.1.2 ou superior)
- [Docker Compose](https://docs.docker.com/compose/install/) (versão recomendada 2.29.2 ou superior)

## Instruções

### 1. Clonar o Repositório

Se você ainda não clonou o repositório, faça isso com o comando:
```bash
git clone <URL-do-repositorio>
cd <nome-do-repositorio>
```

### 2. Construir e Iniciar os Containers
Para construir a imagem Docker e iniciar os containers, execute:
```bash
docker-compose up --build
```

### 3. Executar Migrações
Após os containers estarem em execução, execute as seguintes migrações para configurar o banco de dados:
```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```
- `makemigrations` cria novas migrações com base nas alterações feitas nos modelos.
- `migrate` aplica essas migrações ao banco de dados.

### 4. Criar um Superusuário (Opcional)
Se você precisar criar um superusuário para acessar o painel de administração do Django, use o comando:
```bash
docker-compose exec web python manage.py createsuperuser
```

Siga as instruções no terminal para definir um nome de usuário, e-mail e senha para o superusuário.

### 5. Parar e Remover os Containers
Para parar os containers em execução e remover os containers, redes e volumes criados, use:
```bash
docker-compose down
```

### 6. Ver Logs
Para visualizar os logs dos containers, execute:
```bash
docker-compose logs
```
Ou para um container específico:

```bash
docker-compose logs <nome-do-serviço>
```
Substitua `<nome-do-serviço>` pelo nome do serviço definido no `docker-compose.yml`, como web.