#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from .models import TuWen
from .serializers import TuWenModelSerializer

# 引入drf的功能组件
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


class GetTuWenView(APIView):
    """获取图文列表"""

    renderer_classes = [JSONRenderer]

    def get(self, request):
        t_list = TuWen.objects.all()
        re = TuWenModelSerializer(t_list, many=True)
        return Response(re.data)

