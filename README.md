# 📛 Django REST API – Book Management

This project is a simple RESTful API for managing books, built with Django REST Framework. It supports basic CRUD operations and is Dockerized for easy deployment.

---

## 🚀 Features

- Add, update, delete, and list books
- Django REST Framework-powered API
- Dockerized setup
- Unit tests included
- Pre-commit hooks for code quality

---

## 🛠️ Tech Stack

- Python 3.10
- Django 4.x
- Django REST Framework
- Docker
- SQLite (default DB)
- Pre-commit (black, flake8, detect-secrets)

---

## 📆 Setup Instructions

### ✅ Running Locally (with virtualenv/pyenv)

```bash
# Clone the repo
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo

# Create virtual environment
pyenv virtualenv 3.10.0 ci-cd
pyenv activate ci-cd

# Install dependencies
pip install -r requirements.txt

# Apply migrations and run server
python manage.py migrate
python manage.py runserver
```

---

### 🐳 Running with Docker

```bash
# Build Docker image
sudo docker build -t my-django-app .

# Run the container
sudo docker run -p 8000:8000 my-django-app
```

---

## 🔪 Running Tests

```bash
python manage.py test
```

---

## 📍 API Overview

| Endpoint          | Method | Description       |
| ----------------- | ------ | ----------------- |
| `/api/books/`     | GET    | List all books    |
| `/api/books/`     | POST   | Create a new book |
| `/api/books/<id>` | PUT    | Update a book     |
| `/api/books/<id>` | DELETE | Delete a book     |

> Use tools like Postman or `curl` to test these endpoints.

---

## 🪩 Pre-commit Hooks

This project uses `pre-commit` to ensure clean, consistent code.

### Setup:

```bash
pip install pre-commit
pre-commit install
```

### Run all hooks manually:

```bash
pre-commit run --all-files
```

### Included Hooks:

- `black` – Python code formatter
- `flake8` – Linter
- `detect-secrets` – Detect secrets in code
- `end-of-file-fixer`, `trailing-whitespace`, `check-yaml`, etc.

---

## 📄 License

Apache License
