from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r"^buliang/$", views.BuLiangWeiXiu.as_view()),
    re_path(r"^hebing/$", views.HeBingShuJu.as_view()),
]





