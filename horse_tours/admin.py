from django.contrib import admin
from .models import Person, Horse, TourCompany, Review, Service

admin.site.register(Person)
admin.site.register(Horse)
admin.site.register(TourCompany)
admin.site.register(Review)
admin.site.register(Service)