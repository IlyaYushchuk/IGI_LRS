from django.shortcuts import render
from .models import Medicines, Categories, Departments

from functions.menu import load_medicines

def medicines(request, dep_id, cat_id):
    cat = Categories.objects.filter(id=cat_id)[0]

    meds = []
    for med in Medicines.objects.filter(category=cat):
        temp = {
            'dep_id': dep_id,
            'cat_id': cat_id,
            'med': med
        }
        meds.append(temp)

    context = {
        'departments' : load_medicines(),
        'meds': meds,
        }
    return render(request, "Medicines/medicines.html", context)

def medicine(request, dep_id, cat_id, med_id):
    med = Medicines.objects.filter(id=med_id)[0]

    context = {
        'departments' : load_medicines(),
        'med': med,
        }
    return render(request, "Medicines/medicine.html", context)

def department(request, dep_id):
    dep = Departments.objects.filter(id=dep_id)[0]
    meds = []
    for cat in Categories.objects.filter(department=dep):
        for med in Medicines.objects.filter(category=cat):
            temp = {
                'dep_id': dep_id,
                'cat_id': cat.id,
                'med': med
            }
            meds.append(temp)

    context = {
        'departments' : load_medicines(),
        'meds': meds,
        }
    return render(request, "Medicines/medicines.html", context)

def departments(request):
    meds = []
    for dep in Departments.objects.all():
        for cat in Categories.objects.filter(department=dep):
            for med in Medicines.objects.filter(category=cat):
                temp = {
                    'dep_id': dep.id,
                    'cat_id': cat.id,
                    'med': med
                }
                meds.append(temp)

    context = {
        'departments' : load_medicines(),
        'meds': meds,
        }
    return render(request, "Medicines/medicines.html", context)