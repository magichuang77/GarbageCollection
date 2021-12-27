import requests

from rest_framework import authentication
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response


# Create your views here.

# 垃圾搜搜
# 垃圾回收
# class GarbageViewSet(viewsets.ModelViewSet):
class GarbageView(views.APIView):
    # get请求
    def get(self, request, *args, **kwargs):
        gbname = request.get("gbname", "")
        if not gbname:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        api_url = "https://smartmll.com/ajax.php?gbname={}".format(gbname)
        res = requests.get(api_url).json()
        data = {}
        if 'code' in res and res['code'] == "200":

        return Response(data={}, status=status.HTTP_200_OK)
