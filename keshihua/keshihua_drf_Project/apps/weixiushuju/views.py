from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views import View
from pyecharts import options as opts
from pyecharts.charts import Pie, Timeline, Grid, Line, Page, Liquid, Bar
from pyecharts.commons.utils import JsCode
import pandas as pd
from pathlib import Path
import os
# 只需要在顶部声明 CurrentConfig.ONLINE_HOST 即可
from pyecharts.globals import CurrentConfig, OnlineHostType
import matplotlib
import xlrd
from pandas import DataFrame
from pyecharts.faker import Faker
from pyecharts.components import Table
import numpy as np
from pyecharts.globals import ThemeType, ChartType


# Create your views here.


class BuLiangWeiXiu(View):

    def get(self, request):
        df_weixiu = pd.read_excel(r'D:\桌面\anli\weixiushuju.xlsx')
        total = sum(count[1] for count in [size for size in df_weixiu['不良原因'].value_counts().items()])
        list1 = [size for size in df_weixiu['不良原因'].value_counts().items()]


        total_a0_list = list1[0]
        total_a0 = total_a0_list[0]

        # list1[0]表示list1中的第1列

        total_a0_list = list1[0]
        total_b0 = total_a0_list[1]

        # total_a0_list[1]表示第一行的第2位数字

        total_a1_list = list1[1]
        total_a1 = total_a1_list[0]


        total_a1_list = list1[1]
        total_b1 = total_a1_list[1]


        total_a2_list = list1[2]
        total_a2 = total_a2_list[0]


        total_a2_list = list1[2]
        total_b2 = total_a2_list[1]


        total_a3_list = list1[3]
        total_a3 = total_a3_list[0]


        total_a3_list = list1[3]
        total_b3 = total_a3_list[1]


        total_a4_list = list1[4]
        total_a4 = total_a4_list[0]


        total_a4_list = list1[4]
        total_b4 = total_a4_list[1]


        d0 = round(total_b0 / total, 2) * 100


        d1 = round(total_b1 / total, 2) * 100


        d2 = round(total_b2 / total, 2) * 100


        d3 = round(total_b3 / total, 3) * 100


        d4 = round(total_b4 / total, 2) * 100


        c0 = '{:.1%}'.format(total_b0 / total)


        c1 = '{:.1%}'.format(total_b1 / total)


        c2 = '{:.1%}'.format(total_b2 / total)


        c3 = '{:.1%}'.format(total_b3 / total)


        c4 = '{:.1%}'.format(total_b4 / total)

        fn = """
            function(params) {
                if(params.name == '其他')
                    return '\\n\\n\\n' + params.name + ' : ' + params.value + '%';
                return params.name + ' : ' + params.value + '%';
            }
            """

        def new_label_opts():
            return opts.LabelOpts(formatter=JsCode(fn), position="center")

        c = (
            Pie()
            .add(
                "",
                [list(z) for z in zip([total_a0, ""], [d0, ])],
                center=["20%", "30%"],
                radius=[60, 80],
                label_opts=new_label_opts(),
            )
            .add(
                "",
                [list(z) for z in zip([total_a1, ""], [d1, ])],
                center=["60%", "30%"],
                radius=[60, 80],
                label_opts=new_label_opts(),
            )
            .add(
                "",
                [list(z) for z in zip([total_a2, ""], [d2, ])],
                center=["20%", "70%"],
                radius=[60, 80],
                label_opts=new_label_opts(),
            )
            .add(
                "",
                [list(z) for z in zip([total_a3, ""], [d3, ])],
                center=["60%", "70%"],
                radius=[60, 80],
                label_opts=new_label_opts(),
            )
            .add(
                "",
                [list(z) for z in zip([total_a4, ""], [d4, ])],
                center=["40%", "50%"],
                radius=[60, 80],
                label_opts=new_label_opts(),
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="TOP5多比饼图"),
                legend_opts=opts.LegendOpts(
                    type_="scroll", pos_top="20%", pos_left="80%", orient="vertical"
                ),
            )
            .render(os.path.join(Path(__file__).resolve().parent.parent.parent.parent) + r'\templates\top5.html')

        )
        # 解码变成字符串
        html1 = render(request, 'top5.html').content.decode()
        # 分割获取body里面的数据
        html2 = html1.split('body')
        # print(html2[1][2:-2])
        # 获取完成再转码
        html3 = html2[1][2:-2]
        return HttpResponse(html1)


