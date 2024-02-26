# How to set up
## 1. This project uses Python 3.12.1
The packages are also found in `requirements.txt`

## 2. Clone the repository
```
git clone https://github.com/sergelorenz/django-email-classifier.git
```

## 3. Create virtual environment and activate
```
cd django-email-classifier
python -m venv .venv
```
For windows users:
```
.venv/Scripts/activate
```
For linux users:
```
source .venv/bin/activate
```

## 4. Install the packages
```
pip install -r requirements.txt
```

## 5. Migrate all necessary database schema
```
cd emailclassifier
python manage.py migrate
```

## 6. Run the application
```
python manage.py runserver
```

## 7. **Note**: You need to create `superuser` during the first time running the application


# How to Regenerate Migrations into one file
From [github/mhipo1364/merge_migration.md](https://gist.github.com/mhipo1364/a55da230e1ec80bfab70e9650637bb15).

To merge exist migration files into one file:

  - Remove `django_migration` records table (manually)
  - Remove all migration files
  - run `python manage.py migrate --fake` command
  - run `python manage.py makemigrations` command
  - run `python manage.py migrate --fake-initial` command
  - run `python manage.py migrate contenttypes` command
  - and finally, for chacking if everything is just fine, run `python manage.py migrate` command
 
Now, check `django_migration` table and make sure all new files added in this table
