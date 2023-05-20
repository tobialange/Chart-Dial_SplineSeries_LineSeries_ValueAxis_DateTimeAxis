from PySide6.QtWidgets import QWidget, QGridLayout, QDial
from PySide6.QtCharts import QChart, QLineSeries, QChartView, QSplineSeries, QValueAxis, QDateTimeAxis
from PySide6.QtCore import Qt, QDateTime
from PySide6.QtGui import QColor


class TempChart(QWidget):
    def __init__(self, parent):
        super(TempChart, self).__init__(parent)

        self.axis_time = QDateTimeAxis()
        self.axis_time.setTitleText("Zeitachse")
        #self.axis_time.setTickCount(6)
        #self.axis_time.setGridLineColor(QColor("red"))
        self.axis_time.setFormat("mm:ss")
        self.axis_time.setRange(QDateTime.currentDateTime(), QDateTime.currentDateTime().addSecs(5*60))

        self.axis_percent = QValueAxis()
        self.axis_percent.setTitleText("Prozent")
        self.axis_percent.setRange(0, 100)

        self.axis_x = QValueAxis()
        self.axis_x.setTitleText("x-Achse")
        self.axis_x.setRange(0, 5)

        self.axis_y = QValueAxis()
        self.axis_y.setTitleText("y-Achse")
        self.axis_y.setRange(0, 20)

        self.chart = QChart()
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.chart.addAxis(self.axis_time, Qt.AlignTop)
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.chart.addAxis(self.axis_percent, Qt.AlignRight)

        self.chart_view = QChartView()
        self.chart_view.setChart(self.chart)

        self.my_layout = QGridLayout()
        self.my_layout.addWidget(self.chart_view, 0, 1)


        self.dial1 = QDial(self)
        self.dial1.valueChanged.connect(self.newdial1value)
        self.my_layout.addWidget(self.dial1, 0, 0)

        self.dial2 = QDial(self)
        self.dial2.valueChanged.connect(self.newdial2value)
        self.my_layout.addWidget(self.dial2, 0, 2)

        self.setLayout(self.my_layout)

        #self.series = QSplineSeries()
        #self.chart.addSeries(self.series)
        #self.series.setName("f(x) = x^2")
        #self.series.attachAxis(self.axis_x)
        #self.series.attachAxis(self.axis_y)

        self.series = QLineSeries()
        self.chart.addSeries(self.series)
        self.series.attachAxis(self.axis_x)
        self.series.attachAxis(self.axis_y)
        self.series.setName("Prozent über Zeit")




    def newdial1value(self, dial1value: int):
        #self.dial1value = dial1value
        self.series.append(dial1value, self.dial2.value())


    def newdial2value(self, dial2value: int):
        #self.dial2value = dial2value
        self.series.append(self.dial1.value(), dial2value)