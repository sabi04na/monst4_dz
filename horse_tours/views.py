from django.shortcuts import render
from .models import TourCompany
from django.db.models import Avg

def company_rating_view(request):
    companies = TourCompany.objects.annotate(
        average_rating=Avg('reviews__rating')
    )
    return render(request, 'horse_tours/rating.html', {'companies': companies})

# Create your views here.
