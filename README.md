# 🎬 Flix API

API REST completa para gerenciamento de filmes, desenvolvida com Django REST Framework. Sistema completo com autenticação JWT, CRUD de filmes, atores, gêneros e sistema de avaliações.

## 📋 Características

- ✅ **Autenticação JWT** - Sistema seguro de autenticação com tokens
- ✅ **CRUD Completo** - Operações completas para filmes, atores, gêneros e avaliações
- ✅ **Django REST Framework** - API RESTful robusta e escalável
- ✅ **Banco de Dados SQLite** - Banco de dados leve e fácil de configurar
- ✅ **Clean Code** - Código organizado seguindo boas práticas
- ✅ **Documentação Completa** - README detalhado com exemplos

## 🚀 Tecnologias

- **Django 5.0.4** - Framework web Python
- **Django REST Framework 3.15.1** - Framework para construção de APIs REST
- **djangorestframework-simplejwt 5.3.1** - Autenticação JWT
- **Python 3.8+** - Linguagem de programação

## 📦 Estrutura do Projeto

```
flix_api/
├── app/                    # Configurações principais do Django
│   ├── settings.py         # Configurações do projeto
│   ├── urls.py             # URLs principais
│   └── wsgi.py             # WSGI config
├── authentication/         # App de autenticação
├── genres/                 # App de gêneros
├── actors/                 # App de atores
├── movies/                 # App de filmes
├── reviews/                # App de avaliações
├── manage.py               # Script de gerenciamento Django
├── requirements.txt        # Dependências do projeto
└── db.sqlite3              # Banco de dados SQLite
```

## 🔧 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório:**

```bash
git clone https://github.com/christianresende/flix_api.git
cd flix_api
```

2. **Crie um ambiente virtual (recomendado):**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Execute as migrações:**

```bash
python manage.py migrate
```

5. **Crie um superusuário (opcional):**

```bash
python manage.py createsuperuser
```

6. **Execute o servidor de desenvolvimento:**

```bash
python manage.py runserver
```

A API estará disponível em: `http://localhost:8000/`

## 📚 Endpoints da API

### Autenticação

#### Registrar Usuário
```
POST /api/auth/register/
```

**Body:**
```json
{
  "username": "usuario",
  "email": "usuario@email.com",
  "password": "senha123"
}
```

#### Obter Token de Acesso
```
POST /api/auth/token/
```

**Body:**
```json
{
  "username": "usuario",
  "password": "senha123"
}
```

**Response:**
```json
{
  "access": "token_de_acesso",
  "refresh": "token_de_refresh"
}
```

#### Atualizar Token
```
POST /api/auth/token/refresh/
```

**Body:**
```json
{
  "refresh": "token_de_refresh"
}
```

### Filmes

- `GET /api/movies/` - Listar todos os filmes
- `POST /api/movies/` - Criar novo filme (requer autenticação)
- `GET /api/movies/{id}/` - Detalhes de um filme
- `PUT /api/movies/{id}/` - Atualizar filme (requer autenticação)
- `DELETE /api/movies/{id}/` - Deletar filme (requer autenticação)

### Atores

- `GET /api/actors/` - Listar todos os atores
- `POST /api/actors/` - Criar novo ator (requer autenticação)
- `GET /api/actors/{id}/` - Detalhes de um ator
- `PUT /api/actors/{id}/` - Atualizar ator (requer autenticação)
- `DELETE /api/actors/{id}/` - Deletar ator (requer autenticação)

### Gêneros

- `GET /api/genres/` - Listar todos os gêneros
- `POST /api/genres/` - Criar novo gênero (requer autenticação)
- `GET /api/genres/{id}/` - Detalhes de um gênero
- `PUT /api/genres/{id}/` - Atualizar gênero (requer autenticação)
- `DELETE /api/genres/{id}/` - Deletar gênero (requer autenticação)

### Avaliações

- `GET /api/reviews/` - Listar todas as avaliações
- `POST /api/reviews/` - Criar nova avaliação (requer autenticação)
- `GET /api/reviews/{id}/` - Detalhes de uma avaliação
- `PUT /api/reviews/{id}/` - Atualizar avaliação (requer autenticação)
- `DELETE /api/reviews/{id}/` - Deletar avaliação (requer autenticação)

## 🔐 Autenticação

A API utiliza JWT (JSON Web Tokens) para autenticação. Para acessar endpoints protegidos:

1. Obtenha um token de acesso através do endpoint `/api/auth/token/`
2. Inclua o token no header das requisições:

```
Authorization: Bearer {seu_token_de_acesso}
```

### Exemplo com cURL

```bash
# Obter token
curl -X POST http://localhost:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "usuario", "password": "senha123"}'

# Usar token em requisição
curl -X GET http://localhost:8000/api/movies/ \
  -H "Authorization: Bearer {seu_token_de_acesso}"
```

### Exemplo com Python (requests)

```python
import requests

# Obter token
response = requests.post('http://localhost:8000/api/auth/token/', json={
    'username': 'usuario',
    'password': 'senha123'
})
token = response.json()['access']

# Usar token em requisição
headers = {'Authorization': f'Bearer {token}'}
response = requests.get('http://localhost:8000/api/movies/', headers=headers)
movies = response.json()
```

## 🛠️ Desenvolvimento

### Executar Testes

```bash
python manage.py test
```

### Criar Migrações

```bash
python manage.py makemigrations
```

### Aplicar Migrações

```bash
python manage.py migrate
```

### Acessar Admin do Django

1. Crie um superusuário (se ainda não tiver):
```bash
python manage.py createsuperuser
```

2. Acesse: `http://localhost:8000/admin/`

## 📝 Configurações JWT

As configurações de JWT podem ser ajustadas em `app/settings.py`:

```python
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),    # Token de acesso válido por 1 dia
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),   # Token de refresh válido por 7 dias
}
```

## 🗄️ Banco de Dados

O projeto utiliza SQLite por padrão. Para usar outro banco de dados (PostgreSQL, MySQL, etc.), configure em `app/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🚀 Deploy

### Variáveis de Ambiente Importantes

Antes de fazer deploy em produção, configure:

- `SECRET_KEY` - Chave secreta do Django (não compartilhe!)
- `DEBUG=False` - Desative o modo debug
- `ALLOWED_HOSTS` - Configure os hosts permitidos
- Configure um banco de dados de produção (PostgreSQL recomendado)

### Exemplo de Deploy no Heroku

1. Instale o Heroku CLI
2. Crie um arquivo `Procfile`:
```
web: gunicorn app.wsgi --log-file -
```

3. Configure as variáveis de ambiente no Heroku
4. Faça o deploy:
```bash
git push heroku main
```

## 📄 Licença

Este projeto é de código aberto e está disponível para uso livre.

## 👤 Autor

**Christian Resende**

- GitHub: [@christianresende](https://github.com/christianresende)
- LinkedIn: [Christian Resende](https://www.linkedin.com/in/christian-resende/)

## 🙏 Agradecimentos

- Django REST Framework pela excelente documentação
- Comunidade Django pela suporte e recursos

## 📞 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!
