from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.views import View
import json
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
# Create your views here.


class LoginView(View):

    def post(self, request):
        json_dict = json.loads(request.body.decode())
        username = json_dict.get('username')
        password = json_dict.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return JsonResponse({'code': 200, 'message': '登录成功', 'data': {'token': token}})
        else:
            return HttpResponseForbidden("用户名或密码错误")

