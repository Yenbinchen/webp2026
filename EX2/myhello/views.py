from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MyHello
from .serializers import MyHelloSerializer

class HelloApiView(APIView):
    # 這就是 List Post (取得清單)
    def get(self, request):
        data = MyHello.objects.all()
        serializer = MyHelloSerializer(data, many=True)
        return Response(serializer.data)

    # 這就是 Add Post (新增資料)
    def post(self, request):
        serializer = MyHelloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)