// 立即执行函数，防止变量污染 (function() {})();

// 柱状图模块---相位顺序示意图(echart)
(function () {
  // 1.实例化对象
  var myChart = echarts.init(document.querySelector(".bar .chart"));
  // 2.指定配置项和数据
  var option = {
    color: ['#60cda0', '#ed8884', '#ff9f7f', '#0096ff', '#9fe6b8', '#32c5e9', '#1d9dff'],
    // 提示框组件
    tooltip: {
      trigger: 'axis',
      axisPointer: {
          // Use axis to trigger tooltip
          type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
        }
    },
    legend: {
      textStyle: {
        color: "rgba(219,225,255,1)",
      }
    },
    // 修改图表位置大小
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    // x轴相关配置
     xAxis: {
       type: 'value',
       data: [0, 30, 60, 90, 120, 150],
       lineStyle: {
            color: "rgba(219,225,255,1)",
            width: 0,
            type: "solid"
        },
        axisTick: {
            show: false,
        },
        axisLabel: {//x轴文字的配置
            show: true,
            textStyle: {
                color: "rgba(219,225,255,1)",
            }
        },
        splitLine: {//分割线配置
            show:false,
            lineStyle: {
                color: "rgba(219,225,255,1)",
         }
        }
      },
    // y轴相关配置
    yAxis: {
      type: 'category',
      data: ['东西直行', '东西左转', '南北直行', '南北左转'],
      axisTick: {
        show: false,
      },
      axisLabel: {//x轴文字的配置
          show: true,
          textStyle: {
              color: "rgba(219,225,255,1)",
          }
      },
      splitLine: {//分割线配置
          show:false,
          lineStyle: {
              color: "rgba(219,225,255,1)",
       }
      }
    },
    // 系列列表配置
    series: [
    {
      name: 'Direct',
      type: 'bar',
      stack: 'total',
      label: {
        show: true
      },
      emphasis: {
        focus: 'series'
      },
      data: [55, 60, 90, 123]
    },
    {
      name: 'Mail Ad',
      type: 'bar',
      stack: 'total',
      label: {
        show: true
      },
      emphasis: {
        focus: 'series'
      },
      data: [5, 28, 32, 20]
    },
    {
      name: 'Affiliate Ad',
      type: 'bar',
      stack: 'total',
      label: {
        show: true
      },
      emphasis: {
        focus: 'series'
      },
      data: [90, 2, 5, 8]
    },
    {
      name: 'Affiliate',
      type: 'bar',
      stack: 'total',
      label: {
        show: true
      },
      emphasis: {
        focus: 'series'
      },
      data: [0, 60, 23, 0]
    }
    ]
  };
  // 3.把配置项给实例对象
  myChart.setOption(option);

  // 4.让图表随屏幕自适应
  window.addEventListener('resize', function () {
    myChart.resize();
  })
})();

