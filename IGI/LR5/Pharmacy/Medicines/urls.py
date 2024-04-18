from django.urls import path
from Medicines import views

app_name = 'medicines'

urlpatterns = [
    path('search/', views.departments, name='search'),
    path('sales/', views.sales, name='sales'),
    path('', views.departments, name='deps'),
    path('<int:dep_id>/', views.department, name='dep'),
    path('<int:dep_id>/<int:cat_id>/', views.medicines, name='meds'),
    path('<int:dep_id>/<int:cat_id>/<int:med_id>/', views.medicine, name='med'),
]
