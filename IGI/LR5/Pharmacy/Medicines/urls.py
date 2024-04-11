from django.urls import path
from Medicines import views

urlpatterns = [
    path('<int:dep_id>/<int:cat_id>/', views.medicines, name='med'),
]
