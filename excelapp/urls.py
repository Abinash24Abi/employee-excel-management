from django.urls import path
from .views import home, upload_excel, upload_summary, export_pdf, export_excel, export_csv, export_txt

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload_excel, name='upload_excel'),
    path('upload/summary/', upload_summary, name='upload_summary'),
    path('export/pdf/', export_pdf, name='export_pdf'),
    path('export/excel/', export_excel, name='export_excel'),
    path('export/csv/', export_csv, name='export_csv'),
    path('export/txt/', export_txt, name='export_txt'),
]                                                                           
