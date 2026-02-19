# 🚀 Employee Excel Management System

A powerful Django-based web application for managing employee data through Excel uploads.

This system intelligently processes employee records by inserting new data, updating existing records, and skipping unchanged entries — just like real enterprise software.

------------------------------------------------------------

✨ FEATURES

✔ Upload Excel (.xlsx) files  
✔ Intelligent Insert / Update / Skip logic  
✔ Clean table view of employee records  
✔ Upload summary dashboard  
✔ Export data in multiple formats:
    • PDF
    • Excel (.xlsx)
    • CSV
    • TXT  
✔ Django Admin panel support  

------------------------------------------------------------

🛠 TECHNOLOGY STACK

Backend:
- Python 3.x
- Django
- MySQL

Frontend:
- Bootstrap 5

Libraries Used:
- OpenPyXL
- Pandas
- ReportLab
- pypandoc

------------------------------------------------------------

🧠 INTELLIGENT DATA PROCESSING

When an Excel file is uploaded:

• If employee does NOT exist → INSERT  
• If employee exists and data changed → UPDATE  
• If employee exists and data unchanged → SKIP  

After upload, system shows:

- Total Records Processed
- Inserted Records
- Updated Records
- Skipped Records

------------------------------------------------------------

⚙ INSTALLATION GUIDE

1️⃣ Create Virtual Environment

Windows:
python -m venv venv
venv\Scripts\activate

Mac/Linux:
python3 -m venv venv
source venv/bin/activate

2️⃣ Install Required Packages

pip install django mysqlclient openpyxl pandas reportlab pypandoc

3️⃣ Configure MySQL Database

Create a database:

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

4️⃣ Apply Migrations

 -  python manage.py makemigrations
 -  python manage.py migrate

5️⃣ Run the Server

python manage.py runserver

Open in browser:
http://127.0.0.1:8000/

------------------------------------------------------------

📊 EXCEL FORMAT REQUIRED

Your Excel file should contain columns like:

Employee ID | Name | Email | Department | Salary | Date Joined

Column names must match the Django model fields.

------------------------------------------------------------

📤 EXPORT OPTIONS

Download employee data in:

• PDF  
• Excel (.xlsx)  
• CSV  
• TXT  

------------------------------------------------------------

🔐 ADMIN ACCESS

Create admin user:

python manage.py createsuperuser

Access admin panel:
http://127.0.0.1:8000/admin/

------------------------------------------------------------

🎯 PROJECT HIGHLIGHTS

• Real-world backend logic  
• Clean and structured Django architecture  
• Enterprise-style data validation  
• Multiple export formats  
• Professional project for portfolio  

------------------------------------------------------------

🚀 FUTURE ENHANCEMENTS

• User authentication system  
• REST API integration  
• Cloud deployment (AWS / Render)  
• Docker support  

------------------------------------------------------------

👨‍💻 Author
Your Name  
Abinash K
