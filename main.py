

import hjio
import setting
import historyLib
import hjdraw
import graphlib

import time
import sys
import threading



def main():

    # 日志初始化 必要
    hjio.init(setting.logpath)
    hjio.writelog("PROCESS START")
    # 运行
    ModeHistoryDataAna()

    hjio.clearbuf('PROCESS END')

    return



def ModeHistoryDataAna():

    #历史数据处理
    # historyLib.init(setting.history_data_path)

    # 生成图表
    # 按周期分表,按市场为坐标统计的数据量汇总柱形图
    # graphlib.drawBarAll(setting.graph_bar_path)

    # 绘制站点数据曲线图
    # graphlib.drawAllMarketPlot(setting.graph_plot_path)

    # 绘制市场周期二维表
    # graphlib.drawAllMarketTable2(setting.table_path)

    #图表工具
    hjdraw.init()
    return

if __name__ == '__main__':
    main()


