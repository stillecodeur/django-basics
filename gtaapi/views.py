import datetime
import logging
import sqlite3

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.templatetags.rest_framework import data
from rest_framework import status

from gtaapi.serializers import UserSerializer
from rest_framework import viewsets
from gtaapi.models import User


# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self, data, msg, error, **kwargs):
        content = JSONRenderer().render({"status": msg, "error": error, "data": data})
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_ser = UserSerializer(users, many=True)
        return JSONResponse(msg="success", error=False, data=user_ser.data)

    elif request.method == 'POST':
            user_data = JSONParser().parse(request)
            user_ser = UserSerializer(data=user_data)
            if user_ser.is_valid():
                user_ser.save()
                return JSONResponse(msg="success", error=False, data=user_ser.data, status=status.HTTP_201_CREATED)
            return JSONResponse(msg=user_ser.errors, error=True, data={}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def user_detail(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return JSONResponse(msg="invalid id", error=True, data={}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_ser = UserSerializer(user)
        return JSONResponse(msg="success", error=False, data=user_ser.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_ser = UserSerializer(user, user_data)
        if user_ser.is_valid():
            user_ser.save()
            return JSONResponse(msg="updated", error=False, data=user_ser.data, status=status.HTTP_200_OK)
        return JSONResponse(msg="invalid request data", error=True, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return JSONResponse(msg="deleted", error=False, data={}, status=status.HTTP_204_NO_CONTENT)
