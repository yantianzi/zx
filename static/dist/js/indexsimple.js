// 立即执行函数，防止变量污染 (function() {})();

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
                data: ["总体延误", "排队长度", "周期内流量", "绿灯利用率", "绿灯利用率", "停驶车辆数","平均通过车辆数"],
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

