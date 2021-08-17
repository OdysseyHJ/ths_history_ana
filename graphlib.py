import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Microsoft YaHei']

import historyLib
import hjio


def drawBarGraph(title, datatype='day', fieldtype='hostcount', savPath=''):
    X1, Y1 = historyLib.siMarketDict.getDatatypeFieldList(datatype, fieldtype)
    taillist1 = historyLib.siMarketDict.getDatatypeFieldList(datatype, historyLib.STAT_KEY_HOST_CNT)[1]
    X2, Y2 = historyLib.siMarketDict.getShszDatafield(datatype, fieldtype)
    taillist2 = historyLib.siMarketDict.getShszDatafield(datatype, historyLib.STAT_KEY_HOST_CNT)[1]
    X1 = historyLib.marketnameChnese(X1)
    X = X2 + X1[2:]
    Y = Y2 + Y1[2:]
    taillist = taillist2 + taillist1[2:]
    width=1
    xpos = np.arange(0, len(X)*1.5, 1.5)
    if len(X) == 0:
        print(datatype)
    fig, ax = plt.subplots(figsize=(10, 8))
    bars1 = plt.barh(xpos, Y, align='center', height=width, alpha=0.9, label='Category A')

    ax.set_yticks(xpos)  # 确定每个记号的位置
    ax.set_yticklabels(X)  # 确定每个记号的内容

    plt.title(title)

    autolabelHT(bars1, ax, taillist)

    if len(savPath) == 0:
        plt.show()
    else:
        graph_fullpath = '{}\{}.png'.format(savPath, title)
        plt.savefig(graph_fullpath)
    return

#给每个柱子上面添加标注
def autolabelH(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        width = rect.get_width()
        ax.annotate('{}'.format(width),
              xy=(width, rect.get_y() + rect.get_height() / 2),
              xytext=(3, 0),  # 3 points vertical offset
              textcoords="offset points",
              ha='left', va='center'
              )

def autolabelHT(rects, ax, taillist):
    index = 0
    for rect in rects:
        width = rect.get_width()
        ax.annotate('{}({})'.format(width, taillist[index]),
              xy=(width, rect.get_y() + rect.get_height() / 2),
              xytext=(3, 0),  # 3 points vertical offset
              textcoords="offset points",
              ha='left', va='center'
              )
        index += 1

#给每个柱子上面添加标注
def autolabelV(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
              xy=(rect.get_x() + rect.get_dwith() / 2, height),
              xytext=(0, 3),  # 3 points vertical offset
              textcoords="offset points",
              ha='center', va='top'
              )

def drawBarAll(path=''):
    # drawBarGraph('test', savPath=path)
    for datatype in historyLib.datatypeSet:

        field = historyLib.STAT_KEY_STOREAGE_CNT
        title = '{}-{}'.format(historyLib.datatypeChn[datatype],
                                   historyLib.statKeyChn[field])
        drawBarGraph(title, datatype, field, savPath=path )

        field = historyLib.STAT_KEY_FILE_CNT
        title = '{}-{}'.format(historyLib.datatypeChn[datatype],
                                   historyLib.statKeyChn[field])
        drawBarGraph(title, datatype, field, savPath=path)

        field = historyLib.STAT_KEY_FIELD_CNT
        title = '{}-{}'.format(historyLib.datatypeChn[datatype],
                                   historyLib.statKeyChn[field])
        drawBarGraph(title, datatype, field, savPath=path )

        field = historyLib.STAT_KEY_RECORD_CNT
        title = '{}-{}'.format(historyLib.datatypeChn[datatype],
                                   historyLib.statKeyChn[field])
        drawBarGraph(title, datatype, field, savPath=path)

def drawPlotAll(path='', field=historyLib.STAT_KEY_STOREAGE_CNT):
    for market in historyLib.marketChn.keys():
        for datatype in historyLib.datatypeChn.keys():
            drawPlotGraph('test', market, datatype, field, True)


def drawPlotGraph(title, market, datatype, field, abbrx=False, savPath=''):
    X, Y = historyLib.siMarketDict.gethostFieldList(market, datatype, field)
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.plot(X, Y)
    xStep = 1
    xpos = np.arange(0, len(X), xStep)
    if abbrx:
        xStep = len(X) // 20
        if xStep < 1:
            xStep = 1
        print(xStep)
        ax.set_xticks(xpos[::xStep])  # 确定每个记号的位置
        ax.set_xticklabels(X[::xStep])  # 确定每个记号的内容

    plt.xticks(rotation=90)
    plt.title(title)
    plt.show()

    return

def drawAllMarketTable(path):
    sheetdict = {}
    tablename = '市场周期汇总表'
    filepath = '{}/{}.xls'.format(path, tablename)

    fildlist = [
        historyLib.STAT_KEY_FILE_CNT,
        historyLib.STAT_KEY_STOREAGE_CNT,
        historyLib.STAT_KEY_RECORD_CNT,
        historyLib.STAT_KEY_FIELD_CNT,
    ]

    for field in fildlist:
        # 其他市场
        table = []
        markenamelist = list(historyLib.marketChn.values())
        table.append(['市场'] + markenamelist)
        for datatype in historyLib.datatypeChn.keys():
            line = historyLib.siMarketDict.getDatatypeFieldList(datatype, field)[1]
            line = [historyLib.datatypeChn[datatype]] + line
            table.append(line)
        line = historyLib.siMarketDict.getDatatypeFieldList('day', historyLib.STAT_KEY_HOST_CNT)[1]
        line = ['站点数'] + line
        table.append(line)
        sheetname = historyLib.statKeyChn[field]
        sheetdict[sheetname] = table

        # 沪深市场
        table = []
        isTableHeadInit = False
        for datatype in historyLib.datatypeChn.keys():
            marketlist,line = historyLib.siMarketDict.getShszDatafield(datatype, field)

            if not isTableHeadInit:
                table.append(['市场'] + marketlist)
                isTableHeadInit = True
            line = [historyLib.datatypeChn[datatype]] + line
            table.append(line)
        line = historyLib.siMarketDict.getShszDatafield('day', historyLib.STAT_KEY_HOST_CNT)[1]
        line = ['站点数'] + line
        table.append(line)
        sheetname = '{}-沪深'.format(historyLib.statKeyChn[field])
        sheetdict[sheetname] = table

    hjio.writeExcel(filepath, sheetdict)



# 绘制曲线图
def commonDrawPlotGraph(title, X, Y, abbrx=1, savPath=''):
    fig, ax = plt.subplots(figsize=(16, 8))
    plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.25)

    xLen = len(X)
    if xLen == 0:
        return
    minMaxLable = '最小值站点：{}\n最小值：{}\n\n最大值站点：{}\n最大值：{}\n'.format(X[0], Y[0], X[xLen-1], Y[xLen-1])
    plt.annotate(minMaxLable,xytext=(X[0], Y[xLen-1]*0.8),xy=(X[0], Y[0]))
    plt.plot(X, Y)

    xStep = 1
    xpos = np.arange(0, xLen, xStep)
    if abbrx > 1:
        xStep = xLen // abbrx
        if xStep < 1:
            xStep = 1
        print(xStep)
        ax.set_xticks(xpos[::xStep])  # 确定每个记号的位置
        ax.set_xticklabels(X[::xStep])  # 确定每个记号的内容

    plt.xticks(rotation=80)
    # plt.legend(['站点数:','单位:KB'])
    plt.title(title)
    if len(savPath) == 0:
        plt.show()
    else:
        graph_fullpath = '{}\{}.png'.format(savPath, title)
        plt.savefig(graph_fullpath)
    return

