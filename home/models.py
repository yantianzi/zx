from django.db import models

# Create your models here.
class Backbone(models.Model):
    backbone_id = models.AutoField(primary_key=True, verbose_name="干线ID")
    level = models.CharField(max_length=40,verbose_name="方案层级")  # 方案层级
    avg_delay = models.FloatField(default=0,verbose_name="总体延误",null=True)  # 总体延误
    queue_length = models.FloatField(default=0,verbose_name="排队长度",null=True)  # 排队长度
    flow_volume = models.FloatField(default=0, verbose_name="周期内流量", null=True)  # 周期内流量
    service_level = models.CharField(max_length=40,verbose_name="通行服务等级")  # 通行服务等级
    signal_rationality = models.FloatField(default=0,verbose_name="信号合理性",null=True)  # 信号合理性
    paused_vehicle_num = models.FloatField(default=0,verbose_name="停驶车辆数",null=True)  # 停驶车辆数
    avg_passed_vehicle_num = models.FloatField(default=0,verbose_name="平均通过车辆数",null=True)  # 平均通过车辆数
    greenrate = models.FloatField(default=0,verbose_name="绿灯利用率",null=True)  # 排队长度

    class Meta:
        db_table = "backbone"
    def toDict(self):
        return {'backbone_id': self.backbone_id, 'level': self.level, 'avg_delay': self.avg_delay,
                'queue_length': self.queue_length, 'flow_volume': self.flow_volume, 'service_level': self.service_level,
                'signal_rationality': self.signal_rationality, 'paused_vehicle_num': self.paused_vehicle_num,
                'avg_passed_vehicle_num': self.avg_passed_vehicle_num, 'greenrate': self.greenrate,

                }

class BackboneOptimized(models.Model):
    backbone_id = models.AutoField(primary_key=True, verbose_name="优化后干线ID")
    level = models.CharField(max_length=40,verbose_name="方案层级")  # 方案层级
    avg_delay = models.FloatField(default=0,verbose_name="总体延误",null=True)  # 总体延误
    queue_length = models.FloatField(default=0,verbose_name="排队长度",null=True)  # 排队长度
    flow_volume = models.FloatField(default=0, verbose_name="周期内流量", null=True)  # 周期内流量
    service_level = models.CharField(max_length=40,verbose_name="通行服务等级")  # 通行服务等级
    signal_rationality = models.FloatField(default=0,verbose_name="信号合理性",null=True)  # 信号合理性
    paused_vehicle_num = models.FloatField(default=0,verbose_name="停驶车辆数",null=True)  # 停驶车辆数
    avg_passed_vehicle_num = models.FloatField(default=0,verbose_name="平均通过车辆数",null=True)  # 平均通过车辆数
    greenrate = models.FloatField(default=0,verbose_name="绿灯利用率",null=True)  # 排队长度

    class Meta:
        db_table = "backboneoptimized"
    def toDict(self):
        return {'backbone_id': self.backbone_id, 'level': self.level, 'avg_delay': self.avg_delay,
                'queue_length': self.queue_length, 'flow_volume': self.flow_volume, 'service_level': self.service_level,
                'signal_rationality': self.signal_rationality, 'paused_vehicle_num': self.paused_vehicle_num,
                'avg_passed_vehicle_num': self.avg_passed_vehicle_num, 'greenrate': self.greenrate,

                }

