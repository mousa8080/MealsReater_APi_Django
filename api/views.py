
from rest_framework import viewsets
from .models import Rating,Meal
from .serializers import RatingSerializer,MealSerializer


class RatingViewSet(viewsets.ModelViewSet):
  queryset = Rating.objects.all()
  serializer_class = RatingSerializer

class MealViewSet(viewsets.ModelViewSet):
  queryset = Meal.objects.all()
  serializer_class = MealSerializer