from reviews.serializers import ReviewSerializer
from reviews.models import Review   
from rest_framework.viewsets import ModelViewSet

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Create your views here.