class HeBingShuJu(View):

    def get(self, request):

        # # OnlineHostType.NOTEBOOK_HOST 默认值为 http://localhost:8888/nbextensions/assets/
        # CurrentConfig.ONLINE_HOST = OnlineHostType.NOTEBOOK_HOST
        df_weixiu = pd.read_excel(r'D:\桌面\anli\weixiushuju.xlsx')
        df_weixiu

        list1 = [size for size in df_weixiu['成品料号描述'].value_counts().items()]
        list1

        data1 = [size for size in df_weixiu['成品料号描述'].value_counts().items()]
        jixing = [item[0] for item in data1]
        jixing

        data1 = [size for size in df_weixiu['成品料号描述'].value_counts().items()]
        jixingshuliang = [item[1] for item in data1]
        jixingshuliang


        pie1 = (
            Bar()
            .add_xaxis(jixing)
            .add_yaxis("机型数据分析", jixingshuliang)
            .set_global_opts(
                title_opts=opts.TitleOpts(title="机型数据分析（slider-水平）"),
                datazoom_opts=opts.DataZoomOpts(),
            )
        )
        pie1.render_notebook()


        df_weixiu = pd.read_excel(r'D:\桌面\anli\weixiushuju.xlsx')
        df_weixiu

        list1 = [size for size in df_weixiu['责任类别'].value_counts().items()]
        list1

        data1 = [size for size in df_weixiu['责任类别'].value_counts().items()]
        liebie = [item[0] for item in data1]
        liebie

        data1 = [size for size in df_weixiu['责任类别'].value_counts().items()]
        zerenleibie = [item[1] for item in data1]
        zerenleibie

        data1 = [size for size in df_weixiu['责任类别'].value_counts().items()]
        liebie = [item[0] for item in data1]
        liebie

        total1 = sum(count[1] for count in [size for size in df_weixiu['责任类别'].value_counts().items()])
        total1

        zeren_a0_list = list1[0]
        zeren_b0 = zeren_a0_list[1]
        zeren_b0

        zeren_a1_list = list1[1]
        zeren_b1 = zeren_a1_list[1]
        zeren_b1

        zeren_a2_list = list1[2]
        zeren_b2 = zeren_a2_list[1]
        zeren_b2

        zeren_a3_list = list1[3]
        zeren_b3 = zeren_a3_list[1]
        zeren_b3

        zeren_a4_list = list1[4]
        zeren_b4 = zeren_a4_list[1]
        zeren_b4

        e0 = '{:.1%}'.format(zeren_b0 / total1)
        e0

        e1 = '{:.1%}'.format(zeren_b1 / total1)
        e1

        e2 = '{:.1%}'.format(zeren_b2 / total1)
        e2

        e3 = '{:.1%}'.format(zeren_b3 / total1)
        e3

        e4 = '{:.1%}'.format(zeren_b4 / total1)
        e4

        list2 = [e0, e1, e2, e3, e4]
        list2


        fn = """
            function(params) {
                if(params.name == '其他')
                    return '\\n\\n\\n' + params.name + ' : ' + params.value + '%';
                return params.name + ' : ' + params.value + '%';
            }
            """

        def new_label_opts():
            return opts.LabelOpts(formatter=JsCode(fn), position="center")

        v = liebie
        pie2 = (
            Pie()
            .add(
                "",
                [list(z) for z in zip(list2, zerenleibie)],
                radius=["30%", "55%"],
                center=["25%", "60%"],
                rosetype="radius",
                label_opts=opts.LabelOpts(is_show=True),
            )
            .add(
                "",
                [list(z) for z in zip(v, zerenleibie)],
                radius=["30%", "55%"],
                center=["70%", "60%"],
                rosetype="area",
            )

            .set_global_opts(title_opts=opts.TitleOpts(title="维修不良类别TOP5-玫瑰图"),

                             legend_opts=opts.LegendOpts(pos_left="25%", orient="horizontal"))

            .set_series_opts(
                tooltip_opts=opts.TooltipOpts(
                    trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
                )
            )

        )
        pie2.render_notebook()


        df_weixiu = pd.read_excel(r'D:\桌面\anli\weixiushuju.xlsx')
        df_weixiu

        list1 = [size for size in df_weixiu['不良原因'].value_counts().items()]
        list1

        total_a0_list = list1[0]
        total_a0 = total_a0_list[0]
        total_a0
        # list1[0]表示list1中的第1列

        total_a0_list = list1[0]
        total_b0 = total_a0_list[1]
        total_b0
        # total_a0_list[1]表示第一行的第2位数字

        total_a1_list = list1[1]
        total_a1 = total_a1_list[0]
        total_a1

        total_a1_list = list1[1]
        total_b1 = total_a1_list[1]
        total_b1

        total_a2_list = list1[2]
        total_a2 = total_a2_list[0]
        total_a2

        total_a2_list = list1[2]
        total_b2 = total_a2_list[1]
        total_b2

        total_a3_list = list1[3]
        total_a3 = total_a3_list[0]
        total_a3

        total_a3_list = list1[3]
        total_b3 = total_a3_list[1]
        total_b3

        total_a4_list = list1[4]
        total_a4 = total_a4_list[0]
        total_a4

        total_a4_list = list1[4]
        total_b4 = total_a4_list[1]
        total_b4

        total = sum(count[1] for count in [size for size in df_weixiu['不良原因'].value_counts().items()])
        total

        d0 = round(total_b0 / total, 2) * 100
        d0

        d1 = round(total_b1 / total, 2) * 100
        d1

        d2 = round(total_b2 / total, 2) * 100
        d2

        d3 = round(total_b3 / total, 3) * 100
        d3

        d4 = round(total_b4 / total, 2) * 100
        d4

        c0 = '{:.1%}'.format(total_b0 / total)
        c0

        c1 = '{:.1%}'.format(total_b1 / total)
        c1

        c2 = '{:.1%}'.format(total_b2 / total)
        c2

        c3 = '{:.1%}'.format(total_b3 / total)
        c3

        c4 = '{:.1%}'.format(total_b4 / total)
        c4


        fn = """
            function(params) {
                if(params.name == '其他')
                    return '\\n\\n\\n' + params.name + ' : ' + params.value + '%';
                return params.name + ' : ' + params.value + '%';
            }
            """

        def new_label_opts():
            return opts.LabelOpts(formatter=JsCode(fn), position="center")

        pie3 = (
            Pie()
            .add(
                "",
                [list(z) for z in zip([total_a0, ""], [d0, ])],
                center=["20%", "30%"],
                radius=[60, 80],
                label_opts=new_label_opts(),
            )
            .add(
                "",
                [list(z) for z in zip([total_a1, ""], [d1, ])],
                center=["60%", "30%"],
                radius=[60, 80],
                label_opts=new_label_opts(),
            )
            .add(
                "",
                [list(z) for z in zip([total_a2, ""], [d2, ])],
                center=["20%", "70%"],
                radius=[60, 80],
                label_opts=new_label_opts(),
            )
            .add(
                "",
                [list(z) for z in zip([total_a3, ""], [d3, ])],
                center=["60%", "70%"],
                radius=[60, 80],
                label_opts=new_label_opts(),
            )
            .add(
                "",
                [list(z) for z in zip([total_a4, ""], [d4, ])],
                center=["40%", "50%"],
                radius=[60, 80],
                label_opts=new_label_opts(),
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="TOP5多比饼图"),
                legend_opts=opts.LegendOpts(
                    type_="scroll", pos_top="20%", pos_left="80%", orient="vertical"
                ),
            )
        )
        pie3.render_notebook()

        df_RAUSE = pd.read_excel(r'D:\桌面\anli\kpishuju.xls')

        [i for i in df_RAUSE['抽检良率'].value_counts().items()]

        a_list = [size for size in df_RAUSE['抽检良率'].items()]
        total_a_list = a_list[0]
        total_a = total_a_list[1]
        total_a
        data1 = [size for size in df_RAUSE['抽检良率'].value_counts().items()]
        count_list1 = [item[0] for item in data1]
        count_list1

        a = count_list1
        [x * 100 for x in a]
        a1 = [x * 100 for x in a]
        a1

        [size for size in df_RAUSE['工资成本'].value_counts().items()]
        a_list = [size for size in df_RAUSE['工资成本'].items()]
        total_a1_list = a_list[0]
        total_a1 = total_a_list[1]
        total_a1

        data2 = [size for size in df_RAUSE['工资成本'].items()]
        count_list2 = [item[1] for item in data2]
        count_list2

        [size for size in df_RAUSE['通讯上线DPPM'].value_counts().items()]
        a_list = [size for size in df_RAUSE['通讯上线DPPM'].items()]
        total_a2_list = a_list[0]
        total_a2 = total_a_list[1]
        total_a2

        data3 = [size for size in df_RAUSE['通讯上线DPPM'].items()]
        count_list3 = [item[1] for item in data3]
        count_list3

        [size for size in df_RAUSE['PC产品5月早返率(DPPM)'].value_counts().items()]
        a_list = [size for size in df_RAUSE['PC产品5月早返率(DPPM)'].items()]
        total_a4_list = a_list[0]
        total_a4 = total_a_list[1]
        total_a4

        data4 = [size for size in df_RAUSE['PC产品5月早返率(DPPM)'].items()]
        count_list4 = [item[1] for item in data4]
        count_list4

        data5 = [size for size in df_RAUSE['返工工时'].items()]
        count_list5 = [item[1] for item in data5]
        count_list5

        data6 = [size for size in df_RAUSE['直通率'].items()]
        count_list6 = [item[1] for item in data6]
        count_list6

        b6 = count_list6
        [x * 100 for x in b6]
        a6 = [x * 100 for x in b6]
        a6


        x = Faker.choose()
        kpi = Timeline()

        x_data = ["{}月".format(i) for i in range(1, 13)]
        pie4 = (
            Bar()
            .add_xaxis(x_data)
            .add_yaxis(
                "工资成本",
                count_list2,
                yaxis_index=1,
                color="#d14a61",
            )
            .add_yaxis(
                "通讯上线DPPM",
                count_list3,
                yaxis_index=2,
                color="#5793f3",
            )
            .add_yaxis(
                "返工工时",
                count_list5,
                yaxis_index=1,
                color="green",
            )

            .add_yaxis(
                "PC产品5月早返率(DPPM)",
                count_list4,
                yaxis_index=2,
                color="#060bb0",
            )

            .set_global_opts(title_opts=opts.TitleOpts("质量月度KPI".format()))

            .extend_axis(
                yaxis=opts.AxisOpts(
                    name="工资成本",
                    type_="value",
                    min_=0,
                    max_=4000,
                    position="right",
                    offset=50,
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                    ),
                    axislabel_opts=opts.LabelOpts(formatter="{value} RMB"),
                )
            )
            .extend_axis(

                yaxis=opts.AxisOpts(
                    type_="value",
                    name="PC产品5月早返率",
                    min_=0,
                    max_=800,
                    position="left",
                    offset=50,
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#675bba")
                    ),
                    axislabel_opts=opts.LabelOpts(formatter="{value} DPPM"),
                    splitline_opts=opts.SplitLineOpts(
                        is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                    ),
                )
            )
            .extend_axis(

                yaxis=opts.AxisOpts(
                    type_="value",
                    name="返工工时",
                    min_=0,
                    max_=4000,
                    position="left",
                    offset=50,
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#675bba")
                    ),
                    axislabel_opts=opts.LabelOpts(formatter="{value} DPPM"),
                    splitline_opts=opts.SplitLineOpts(
                        is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                    ),
                )
            )
            .extend_axis(
                yaxis=opts.AxisOpts(
                    type_="value",
                    name="抽检良率",
                    min_=0,
                    max_=100,
                    position="left",
                    offset=95,
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#675bba")
                    ),
                    axislabel_opts=opts.LabelOpts(formatter="{value} %"),
                    splitline_opts=opts.SplitLineOpts(
                        is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                    ),
                )
            )

            .extend_axis(

                yaxis=opts.AxisOpts(
                    type_="value",
                    name=" ",
                    min_=0,
                    max_=600,

                    position="right",
                    offset=30,
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#999bb0")
                    ),
                    axislabel_opts=opts.LabelOpts(formatter="{value} %"),
                    splitline_opts=opts.SplitLineOpts(
                        is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                    ),
                )
            )
            .set_global_opts(
                yaxis_opts=opts.AxisOpts(
                    name="通讯上线DPPM",
                    min_=0,
                    max_=550,
                    position="right",
                    offset=68,
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                    ),
                    axislabel_opts=opts.LabelOpts(formatter="{value} DPPM"),
                ),
                title_opts=opts.TitleOpts(title="质量KPI统计图"),
                tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),

            )
        )

        line = (
            Line()
            .add_xaxis(x_data)
            .add_yaxis(
                "抽检良率",
                a1,
                yaxis_index=2,
                color="#675bba",
                label_opts=opts.LabelOpts(is_show=True),
            )

            .add_yaxis(
                "直通率",
                a6,
                yaxis_index=5,
                color="#65B581",
                label_opts=opts.LabelOpts(is_show=True),
            )

        )
        # kpi.add(kpi, "{}月".format(i))
        pie4.overlap(line)
        grid = Grid()
        grid.add(pie4, opts.GridOpts(pos_left="15%", pos_right="15%"), is_control_axis_index=True)
        # grid.render("grid_multi_yaxis.html")
        grid.render_notebook()

        page = Page(layout=Page.DraggablePageLayout)

        page.add(pie1, pie2, pie3, pie4)
        page.render(os.path.join(Path(__file__).resolve().parent.parent.parent.parent) + r'\templates\质量可视化数据.html')
        return render(request, "质量可视化数据.html")

