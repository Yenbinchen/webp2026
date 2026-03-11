from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MyHelloAPIView(APIView):
    def get(self, request):
        # 從網址 query string 取得 name 參數，例如 ?name=Jack
        name = request.GET.get('name', None)
        
        if name and name.strip():
            # 如果有名字，回傳 200 OK
            return Response({"res": f"Hello {name}"}, status=status.HTTP_200_OK)
        else:
            # 如果沒名字，回傳你截圖中的 400 Bad Request
            return Response({"res": "parameter: name is None"}, status=status.HTTP_400_BAD_REQUEST)