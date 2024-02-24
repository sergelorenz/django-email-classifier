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