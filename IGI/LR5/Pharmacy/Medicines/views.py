from django.shortcuts import render
from .models import Medicines, Categories

from functions.menu import load_medicines

def medicines(request, dep_id, cat_id):
    cat = Categories.objects.filter(id=cat_id)[0]
    meds = Medicines.objects.filter(category=cat)

    context = {
        'departments' : load_medicines(),
        'meds': meds,
        'category_id': cat_id,
        'department_id': dep_id
        }
    return render(request, "Medicines/medicines.html", context)

def medicine(request, dep_id, cat_id, med_id):
    med = Medicines.objects.filter(id=med_id)[0]

    context = {
        'departments' : load_medicines(),
        'med': med,
        }
    return render(request, "Medicines/medicine.html", context)