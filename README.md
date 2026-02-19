# 🚀 Employee Excel Management System

A professional Django-based web application to upload, manage, update, and export employee data using Excel files.

This system supports intelligent data handling including insert, update, skip logic and multiple export formats.

---

## 📌 Project Overview

The Employee Excel Management System allows users to:

- Upload Excel (.xlsx) files
- Insert new employee records
- Update existing employee records
- Skip unchanged duplicate records
- View all records in table format
- Export records in multiple formats (PDF, Excel, CSV, TXT)
- View upload summary dashboard

This project demonstrates real-world backend logic and enterprise-level data handling.

---

## 🛠 Tech Stack

- Python 3.x
- Django
- MySQL
- Bootstrap 5
- OpenPyXL
- Pandas
- ReportLab
- pypandoc

---

2️⃣ Create Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate


Mac/Linux:

python3 -m venv venv
source venv/bin/activate

3️⃣ Install Required Packages

pip install django mysqlclient openpyxl pandas reportlab pypandoc


4️⃣ Configure MySQL Database

Create a database in MySQL:

Database Name: excel_db

Update settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'excel_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


5️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate


6️⃣ Run the Development Server
python manage.py runserver


Open in browser:

http://127.0.0.1:8000/


