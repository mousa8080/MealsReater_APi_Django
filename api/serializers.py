from rest_framework import serializers

from api.models import Meal,Rating

class MealSerializer(serializers.ModelSerializer):
  class Meta:
    model = Meal
    fields = ('id', 'title', 'description')
class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rating
    fields = ('id', 'user', 'meal', 'stars')