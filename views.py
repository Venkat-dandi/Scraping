from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import NewsItem
from .serializers import NewsItemSerializer

class NewsAPIView(APIView):
    def post(self, request):
        serializer = NewsItemSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NewsListAPIView(APIView):
    def get(self, request):
        news_items = NewsItem.objects.all()
        serializer = NewsItemSerializer(news_items, many=True)
        return Response(serializer.data)