# 绘制站点数据量汇总曲线图,按市场分表
def drawAllMarketPlot(path='', field=historyLib.STAT_KEY_STOREAGE_CNT):
    for market in historyLib.marketChn.keys():
        X, Y = historyLib.siMarketDict.getAllMarketHostSummary(market, field)
        title = "{}-站点数据量统计-(站点数：{} 单位：KB)".format(historyLib.marketChn[market], len(X))
        commonDrawPlotGraph(title, X, Y, 50, path)

    for market in historyLib.shszSet:
        for level in historyLib.shszLvSet:
            X, Y = historyLib.siMarketDict.getShszHostSummary(market, level, field)
            title = "{}{}-站点数据量统计-(站点数：{} 单位：KB)".format(historyLib.marketChn[market], level, len(X))
            commonDrawPlotGraph(title, X, Y, 40, path)


# 绘制市场周期的二维汇总表,按照3个统计项分表
def drawAllMarketTable2(path=''):
    fildlist = [
        historyLib.STAT_KEY_FILE_CNT,
        historyLib.STAT_KEY_STOREAGE_CNT,
        historyLib.STAT_KEY_RECORD_CNT,
    ]
    sheetdict = {}
    tablename = '站点数据量汇总'

    # 沪深市场数据-区分lv1 lv2
    for market in historyLib.shszSet:
        for level in historyLib.shszLvSet:
            table = []
            isTableHead = True
            for field in fildlist:
                X, Y = historyLib.siMarketDict.getShszHostSummary(market, level, field, False)
                if isTableHead:
                    isTableHead = False
                    X = ['站点'] + X
                    table.append(X)
                elif X != table[0][1:]:
                    print('error {} {}'.format(market, field))
                    print('error', X, table[0][1:])
                Y = [historyLib.statKeyChn[field]] + Y
                table.append(Y)

            title = "{}{}".format(historyLib.marketChn[market], level)
            table = listRT(table)
            sheetdict[title] = table

    # 其他市场数据
    for market in historyLib.marketChn.keys():
        if market == 'shase' or market == 'sznse':
            continue
        table = []
        isTableHead = True
        for field in fildlist:
            X, Y = historyLib.siMarketDict.getAllMarketHostSummary(market, field, False)
            if isTableHead:
                isTableHead = False
                X = ['站点'] + X
                table.append(X)
            elif X != table[0][1:]:
                print('error {} {}'.format(market, field))
                print('error', X, table[0][1:])
                # break
            Y = [historyLib.statKeyChn[field]] + Y
            table.append(Y)

        title = "{}".format(historyLib.marketChn[market])
        table = listRT(table)
        sheetdict[title] = table

    filepath = '{}/{}.xls'.format(path, tablename)
    hjio.writeExcel(filepath, sheetdict)

# 写excel文件
def drawMaketPlotTable(linelist, title, path):
    tableName = "{}/{}.csv".format(path, title)
    hjio.writeCsvbyList(linelist, tableName)
    return

# 列表转置
def listRT(d2list):
    res = []
    for raw in range(len(d2list[0])):
        line = []
        for column in range(len(d2list)):
            line.append(d2list[column][raw])
        res.append(line)
    return res



