import json

from django.views import generic

from core.models import SensorReading
from core.tools.fusioncharts import FusionCharts


class BaseIndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(BaseIndexView, self).get_context_data(**kwargs)

        sensor_reading = SensorReading.objects.filter(setting__id=1).values_list(
            'working_duration', 'number_of_telemetry_packets', 'battery_voltage', 'altitude',
            'velocity', 'no2_level_in_ppm', 'co_level_in_ppm', 'h2_level_in_ppm', 'latitude', 'longitude',
            'has_recording_started'
        )[0]
        labels = [field.name for field in SensorReading._meta.fields
                  if field.name not in ['id', 'setting', 'created_at', 'updated_at', 'departure_time']]

        context['dataset'] = json.dumps(sensor_reading)
        context['labels'] = json.dumps(labels)

        return context


class FusionChartView(generic.TemplateView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super(FusionChartView, self).get_context_data(**kwargs)

        chartObj1 = FusionCharts('line', 'ex1', '600', '400', 'chart-1', 'json', """{
          "chart": {
            "caption": "Average Fastball Velocity",
            "yaxisname": "Velocity (in mph)",
            "subcaption": "[2005-2016]",
            "numbersuffix": " mph",
            "rotatelabels": "1",
            "setadaptiveymin": "1",
            "theme": "fusion"
          },
          "data": [
            {
              "label": "2005",
              "value": "89.45"
            },
            {
              "label": "2006",
              "value": "89.87"
            },
            {
              "label": "2007",
              "value": "89.64"
            },
            {
              "label": "2008",
              "value": "90.13"
            },
            {
              "label": "2009",
              "value": "90.67"
            },
            {
              "label": "2010",
              "value": "90.54"
            },
            {
              "label": "2011",
              "value": "90.75"
            },
            {
              "label": "2012",
              "value": "90.8"
            },
            {
              "label": "2013",
              "value": "91.16"
            },
            {
              "label": "2014",
              "value": "91.37"
            },
            {
              "label": "2015",
              "value": "91.66"
            },
            {
              "label": "2016",
              "value": "91.8"
            }
          ]
        }""")

        chartObj2 = FusionCharts('line', 'ex2', '600', '400', 'chart-2', 'json', """{
                  "chart": {
                    "caption": "Average Fastball Velocity",
                    "yaxisname": "Velocity (in mph)",
                    "subcaption": "[2005-2016]",
                    "numbersuffix": " mph",
                    "rotatelabels": "1",
                    "setadaptiveymin": "1",
                    "theme": "gammel"
                  },
                  "data": [
                    {
                      "label": "2005",
                      "value": "89.45"
                    },
                    {
                      "label": "2006",
                      "value": "89.87"
                    },
                    {
                      "label": "2007",
                      "value": "89.64"
                    },
                    {
                      "label": "2008",
                      "value": "90.13"
                    },
                    {
                      "label": "2009",
                      "value": "90.67"
                    },
                    {
                      "label": "2010",
                      "value": "90.54"
                    },
                    {
                      "label": "2011",
                      "value": "90.75"
                    },
                    {
                      "label": "2012",
                      "value": "90.8"
                    },
                    {
                      "label": "2013",
                      "value": "91.16"
                    },
                    {
                      "label": "2014",
                      "value": "91.37"
                    },
                    {
                      "label": "2015",
                      "value": "91.66"
                    },
                    {
                      "label": "2016",
                      "value": "91.8"
                    }
                  ]
                }""")

        chartObj3 = FusionCharts('line', 'ex3', '600', '400', 'chart-3', 'json', """{
                  "chart": {
                    "caption": "Average Fastball Velocity",
                    "yaxisname": "Velocity (in mph)",
                    "subcaption": "[2005-2016]",
                    "numbersuffix": " mph",
                    "rotatelabels": "1",
                    "setadaptiveymin": "1",
                    "theme": "fusion"
                  },
                  "data": [
                    {
                      "label": "2005",
                      "value": "89.45"
                    },
                    {
                      "label": "2006",
                      "value": "89.87"
                    },
                    {
                      "label": "2007",
                      "value": "89.64"
                    },
                    {
                      "label": "2008",
                      "value": "90.13"
                    },
                    {
                      "label": "2009",
                      "value": "90.67"
                    },
                    {
                      "label": "2010",
                      "value": "90.54"
                    },
                    {
                      "label": "2011",
                      "value": "90.75"
                    },
                    {
                      "label": "2012",
                      "value": "90.8"
                    },
                    {
                      "label": "2013",
                      "value": "91.16"
                    },
                    {
                      "label": "2014",
                      "value": "91.37"
                    },
                    {
                      "label": "2015",
                      "value": "91.66"
                    },
                    {
                      "label": "2016",
                      "value": "91.8"
                    }
                  ]
                }""")

        context['output1'] = chartObj1.render()
        context['output2'] = chartObj2.render()
        context['output3'] = chartObj3.render()

        return context


class RealTimeChartView(generic.TemplateView):
    template_name = 'real_time.html'

    def get_context_data(self, **kwargs):
        context = super(RealTimeChartView, self).get_context_data(**kwargs)

        angularGauge = FusionCharts("angulargauge", "ex1", "450", "270", "chart-1", "json",
                                    # The data is passed as a string in the `dataSource` as parameter.
                                    """{  
                "chart": { 
                    "caption": "Customer Satisfaction Score", 
                    "subcaption": "Los Angeles Topanga", 
                    "plotToolText": "Current Score: $value", 
                    "theme": "fint", 
                    "chartBottomMargin": "50", 
                    "showValue": "1" 
                }, 
                "colorRange": { 
                    "color": [{ 
                        "minValue": "0", 
                        "maxValue": "45", 
                        "code": "#e44a00"
                    }, { 
                        "minValue": "45", 
                        "maxValue": "75", 
                        "code": "#f8bd19" 
                    }, { 
                        "minValue": "75", 
                        "maxValue": "100", 
                        "code": "#6baa01" 
                    }] 
                }, 
                "dials": { 
                    "dial": [{ 
                        "value": "70", 
                        "id": "dial1" 
                    }] 
                }
            }""")

        context['output'] = angularGauge.render()
        context['chartTitle'] = 'Update data at runtime'

        return context
