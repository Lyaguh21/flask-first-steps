```
routes/ — только HTTP: валидация входных данных, статус-коды, JSON-ответы.

services/ — логика и запросы (CRUD), бизнес-правила.

models/ — таблицы/отношения (SQLAlchemy модели).

extensions.py — единые инстансы db, migrate.

create_app() — сборка приложения и регистрация блюпринтов.
```

## Запуск

1. Установка виртуального окружения и зависимостей

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

```

2. Создание файла .env

```powershell
FLASK_APP=app.py
FLASK_DEBUG=1
SECRET_KEY=dev-secret
DATABASE_URL=postgresql+psycopg2://appuser:apppass@localhost:5432/appdb

```

3. Запуск приложения

```powershell
docker compose up -d
flask db upgrade
flask run
```
