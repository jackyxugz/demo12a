#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from rest_framework import serializers
from .models import TuWen


class TuWenModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuWen
        fields = "__all__"