class Summary(models.Model):
    summary_id = models.AutoField(primary_key=True, verbose_name="总体ID")
    level = models.CharField(max_length=40, verbose_name="方案层级")  # 方案层级
    avg_delay = models.FloatField(default=0, verbose_name="总体延误", null=True)  # 总体延误
    queue_length = models.FloatField(default=0, verbose_name="排队长度", null=True)  # 排队长度
    flow_volume = models.FloatField(default=0, verbose_name="周期内流量", null=True)  # 周期内流量
    service_level = models.CharField(max_length=40, verbose_name="通行服务等级")  # 通行服务等级
    signal_rationality = models.FloatField(default=0, verbose_name="信号合理性", null=True)  # 信号合理性
    paused_vehicle_num = models.FloatField(default=0, verbose_name="停驶车辆数", null=True)  # 停驶车辆数
    avg_passed_vehicle_num = models.FloatField(default=0, verbose_name="平均通过车辆数", null=True)  # 平均通过车辆数
    greenrate = models.FloatField(default=0, verbose_name="绿灯利用率", null=True)  # 排队长度
    class Meta:
        db_table = "summary"

    def toDict(self):
        return {'summary_id': self.summary_id, 'level': self.level, 'avg_delay': self.avg_delay,
                'queue_length': self.queue_length, 'flow_volume': self.flow_volume, 'service_level': self.service_level,
                'signal_rationality': self.signal_rationality, 'paused_vehicle_num': self.paused_vehicle_num,
                'avg_passed_vehicle_num': self.avg_passed_vehicle_num, 'greenrate': self.greenrate,

                }

class SummaryOptimized(models.Model):
    summary_id = models.AutoField(primary_key=True, verbose_name="优化后总体ID")
    level = models.CharField(max_length=40, verbose_name="方案层级")  # 方案层级
    avg_delay = models.FloatField(default=0, verbose_name="总体延误", null=True)  # 总体延误
    queue_length = models.FloatField(default=0, verbose_name="排队长度", null=True)  # 排队长度
    flow_volume = models.FloatField(default=0, verbose_name="周期内流量", null=True)  # 周期内流量
    service_level = models.CharField(max_length=40, verbose_name="通行服务等级")  # 通行服务等级
    signal_rationality = models.FloatField(default=0, verbose_name="信号合理性", null=True)  # 信号合理性
    paused_vehicle_num = models.FloatField(default=0, verbose_name="停驶车辆数", null=True)  # 停驶车辆数
    avg_passed_vehicle_num = models.FloatField(default=0, verbose_name="平均通过车辆数", null=True)  # 平均通过车辆数
    greenrate = models.FloatField(default=0, verbose_name="绿灯利用率", null=True)  # 排队长度
    class Meta:
        db_table = "summaryoptimized"
    def toDict(self):
        return {'summary_id':self.summary_id,'level':self.level,'avg_delay':self.avg_delay,
                'queue_length':self.queue_length,'flow_volume':self.flow_volume,'service_level':self.service_level,
                'signal_rationality':self.signal_rationality,'paused_vehicle_num':self.paused_vehicle_num,
                'avg_passed_vehicle_num':self.avg_passed_vehicle_num,'greenrate':self.greenrate,

        }

class Effect(models.Model):
    road_id = models.AutoField(primary_key=True, verbose_name="路口ID")
    road_name = models.CharField(max_length=40, verbose_name="路口名称", null=True)  # 路口名称
    level = models.CharField(max_length=40, verbose_name="方案层级")  # 方案层级
    avg_delay = models.FloatField(default=0, verbose_name="总体延误", null=True)  # 总体延误
    queue_length = models.FloatField(default=0, verbose_name="排队长度", null=True)  # 排队长度
    flow_volume = models.FloatField(default=0, verbose_name="周期内流量", null=True)  # 周期内流量
    service_level = models.CharField(max_length=40, verbose_name="通行服务等级")  # 通行服务等级
    signal_rationality = models.FloatField(default=0, verbose_name="信号合理性", null=True)  # 信号合理性
    paused_vehicle_num = models.FloatField(default=0, verbose_name="停驶车辆数", null=True)  # 停驶车辆数
    avg_passed_vehicle_num = models.FloatField(default=0, verbose_name="平均通过车辆数", null=True)  # 平均通过车辆数
    greenrate = models.FloatField(default=0, verbose_name="绿灯利用率", null=True)  # 绿灯利用率
    # 为路口指定所属的干线：外键,级联删除       一对多
    backbone = models.ForeignKey(to=Backbone, on_delete=models.CASCADE,default=1)
    jingdu = models.FloatField(default=0, verbose_name="经度", null=True)  # 经度
    weidu = models.FloatField(default=0, verbose_name="纬度", null=True)  # 纬度

    class Meta:
        db_table = "effect"
    def toDict(self):
        return {'road_id':self.road_id,'road_name':self.road_name,'level':self.level,'avg_delay':self.avg_delay,
                'queue_length':self.queue_length,'flow_volume':self.flow_volume,'service_level':self.service_level,
                'signal_rationality':self.signal_rationality,'paused_vehicle_num':self.paused_vehicle_num,
                'avg_passed_vehicle_num':self.avg_passed_vehicle_num,'greenrate':self.greenrate,
                'jingdu':self.jingdu,'weidu':self.weidu,
        }


