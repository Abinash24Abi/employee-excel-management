🚀 Employee Excel Management System

A professional Django-based web application to upload, manage, update, and export employee data using Excel files.

This system supports intelligent data handling including insert, update, skip logic, and multiple export formats — designed to demonstrate real-world backend processing and enterprise-level data management.

📌 Project Overview

The Employee Excel Management System allows users to:

📂 Upload Excel (.xlsx) files

➕ Insert new employee records

🔄 Update existing employee records

⏭ Skip unchanged duplicate records

📊 View all employee records in table format

📤 Export records in multiple formats:

PDF

Excel

CSV

TXT

📈 View upload summary dashboard

🛠 Tech Stack

Python 3.x

Django

MySQL

Bootstrap 5

OpenPyXL

Pandas

ReportLab

pypandoc

📁 Project Structure
employee_excel_system/
│
├── manage.py
├── requirements.txt
├── db.sqlite3 (if used for development)
│
├── employee_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│
└── static/

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/employee-excel-management.git
cd employee-excel-management

2️⃣ Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate

Mac/Linux
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Required Packages
pip install django mysqlclient openpyxl pandas reportlab pypandoc


Or install from requirements file:

pip install -r requirements.txt

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

6️⃣ Run Development Server
python manage.py runserver


Open in browser:

http://127.0.0.1:8000/