// 柱状图模块---整体延误对比图
(function () {
    var myChart1 = echarts.init(document.querySelector(".chart1"));
    // 2.指定配置项和数据
    myChart1.hideLoading();
    var option1 = {
        color: ['#60cda0', '#0096ff'],
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow',
                label: {
                    show: true
                }
            }
        },
        toolbox: {
            show: true,
            feature: {
                mark: {show: true},
                dataView: {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar']},
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        calculable: true,
        legend: {
            data: ['Growth', '优化前', '优化后'],
            itemGap: 5,
            textStyle: {
            color: "rgba(219,225,255,1)",
          }
        },
        grid: {
            top: '10%',
            bottom: '10%',
            left: '1%',
            right: '10%',
            containLabel: true
        },
        xAxis: [
            {
                type: 'category',
                data: ["总体延误", "排队长度", "周期内流量", "绿灯利用率", "信号合理性", "停驶车辆数","平均通过车辆数"],
                lineStyle: {
                    color: "rgba(219,225,255,1)",
                    width: 0,
                    type: "solid"
                },
                axisTick: {
                    show: false,
                },
                axisLabel: {//x轴文字的配置
                    show: true,
                    textStyle: {
                        color: "rgba(219,225,255,1)",
                    }
                },
                splitLine: {//分割线配置
                    show: false,
                    lineStyle: {
                        color: "rgba(219,225,255,1)",
                    }
                }
            }
        ],
        yAxis: [
            {
                type: 'value',
                axisTick: {
                    show: false,
                  },

                axisLabel: {
                    show: true,
                    textStyle: {
                        color: "rgba(219,225,255,1)",
                    },
                    formatter: function (a) {
                        a = +a;
                        return isFinite(a) ? echarts.format.addCommas(+a) : '';
                    }
                },
                splitLine: {//分割线配置
                      show:false,
                      lineStyle: {
                          color: "rgba(219,225,255,1)",
                   }
                }
            }
        ],
        dataZoom: [
            {
                show: true,
                start: 94,
                end: 100
            },
            {
                type: 'inside',
                start: 94,
                end: 100
            },
            {
                show: true,
                yAxisIndex: 0,
                filterMode: 'empty',
                width: 30,
                height: '80%',
                showDataShadow: false,
                left: '93%'
            }
        ],
        series: [
            {
                name: '优化前',
                type: 'bar',
                data: [],
            },
            {
                name: '优化后',
                type: 'bar',
                data: [],
            }
        ]
    };
    myChart1.setOption(option1);

    // 4.让图表随屏幕自适应
  window.addEventListener('resize', function () {
    myChart1.resize();
  })
})();

// 柱状图模块---干线延误对比图
(function () {
    var myChart2 = echarts.init(document.querySelector(".chart2"));
    // 2.指定配置项和数据
    myChart2.hideLoading();
    var option2 = {
        color: ['#60cda0', '#0096ff'],
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow',
                label: {
                    show: true
                }
            }
        },
        toolbox: {
            show: true,
            feature: {
                mark: {show: true},
                dataView: {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar']},
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        calculable: true,
        legend: {
            data: ['Growth', '优化前', '优化后'],
            itemGap: 5,
            textStyle: {
            color: "rgba(219,225,255,1)",
          }
        },
        grid: {
            top: '10%',
            bottom: '10%',
            left: '1%',
            right: '10%',
            containLabel: true
        },
        xAxis: [
            {
                type: 'category',
                data: ["总体延误", "排队长度", "周期内流量", "绿灯利用率", "信号合理性", "停驶车辆数","平均通过车辆数"],
                lineStyle: {
                    color: "rgba(219,225,255,1)",
                    width: 0,
                    type: "solid"
                },
                axisTick: {
                    show: false,
                },
                axisLabel: {//x轴文字的配置
                    show: true,
                    textStyle: {
                        color: "rgba(219,225,255,1)",
                    }
                },
                splitLine: {//分割线配置
                    show: false,
                    lineStyle: {
                        color: "rgba(219,225,255,1)",
                    }
                }
            }
        ],
        yAxis: [
            {
                type: 'value',
                axisTick: {
                    show: false,
                  },

                axisLabel: {
                    show: true,
                    textStyle: {
                        color: "rgba(219,225,255,1)",
                    },
                    formatter: function (a) {
                        a = +a;
                        return isFinite(a) ? echarts.format.addCommas(+a) : '';
                    }
                },
                splitLine: {//分割线配置
                      show:false,
                      lineStyle: {
                          color: "rgba(219,225,255,1)",
                   }
                }
            }
        ],
        dataZoom: [
            {
                show: true,
                start: 94,
                end: 100
            },
            {
                type: 'inside',
                start: 94,
                end: 100
            },
            {
                show: true,
                yAxisIndex: 0,
                filterMode: 'empty',
                width: 30,
                height: '80%',
                showDataShadow: false,
                left: '93%'
            }
        ],
        series: [
            {
                name: '优化前',
                type: 'bar',
                data: [],
            },
            {
                name: '优化后',
                type: 'bar',
                data: [],
            }
        ]
    };
    myChart2.setOption(option2);

    // 4.让图表随屏幕自适应
  window.addEventListener('resize', function () {
    myChart2.resize();
  })

})();

// 柱状图模块---路网延误对比图
(function () {
  // 柱状图模块---干线延误对比图
    var myChart3 = echarts.init(document.querySelector(".chart3"));
    // 2.指定配置项和数据
    myChart3.hideLoading();
    var option3 = {
        color: ['#60cda0', '#0096ff'],
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow',
                label: {
                    show: true
                }
            }
        },
        toolbox: {
            show: true,
            feature: {
                mark: {show: true},
                dataView: {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar']},
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        calculable: true,
        legend: {
            data: ['Growth', '优化前', '优化后'],
            itemGap: 5,
            textStyle: {
            color: "rgba(219,225,255,1)",
          }
        },
        grid: {
            top: '10%',
            bottom: '10%',
            left: '1%',
            right: '10%',
            containLabel: true
        },
        xAxis: [
            {
                type: 'category',
                data: ["总体延误", "排队长度", "周期内流量", "绿灯利用率", "信号合理性", "停驶车辆数","平均通过车辆数"],
                lineStyle: {
                    color: "rgba(219,225,255,1)",
                    width: 0,
                    type: "solid"
                },
                axisTick: {
                    show: false,
                },
                axisLabel: {//x轴文字的配置
                    show: true,
                    textStyle: {
                        color: "rgba(219,225,255,1)",
                    }
                },
                splitLine: {//分割线配置
                    show: false,
                    lineStyle: {
                        color: "rgba(219,225,255,1)",
                    }
                }
            }
        ],
        yAxis: [
            {
                type: 'value',
                axisTick: {
                    show: false,
                  },

                axisLabel: {
                    show: true,
                    textStyle: {
                        color: "rgba(219,225,255,1)",
                    },
                    formatter: function (a) {
                        a = +a;
                        return isFinite(a) ? echarts.format.addCommas(+a) : '';
                    }
                },
                splitLine: {//分割线配置
                      show:false,
                      lineStyle: {
                          color: "rgba(219,225,255,1)",
                   }
                }
            }
        ],
        dataZoom: [
            {
                show: true,
                start: 94,
                end: 100
            },
            {
                type: 'inside',
                start: 94,
                end: 100
            },
            {
                show: true,
                yAxisIndex: 0,
                filterMode: 'empty',
                width: 30,
                height: '80%',
                showDataShadow: false,
                left: '93%'
            }
        ],
        series: [
            {
                name: '优化前',
                type: 'bar',
                data: [],
            },
            {
                name: '优化后',
                type: 'bar',
                data: [],
            }
        ]
    };
    myChart3.setOption(option3);

    // 4.让图表随屏幕自适应
  window.addEventListener('resize', function () {
    myChart3.resize();
  })

})();