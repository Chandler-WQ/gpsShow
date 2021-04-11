#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

import folium
import xlrd


# m = folium.Map(location=[45.5236, -122.6750])
# m.save("index.html")
# 将一个点划线
def draw_gps(locations, file_name):
    """
    绘制gps轨迹图
    :param locations: list, 需要绘制轨迹的经纬度信息，格式为[[lat1, lon1], [lat2, lon2], ...]
    :param output_path: str, 轨迹图保存路径
    :param file_name: str, 轨迹图保存文件名
    :return: None
    """
    m = folium.Map(locations[0], zoom_start=15, attr='default')  # 中心区域的确定

    folium.PolyLine(  # polyline方法为将坐标用线段形式连接起来
        locations,  # 将坐标点连接起来
        weight=3,  # 线的大小为3
        color='orange',  # 线的颜色为橙色
        opacity=0.8  # 线的透明度
    ).add_to(m)  # 将这条线添加到刚才的区域m内

    # 起始点，结束点
    folium.Marker(locations[0], popup='<b>Starting Point</b>').add_to(m)
    folium.Marker(locations[-1], popup='<b>End Point</b>').add_to(m)

    m.save(file_name)  # 将结果以HTML形式保存到指定路径


def draw_point(map, point, name):
    folium.Marker(
        location=point,
        popup=name,
        icon=folium.Icon(color='green')
    ).add_to(map)
    return


def draw_gps_point(locations, file_name):
    m = folium.Map(locations[0], zoom_start=35, attr='default')  # 中心区域的确定
    for i in range(len(locations)):
        draw_point(m, locations[i], str(i))

    folium.PolyLine(  # polyline方法为将坐标用线段形式连接起来
        locations,  # 将坐标点连接起来
        weight=3,  # 线的大小为3
        color='orange',  # 线的颜色为橙色
        opacity=0.8  # 线的透明度
    ).add_to(m)  # 将这条线添加到刚才的区域m内

    # 起始点，结束点
    folium.Marker(locations[0], popup='<b>Starting Point</b>').add_to(m)
    folium.Marker(locations[-1], popup='<b>End Point</b>').add_to(m)
    m.save(file_name)
    return


def get_excel(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]  # 通过索引顺序获取
    longitudes = table.col_values(0)
    latitudes = table.col_values(1)
    # py的这个特性也是有点神奇
    locations = [[0] * 2 for _ in range(len(longitudes) - 1)]

    for i in range(len(longitudes)):
        if i == 0:
            continue
        locations[i - 1][0] = float(latitudes[i])
        locations[i - 1][1] = float(longitudes[i])
    return locations


locations = get_excel("./GPS1.xls")
draw_gps_point(locations, "gps1.html")


locations = get_excel("./GPS2.xls")
draw_gps_point(locations, "gps2.html")

locations = get_excel("./CleanGPS1.xls")
draw_gps_point(locations, "cleangps1.html")

locations = get_excel("./CleanGPS2.xls")
draw_gps_point(locations, "cleangps2.html")
