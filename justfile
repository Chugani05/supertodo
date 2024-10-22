# Levantar el servidor de desarrollo
dev:
    ./manage.py runserver

# Comprobar el proyecto Django
check:
    ./manage.py check

# Crear las migraciones
mm:
    ./manage.py makemigrations

# Aplicar las migraciones
m:
    ./manage.py migrate

# Remove migrations and database. Reset DB artefacts.
[confirm("⚠️ All migrations and database will be removed. Continue? [yN]:")]
reset-db:
    #!/usr/bin/env bash
    find . -path "*/migrations/*.py" ! -path "./.venv/*" ! -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc" ! -path "./.venv/*" -delete
    rm -f db.sqlite3
    ./manage.py makemigrations
    ./manage.py migrate
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | ./manage.py shell
    echo
    echo "Creating superuser → admin:admin ... OK"