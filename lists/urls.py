from django.urls import path, include
from . import views

app_name = 'lists'

urlpatterns = [
    path('list/', views.ListView, name='list_view'),
    path('insert/<slug:date>', views.InsertData, name='insert_data'),
    path('download-excel/', views.DownloadExcel, name='download_excel'),
    path('download-excel-all/', views.DownloadExcelAll, name='download_excel_all'),

    # path('api/v1/date_download', views.DateExcel.as_view(), name='Date_Excel'), 
]