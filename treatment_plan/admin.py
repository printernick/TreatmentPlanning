from django.contrib import admin
from .models import ClientPresentation, Treatment, ExternalResource

admin.site.register(ClientPresentation)
admin.site.register(Treatment)
admin.site.register(ExternalResource)