from django.shortcuts import render

# Create your views here.
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope


class Test(APIView):
    permission_classes = [IsAuthenticated,TokenHasReadWriteScope]

    def get(self):
        data={'app':'app2','data':22}
        json_data = data
        return Response(json_data)

