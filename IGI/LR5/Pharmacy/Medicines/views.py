from django.shortcuts import render
from .models import Medicines, Categories

from functions.menu import load_medicines

def medicines(request, dep_id, cat_id):
    cat = Categories.objects.filter(id=cat_id)[0]
    meds = Medicines.objects.filter(category=cat)

    context = {
        'departments' : load_medicines(),
        'meds': meds
        }
    return render(request, "Medicines/medicines.html", context)