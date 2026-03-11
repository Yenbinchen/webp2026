from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# 請檢查這行的類別名稱 (MyHelloAPIView) 是否拼錯
class MyHelloAPIView(APIView):
    def get(self, request):
        name = request.GET.get('name', None)
        if name and name.strip():
            return Response({"res": f"Hello {name}"}, status=status.HTTP_200_OK)
        else:
            return Response({"res": "parameter: name is None"}, status=status.HTTP_400_BAD_REQUEST)