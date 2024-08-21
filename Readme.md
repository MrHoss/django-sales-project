# Instruções para Iniciar a Aplicação com Docker

Este documento fornece instruções para construir e executar a aplicação usando Docker e Docker Compose. A aplicação está configurada com Django REST Framework (DRF).

## Requisitos

- [Docker](https://docs.docker.com/get-docker/) (versão recomendada 27.1.2 ou superior)
- [Docker Compose](https://docs.docker.com/compose/install/) (versão recomendada 2.29.2 ou superior)

## Instruções

### 1. Clonar o Repositório

Se você ainda não clonou o repositório, faça isso com o comando:
```bash
git clone git@github.com:MrHoss/django-sales-project.git
cd django-sales-project
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

---

# Instruções de Uso da API

## Uso de endpoints

### 1. Produtos

#### Listar Produtos

```http
GET /api/produtos/
```

**Exemplo de Resposta:**

```json
[
    {
        "id": 1,
        "nome": "Produto A",
        "preco": "100.00",
        "descricao": "Descrição do Produto A"
    },
    ...
]
```

#### Criar Produto

```http
POST /api/produtos/
```

**Corpo da Requisição:**

```json
{
    "nome": "Produto Novo",
    "preco": "150.00",
    "descricao": "Descrição do Novo Produto"
}
```

#### Atualizar Produto

```http
PUT /api/produtos/{id}/
```

**Corpo da Requisição:**

```json
{
    "nome": "Produto Atualizado",
    "preco": "200.00",
    "descricao": "Descrição Atualizada"
}
```

#### Deletar Produto

```http
DELETE /api/produtos/{id}/
```

---

### 2. Clientes

#### Listar Clientes

```http
GET /api/clientes/
```

**Exemplo de Resposta:**

```json
[
    {
        "id": 1,
        "nome": "Cliente A",
        "email": "clientea@example.com"
    },
    ...
]
```

#### Criar Cliente

```http
POST /api/clientes/
```

**Corpo da Requisição:**

```json
{
    "nome": "Cliente Novo",
    "email": "clientenovo@example.com"
}
```

#### Atualizar Cliente

```http
PUT /api/clientes/{id}/
```

**Corpo da Requisição:**

```json
{
    "nome": "Cliente Atualizado",
    "email": "clienteatualizado@example.com"
}
```

#### Deletar Cliente

```http
DELETE /api/clientes/{id}/
```

---

### 3. Grupo de Produto

#### Listar Grupos de Produtos

```http
GET /api/grupo_produto/
```

**Exemplo de Resposta:**

```json
[
    {
        "id": 1,
        "nome": "Grupo A"
    },
    ...
]
```

#### Criar Grupo de Produto

```http
POST /api/grupo_produto/
```

**Corpo da Requisição:**

```json
{
    "nome": "Grupo Novo"
}
```

#### Atualizar Grupo de Produto

```http
PUT /api/grupo_produto/{id}/
```

**Corpo da Requisição:**

```json
{
    "nome": "Grupo Atualizado"
}
```

#### Deletar Grupo de Produto

```http
DELETE /api/grupo_produto/{id}/
```

---

### 4. Vendas

#### Listar Vendas

```http
GET /api/vendas/
```

**Exemplo de Resposta:**

```json
[
    {
        "id": 1,
        "cliente": 1,
        "vendedor": 1,
        "data_venda": "2024-08-20",
        "total": "500.00",
        "itens": [
            {
                "produto": 1,
                "quantidade": 2,
                "preco": "100.00"
            },
            ...
        ]
    },
    ...
]
```

#### Criar Venda

```http
POST /api/vendas/
```

**Corpo da Requisição:**

```json
{
    "cliente": 1,
    "vendedor": 1,
    "data_venda": "2024-08-20",
    "itens": [
        {
            "produto": 1,
            "quantidade": 2
        },
        ...
    ]
}
```

#### Atualizar Venda

```http
PUT /api/vendas/{id}/
```

**Corpo da Requisição:**

```json
{
    "cliente": 1,
    "vendedor": 1,
    "data_venda": "2024-08-20",
    "itens": [
        {
            "id": 1,
            "produto": 1,
            "quantidade": 3
        },
        ...
    ]
}
```

#### Deletar Venda

```http
DELETE /api/vendas/{id}/
```

---

### 5. Vendedores

#### Listar Vendedores

```http
GET /api/vendedores/
```

**Exemplo de Resposta:**

```json
[
    {
        "id": 1,
        "nome": "Vendedor A",
        "email": "vendedora@example.com"
    },
    ...
]
```

#### Criar Vendedor

```http
POST /api/vendedores/
```

**Corpo da Requisição:**

```json
{
    "nome": "Vendedor Novo",
    "email": "vendedornovo@example.com"
}
```

#### Atualizar Vendedor

```http
PUT /api/vendedores/{id}/
```

**Corpo da Requisição:**

```json
{
    "nome": "Vendedor Atualizado",
    "email": "vendedoratualizado@example.com"
}
```

#### Deletar Vendedor

```http
DELETE /api/vendedores/{id}/
```

---

### 6. Relatórios

#### Obter Relatório em PDF

Para gerar um relatório em PDF das vendas, use a seguinte rota:

```http
GET /api/relatorios/vendas/?data_inicial=2024-01-01&data_final=2024-12-31&vendedor=Shirley&cliente=Maria&format=pdf
```

**Parâmetros:**

- `data_inicial` (opcional): Data inicial para o filtro de vendas no formato `YYYY-MM-DD`.
- `data_final` (opcional): Data final para o filtro de vendas no formato `YYYY-MM-DD`.
- `vendedor` (opcional): Nome do vendedor para filtrar as vendas.
- `cliente` (opcional): Nome do cliente para filtrar as vendas.
- `format` (opcional): O formato do relatório. Pode ser `pdf` ou `excel`. O padrão é `pdf`.

#### Obter Relatório em Excel

Para gerar um relatório em Excel das vendas, use a seguinte rota:

```http
GET /api/relatorios/vendas/?data_inicial=2024-01-01&data_final=2024-12-31&vendedor=Shirley&cliente=Maria&format=excel
```

**Parâmetros:**

- `data_inicial` (opcional): Data inicial para o filtro de vendas no formato `YYYY-MM-DD`.
- `data_final` (opcional): Data final para o filtro de vendas no formato `YYYY-MM-DD`.
- `vendedor` (opcional): Nome do vendedor para filtrar as vendas.
- `cliente` (opcional): Nome do cliente para filtrar as vendas.
- `format` (opcional): O formato do relatório. Pode ser `pdf` ou `excel`. O padrão é `pdf`.


