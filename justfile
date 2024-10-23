# Run development server
s:
    ./manage.py runserver

# Check Django project
c:
    ./manage.py check

# Generate migrations
mm:
    ./manage.py makemigrations

# Apply migrations
m:
    ./manage.py migrate

# Remove migrations and database. Reset DB artefacts.
[confirm("⚠️ All migrations and database will be removed. Continue? [yN]:")]
r:
    #!/usr/bin/env bash
    find . -path "*/migrations/*.py" ! -path "./.venv/*" ! -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc" ! -path "./.venv/*" -delete
    rm -f db.sqlite3
    ./manage.py makemigrations
    ./manage.py migrate
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | ./manage.py shell
    echo
    echo "Creating superuser → admin:admin ... OK"

# Open sqlite project database
db:
    sqlite3 db.sqlite3

# Open a Django interactive shell.
sh:
    ./manage.py shell