class EffectOptimized(models.Model):
    road_id = models.AutoField(primary_key=True, verbose_name="优化后路口ID")
    road_name = models.CharField(max_length=40, verbose_name="优化后路口名称", null=True)  # 优化后路口名称
    level = models.CharField(max_length=40, verbose_name="方案层级")  # 方案层级
    avg_delay = models.FloatField(default=0, verbose_name="总体延误", null=True)  # 总体延误
    queue_length = models.FloatField(default=0, verbose_name="排队长度", null=True)  # 排队长度
    flow_volume = models.FloatField(default=0, verbose_name="周期内流量", null=True)  # 周期内流量
    service_level = models.CharField(max_length=40, verbose_name="通行服务等级")  # 通行服务等级
    signal_rationality = models.FloatField(default=0, verbose_name="信号合理性", null=True)  # 信号合理性
    paused_vehicle_num = models.FloatField(default=0, verbose_name="停驶车辆数", null=True)  # 停驶车辆数
    avg_passed_vehicle_num = models.FloatField(default=0, verbose_name="平均通过车辆数", null=True)  # 平均通过车辆数
    greenrate = models.FloatField(default=0, verbose_name="绿灯利用率", null=True)  # 排队长度
    # 为路口指定所属的干线：外键,级联删除       一对多
    backbone = models.ForeignKey(to=BackboneOptimized, on_delete=models.CASCADE, default=1)
    class Meta:
        db_table = "effectoptimized"
    def toDict(self):
        return {'road_id':self.road_id,'road_name':self.road_name,'level':self.level,'avg_delay':self.avg_delay,
                'queue_length':self.queue_length,'flow_volume':self.flow_volume,'service_level':self.service_level,
                'signal_rationality':self.signal_rationality,'paused_vehicle_num':self.paused_vehicle_num,
                'avg_passed_vehicle_num':self.avg_passed_vehicle_num,'greenrate':self.greenrate,

        }

class Configuration(models.Model):
    configuration_id = models.AutoField(primary_key=True, verbose_name="相位ID")
    level = models.CharField(max_length=40, verbose_name="方案层级")  # 方案层级
    period = models.SmallIntegerField(default=0,verbose_name="周期",null=True)  # 周期
    green_st = models.FloatField(default=0, verbose_name="开始时间", null=True)  # 开始时间
    green_end = models.FloatField(default=0, verbose_name="结束时间", null=True)  # 结束时间
    greenrate = models.FloatField(default=0, verbose_name="绿信比", null=True)  # 绿信比
    # 为相位指定所属的路口：外键,级联删除       一对多
    effect = models.ForeignKey(to=Effect, on_delete=models.CASCADE, default=1)
    # 为相位指定所属的路口：外键,级联删除       一对多
    effect_optimized = models.ForeignKey(to=EffectOptimized, on_delete=models.CASCADE, default=1)
    class Meta:
        db_table = "configuration"
    def toDict(self):
        return {'configuration_id':self.configuration_id,'level':self.level,'period':self.period,
            'green_st':self.green_st,'green_end':self.green_end,'greenrate':self.greenrate,
        }