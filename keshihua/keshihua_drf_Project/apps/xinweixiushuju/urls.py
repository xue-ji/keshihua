from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r"^xinbuliang/$", views.BuLiangWeiXiu.as_view()),
    re_path(r"^xinhebing/$", views.HeBingShuJu.as_view()),
    re_path(r"^xianti/$", views.XiantiView.as_view()),
]





