from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r"^xinbuliang/$", views.BuLiangWeiXiu.as_view()),
    re_path(r"^xinhebing/$", views.HeBingShuJu.as_view()),
    re_path(r"^xianti/$", views.XiantiView.as_view()),
    re_path(r"^kpi/$", views.KpiView.as_view()),
    re_path(r"^xiantishuju/$", views.XiantishujuView.as_view()),
    re_path(r"^xiangqin/$", views.XiangqinShujuView.as_view()),
    re_path(r"^jixing/$", views.JixingShujuView.as_view()),
]





