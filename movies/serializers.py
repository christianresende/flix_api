from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg

class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        return round(rate, 1) or None
    
    
        # reviews = obj.reviews.all()
        # rate = 0
        # if reviews:
        #     rate = sum([review.stars for review in reviews]) / len(reviews)
        # return round(rate, 1)