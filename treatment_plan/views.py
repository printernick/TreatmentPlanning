from django.shortcuts import render
from .models import ClientPresentation, Treatment

def home(request):
    context = {
        "clientPresentations": ClientPresentation.objects.all(),
        "observations": Treatment.objects.filter(treatment_type="OB"),
        "longTermGoals": Treatment.objects.filter(treatment_type="LT"),
        "shortTermObjectives": Treatment.objects.filter(treatment_type="ST"),
        "therapeuticInterventions": Treatment.objects.filter(treatment_type="TI"),
        "clientProgresses": Treatment.objects.filter(treatment_type="CP"),
        "plans": Treatment.objects.filter(treatment_type="PL")
    }
    
    clientPresentationId = request.GET.get('id', None)
    if clientPresentationId != None:
        context['id'] = clientPresentationId
    else:
        context['id'] = 1

    return render(request, 'treatment_plan/home.html', context)

