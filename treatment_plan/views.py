from django.shortcuts import render
from .models import ClientPresentation, Treatment

def home(request):
    context = {
        "clientPresentations": sorted(ClientPresentation.objects.all()),
        "observations": sorted(Treatment.objects.filter(treatment_type="OB")),
        "longTermGoals": sorted(Treatment.objects.filter(treatment_type="LT")),
        "shortTermObjectives": sorted(Treatment.objects.filter(treatment_type="ST")),
        "therapeuticInterventions": sorted(Treatment.objects.filter(treatment_type="TI")),
        "clientProgresses": sorted(Treatment.objects.filter(treatment_type="CP")),
        "plans": sorted(Treatment.objects.filter(treatment_type="PL"))
    }
    
    clientPresentationId = request.GET.get('id', None)
    if clientPresentationId != None:
        context['id'] = clientPresentationId
    else:
        context['id'] = context["clientPresentations"][0].id
    
    return render(request, 'treatment_plan/home.html', context)

