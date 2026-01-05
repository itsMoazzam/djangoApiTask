# 🚀 Django REST API Project

This repository contains a **Django REST API project** built using:

- Django
- Django REST Framework (DRF)
- Simple JWT Authentication
- PostgreSQL Database

Follow the steps below to set up the project locally, create a virtual environment, apply migrations, and run the server.

---

## 📌 Prerequisites

Make sure you have the following installed on your system:

- **Python 3.9 or above**
- **pip**
- **PostgreSQL**
- **Git**

Check versions:

```bash```
python --version
pip --version

git clone https://github.com/itsMoazzam/djangoApiTask.git
cd djangoApiTask

python -m venv venv
venv\Scripts\activate

* pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary python-dotenv

pip freeze > requirements.txt




# Add this in settings.py file db
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'defaultdb',
        'USER': 'avnadmin',
        'PASSWORD': 'AVNS_qrTwEkR5xatq9NODN5N',
        'HOST': 'pg-15a2fed2-ranamoazam954-f1d8.l.aivencloud.com',
        'PORT': '16467',  
    }
}
