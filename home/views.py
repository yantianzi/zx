import json
from operator import mod

import backbone as backbone
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.urls import reverse
from home.models import Effect,Configuration,EffectOptimized,SummaryOptimized,Summary,BackboneOptimized,Backbone


def home_index(request):
    effectlist = Effect.objects.all()
    context = {'effectlist': effectlist}
    return render(request, 'test.html', context)

def home_demo_index(request):
    effectlist = Effect.objects.all()
    context = {'effectlist': effectlist}
    return render(request, 'demo-test.html', context)

def home_simple_index(request):
    """简易版本"""
    effectlist = Effect.objects.all()
    context = {'effectlist': effectlist}
    return render(request, 'simple.html', context)


def home_query(request):
    """带有路口信息请求test.html"""
    effectlist = Effect.objects.all()
    context = {'effectlist': effectlist}
    return render(request, "test.html", context)

def home_doquery(request):
    # # 执行判断是否选择路口
    print(dict(request.POST))
    # if request.POST['road_id'] == 0:
    #     # 请选择所在的路口名称！
    #     return redirect(reverse("home_query") + "?errinfo=1")

    road = Effect.objects.get(road_id=request.POST['road_id'])
    backbone_id = mod(int(request.POST['road_id']), 3) + 1
    print(backbone_id)
    configuration_id = 4 * (int(request.POST['road_id'][0]) - 1) + int(request.POST['configuration_id'][0])
    print(configuration_id)
    configuration = Configuration.objects.get(effect_id=int(request.POST['road_id'][0]),configuration_id=configuration_id)
    backbone = Backbone.objects.get(backbone_id=backbone_id)
    backbone_optimized = BackboneOptimized.objects.get(backbone_id=backbone_id)
    summary = Summary.objects.get(summary_id=1)
    summary_optimized = SummaryOptimized.objects.get(summary_id=1)
    print(backbone)
    print(summary)
    print(summary_optimized)
    print(configuration)
    context = {
        "road": road,
        "configuration": configuration,
        "backbone": backbone,
        "backboneOptimized": backbone_optimized,
        "summary": summary,
        "summaryOptimized": summary_optimized,
    }
    return render(request,'test.html', context)


@csrf_exempt
def home_ajax(request):
    """从前端ajax接收数据，处理之后再传递到前端生成数据可视化图"""
    print(dict(request.POST))
    if request.POST['road_id'] == 0:
    # 请选择所在的路口名称！
        return redirect(reverse("home_query") + "?errinfo=1")

    data_list = dict(request.POST)  # 转为字典格式
    # 在数据库中查找相应的路口
    road_id = int(data_list['road_id'][0])
    road = Effect.objects.get(road_id=road_id).toDict()
    road_optimized = EffectOptimized.objects.get(road_id=road_id).toDict()
    backbone_id = mod(int(road_id),3) + 1
    print('backbone_id:', backbone_id)
    configuration_id = (road_id - 1)*4 + int(data_list['configuration_id'][0])
    print('configuration_id:',configuration_id)
    configuration = Configuration.objects.get(configuration_id=configuration_id).toDict()
    backbone = Backbone.objects.get(backbone_id=backbone_id).toDict()
    backbone_optimized = BackboneOptimized.objects.get(backbone_id=backbone_id).toDict()
    summary = Summary.objects.get(summary_id=1).toDict()
    summary_optimized = SummaryOptimized.objects.get(summary_id=1).toDict()
    # echarts图里的data数据
    backbone_data = [backbone['avg_delay'],backbone['queue_length'],backbone['flow_volume'],backbone['service_level'],backbone['signal_rationality'],backbone['paused_vehicle_num'],backbone['avg_passed_vehicle_num'],backbone['greenrate']]
    backbone_optimized_data = [backbone_optimized['avg_delay'], backbone_optimized['service_level'], backbone_optimized['queue_length'], backbone_optimized['flow_volume'],backbone_optimized['signal_rationality'], backbone_optimized['paused_vehicle_num'], backbone_optimized['avg_passed_vehicle_num'],backbone_optimized['greenrate']]
    effect_data = [road['avg_delay'],road['queue_length'],road['flow_volume'],road['service_level'],road['signal_rationality'],road['paused_vehicle_num'],road['avg_passed_vehicle_num'],road['greenrate']]
    effect_optimized_data = [road_optimized['avg_delay'], road_optimized['queue_length'], road_optimized['service_level'], road_optimized['flow_volume'], road_optimized['signal_rationality'],road_optimized['paused_vehicle_num'], road_optimized['avg_passed_vehicle_num'], road_optimized['greenrate']]
    result = {
        "status": True,
        "data": {
            "road":road,
            "road_optimized":road_optimized,
            "configuration":configuration,
            "backbone":backbone,
            "backboneOptimized": backbone_optimized,
            "summary":summary,
            "summaryOptimized":summary_optimized,
            "backbone_data":backbone_data,
            "backbone_optimized_data":backbone_optimized_data,
            "effect_data":effect_data,
            "effect_optimized_data":effect_optimized_data,
        }
    }
    # print(effect_data)
    # print(effect_optimized_data)
    # print(backbone_data)
    # print(backbone_optimized_data)
    return JsonResponse(result)


