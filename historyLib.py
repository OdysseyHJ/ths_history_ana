import os

import hjio



#统计字段的定义
STAT_KEY_MARKET = 'market'
STAT_KEY_CHANGE_TIME = 'Change'
STAT_KEY_FILE_TYPE = 'data_file'
STAT_KEY_FIELD_CNT = 'field_count'
STAT_KEY_FILE_CNT = 'file_count'
STAT_KEY_STOREAGE_CNT = 'storage_count'
STAT_KEY_RECORD_CNT = 'record_count'
STAT_KEY_HOST_CNT = 'host_count'
STAT_KEY_CALC_STORAGE = 'calc_storage'


originStatKeySet = {
    STAT_KEY_FIELD_CNT,
    STAT_KEY_FILE_CNT,
    STAT_KEY_STOREAGE_CNT,
    STAT_KEY_RECORD_CNT,
}

statKeySet = {
    # STAT_KEY_MARKET,
    # STAT_KEY_FILE_TYPE,
    STAT_KEY_FIELD_CNT,
    STAT_KEY_FILE_CNT,
    STAT_KEY_STOREAGE_CNT,
    STAT_KEY_RECORD_CNT,
    STAT_KEY_HOST_CNT,
}

statKeyChn = {
    # STAT_KEY_MARKET = '',
    # STAT_KEY_FILE_TYPE = '',
    STAT_KEY_FIELD_CNT : '表字段数',
    STAT_KEY_FILE_CNT : '文件总数',
    STAT_KEY_STOREAGE_CNT : '文件合计占用空间(KB)',
    STAT_KEY_RECORD_CNT : '记录总数',
    STAT_KEY_HOST_CNT : '站点总数',
}


#市场定义
# 历史数据处理时生成
marketSet = set()

marketChn = {
    'shase' : '上证',
    'sznse' : '深证',
    'hk' : '港股',
    'bats' : '美股BAT',
    'nyse' : '纽约',
    'nsdq' : '纳斯达克',
    'quota' : '商品期货',
    'shgold' : '上海黄金',
    'cffex' : '中金所',
    'newindx' : '同花顺指数',
    'foreign' : '外汇',
	'fxindx' : '全球指数',
    'europe' : '英股',
	'hz' : '港股期货',
    'options' : '上证期权',
    'szoptions' : '深证期权',
	'shhk' : '沪港通',
	'szhk' : '深港通',
	'stb' : '三板',
	'swindx' : '申万指数',
    'zzindx' : '中证指数',
    'bankbond' : '银行间债券',
    'metal' : '贵金属',
    'nymex' : '外期',
    'indx' : '旧版同花顺指数',
 }


#数据分类定义
DATA_FILE_DAYK = "*.day"
DATA_FILE_MINK = "*.min"
DATA_FILE_MIN5K = "*.mn5"
DATA_FILE_EXT = "*.ext"
DATA_FILE_LATEST_REAL = "*"
DATA_FILE_HISNOWS = "hisnows.now"
DATA_FILE_HISNOWI = "hisnowi.now"
DATA_FILE_HISTRACES = "histraces.trc"
DATA_FILE_HISTRACEI = "histracei.trc"
DATA_FILE_HISMINUTES = "hisminutes.trd"
DATA_FILE_HISMINUTEI = "hisminutei.trd"
DATA_FILE_HISCLOSE = "hiscloseauctiontraces.trc"
DATA_FILE_HISTICKS = "histicks.tic"
DATA_FILE_HISORDERS = "hisorders.tic"
DATA_FILE_HISBORDERS = "hisborders.ord"
DATA_FILE_HISSORDERS = "hissorders.ord"
DATA_FILE_HISOPEN = "hisopenauctiontraces.trc"
DATA_FILE_HISPRE = "hispretraces.trc"
DATA_FILE_HISAFTER = "hisafttraces.trc"

starTrans = {
    DATA_FILE_DAYK : "day",
    DATA_FILE_MINK : 'min',
    DATA_FILE_MIN5K : 'min5',
    DATA_FILE_EXT : 'extra',
    DATA_FILE_LATEST_REAL : 'real_latest_day',
}

datatypeSet = {
    starTrans[DATA_FILE_DAYK],
    starTrans[DATA_FILE_MINK],
    starTrans[DATA_FILE_MIN5K],
    starTrans[DATA_FILE_EXT],
    starTrans[DATA_FILE_LATEST_REAL],
    DATA_FILE_HISNOWS,
    DATA_FILE_HISNOWI,
    DATA_FILE_HISTRACES,
    DATA_FILE_HISTRACEI,
    DATA_FILE_HISMINUTES,
    DATA_FILE_HISMINUTEI,
    DATA_FILE_HISCLOSE,
    DATA_FILE_HISTICKS,
    DATA_FILE_HISORDERS,
    DATA_FILE_HISBORDERS,
    DATA_FILE_HISSORDERS,
    DATA_FILE_HISOPEN,
    DATA_FILE_HISPRE,
    DATA_FILE_HISAFTER,
}

datatypeChn = {
    starTrans[DATA_FILE_DAYK] : '日K线数据',
    starTrans[DATA_FILE_MINK] : '分钟K线数据',
    starTrans[DATA_FILE_MIN5K] : '5分钟K线数据',
    starTrans[DATA_FILE_EXT] : '额外周期数据',
    DATA_FILE_HISNOWS : '股票快照数据',
    DATA_FILE_HISNOWI : '指数快照数据',
    DATA_FILE_HISTRACES : '股票明细数据',
    DATA_FILE_HISTRACEI : '指数明细数据',
    DATA_FILE_HISMINUTES : '股票分时数据',
    DATA_FILE_HISMINUTEI : '指数分时数据',
    DATA_FILE_HISOPEN : '开盘集合竞价明细数据',
    DATA_FILE_HISPRE : '盘前明细数据',
    DATA_FILE_HISCLOSE: '收盘集合竞价明细数据',
    DATA_FILE_HISAFTER: '盘后明细数据',
    DATA_FILE_HISBORDERS: '委买队列数据',
    DATA_FILE_HISSORDERS: '委卖队列数据',
    DATA_FILE_HISORDERS : '逐笔委托数据',
    DATA_FILE_HISTICKS : '逐笔成交数据',
    starTrans[DATA_FILE_LATEST_REAL]: '最新交易日实时数据',
}

SHSZ_LV1 = 'lv1'
SHSZ_LV2 = 'lv2'
shszLvSet = {
    SHSZ_LV1,
    SHSZ_LV2,
}

shszSet = {
    'shase',
    'sznse',
}

dateserverSw = False
dataserver = [
    "sqyd_hq_data_3_186",
    "whdx_hq_data_13_90",
    #"bjwfj_hq_zhu_14_41",
    "njdx_hq_data_12_247",
]

#统计信息字典：
# key (hostname) --- value (dict)
#                     key (market) --- value (dict)
#                                       key (data type) --- value (CStatData)
statistic_data = {}

#市场更新时间字典：
# key (hostname) --- value (dict)
#                     key (market) --- value (date)
host_updatetime = {}

#市场更新时间字典：
# key (hostname) --- value (dict)
#                     key (market) --- value (dict)
#                                       key (data type) --- value (CStatData)
host_market_singleday = {}


klineset = set()
realset = set()

class CStatData:
    def __init__(self, host='', market='', type=''):
        self.host = host
        self.market = market
        self.type = type
        self.field_count = 0
        self.file_count = 0
        self.storage_count = 0
        self.record_count = 0
        self.count = 0
        self.lv2flag = False
        self.date = ''

    def show(self):
        print(self.field_count, self.file_count, self.storage_count, self.record_count)
        return

    def data2list(self):
        return [
            self.host,
            self.market,
            self.type,
            self.field_count,
            self.file_count,
            self.storage_count,
            self.record_count,
        ]

    def getCalcStorage(self):
        return self.record_count * self.field_count * 4 // 1000

    def getField(self, field):
        if field == STAT_KEY_FIELD_CNT:
            return self.field_count
        elif field == STAT_KEY_FILE_CNT:
            return self.file_count
        elif field == STAT_KEY_STOREAGE_CNT:
            return self.storage_count
        elif field == STAT_KEY_RECORD_CNT:
            return self.record_count
        elif field == STAT_KEY_CALC_STORAGE:
            return self.getCalcStorage()
        else:
            return self.count

def getFileList(folderPath):
    fileList = []
    for root, dirs, files in os.walk(folderPath):
        for file in files:
            filepath = '{}\{}'.format(folderPath, file)
            fileList.append(filepath)
    return fileList

def historyKlinedataProc(fileList):
    for file in fileList:

        hostname = file.split('\\')[-1].split('.')[0]

        if dateserverSw:
            if hostname not in dataserver:
                print("skip normal {}".format(hostname))
                continue
        else:
            if hostname in dataserver:
                print("skip dataserver{}".format(hostname))
                continue

        klineset.add(hostname)

        statistic_data[hostname] = {}
        fileContent = hjio.readFile(file)
        lineList = fileContent.split('\n')


        index = 0
        while index < len(lineList):
            line = lineList[index]
            try:
                key = ''
                key, value = getKV(line)
            except:
                index += 1
                continue

            #读到market才开始处理，否则不处理
            if key != STAT_KEY_MARKET:
                index += 1
                continue



            market = value

            if market not in marketSet:
                marketSet.add(market)

            datatype_dict = {}
            index += 1
            line = lineList[index]
            try:
                key = ''
                key, value = getKV(line)
            except:
                index += 1
                continue

            #处理分类数据信息
            isLv2 = False
            while key == STAT_KEY_FILE_TYPE:
                fileType = value.split('/')[-1]
                if fileType in starTrans.keys():
                    fileType = starTrans[fileType]

                # 通过逐笔委托来确认是否是LV2站点
                if fileType == DATA_FILE_HISORDERS:
                    isLv2 = True

                statDataObj = CStatData(hostname, market, fileType)
                index += 1
                valList = getDataKV(lineList, index)

                statDataObj.field_count = valList[0]
                statDataObj.file_count = valList[1]
                statDataObj.storage_count = valList[2]
                statDataObj.record_count = valList[3]
                index = valList[4]

                datatype_dict[fileType] = statDataObj
                line = lineList[index]
                try:
                    key = ''
                    key, value = getKV(line)
                except:
                    index += 1
                    break
            if isLv2:
                for key in datatype_dict.keys():
                    datatype_dict[key].lv2flag = True


            #处理完的市场加入dict
            statistic_data[hostname][market] = datatype_dict
    return

def historyRealdataProc(fileList):
    for file in fileList:

        hostname = file.split('\\')[-1].split('.')[0]

        if dateserverSw:
            if hostname not in dataserver:
                print("skip normal {}".format(hostname))
                continue
        else:
            if hostname in dataserver:
                print("skip dataserver{}".format(hostname))
                continue
        realset.add(hostname)

        host_updatetime[hostname] = {}
        host_market_singleday[hostname] = {}
        try:
            fileContent = hjio.readFile(file)
        except:
            print("fileread error:{}".format(file))
            continue
        lineList = fileContent.split('\n')

        index = 0
        while index < len(lineList):
            line = lineList[index]
            try:
                key = ''
                key, value = getKV(line)
            except:
                index += 1
                continue

            #读到market才开始处理，否则不处理
            if key != STAT_KEY_MARKET:
                index += 1
                continue

            market = value
            datatype_dict_all = {}
            datatype_dict_single = {}
            index += 1
            line = lineList[index]
            try:
                key = ''
                key, value = getKV(line)
            except:
                index += 1
                continue

            if key != STAT_KEY_CHANGE_TIME:
                index += 1
                continue
            YMD = value.split(' ')[1].split('-')
            date = int(''.join(YMD))
            host_updatetime[hostname][market] = date

            index +=1
            line = lineList[index]
            try:
                key = ''
                key, value = getKV(line)
            except:
                index += 1
                continue

            #处理分类数据信息
            isLv2 = False
            while key == STAT_KEY_FILE_TYPE:
                fileType = value.split('/')[-1]
                if fileType in starTrans.keys():
                    fileType = starTrans[fileType]

                # 通过逐笔委托来确认是否是LV2站点
                if fileType == DATA_FILE_HISORDERS:
                    isLv2 = True

                statDataObj = CStatData(hostname, market, fileType)
                index += 1
                valList = getDataKV(lineList, index)

                statDataObj.type = fileType
                statDataObj.field_count = valList[0]
                statDataObj.file_count = valList[1]
                statDataObj.storage_count = valList[2]
                statDataObj.record_count = valList[3]
                index = valList[4]

                if '*' in value:
                    datatype_dict_all[fileType] = statDataObj
                else:
                    datatype_dict_single[fileType] = statDataObj

                line = lineList[index]
                try:
                    key = ''
                    key, value = getKV(line)
                except:
                    index += 1
                    break


            #处理完的市场加入dict
            if hostname in statistic_data.keys():
                statistic_data[hostname][market] = mergeDict(statistic_data[hostname][market], datatype_dict_all)
                if hostname == 'nw_hq_shsz_200_120' and market == 'shase':
                    print("debug1", statistic_data[hostname][market].keys())

                # # 需要在这里校验lv1 lv2
                if isLv2:
                    for key in statistic_data[hostname][market].keys():
                        try:
                            statistic_data[hostname][market][key].lv2flag = True
                            # datatype_dict_single[key].lv2flag = True
                        except:
                            # print(hostname, market, datatype_dict_all.keys(), datatype_dict_single.keys())
                            pass
            else:
                # print('lack base data:{}'.format(hostname))
                pass
            # 需要在这里校验lv1 lv2

            # if isLv2:

            single_day_lv2 = False
            for key in datatype_dict_single.keys():
                if datatype_dict_single[key].type == DATA_FILE_HISORDERS:
                    single_day_lv2 = True
                    break
            if single_day_lv2:
                for key in datatype_dict_single.keys():
                    datatype_dict_single[key].lv2flag = True
            host_market_singleday[hostname][market] = datatype_dict_single
    return


def getKV(line):
    parseList = line.split(':')
    if len(parseList) < 2:
        return None
    return (parseList[0], parseList[1])

    # def get
def getDataKV(linelist, start):
    index = start
    valList = []
    while index < len(linelist) and len(valList) < 4:
        try:
            key,val = getKV(linelist[index])
        except:
            index += 1
            continue
        if key == STAT_KEY_MARKET or key == STAT_KEY_FILE_TYPE:
            return
        if key not in statKeySet:
            index += 1
            continue
        try:
            val = int(val)
        except:
            val = 0
        valList.append(val)
        index += 1

    while len(valList) < 4:
        valList.append(0)
    valList.append(index)
    return valList

def mergeDict(target, source, iscover=False):
    for key in source.keys():
        if iscover:
            target[key] = source[key]
        elif key not in target.keys():
            target[key] = source[key]
    return target

# def single_day_lv2proc(dict2proc):


def genCsv(path):
    tableHead = ['主机名',
                 '市场',
                 '数据分类',
                 '表格字段数',
                 '文件总数',
                 '文件总计存储空间',
                 '文件中记录总数']
    wholeTable = [tableHead]
    typeTableDict = {}

    hostList = list(statistic_data.keys())
    hostList.sort()
    for host in hostList:
        marketDict = statistic_data[host]
        marketList = list(marketDict.keys())
        marketList.sort()
        for market in marketList:
            datatypeDict = marketDict[market]
            datatypeList = list(datatypeDict.keys())
            datatypeList.sort()
            for filetype in datatypeList:
                dataObj = datatypeDict[filetype]
                lineInfo = dataObj.data2list()
                wholeTable.append(lineInfo)

                if filetype not in typeTableDict.keys():
                    typeTableDict[filetype] = [tableHead]
                typeTableDict[filetype].append(lineInfo)


    wholeTablePath = '{}\{}'.format(path, 'total_table.csv')
    hjio.writeCsvbyList(wholeTable, wholeTablePath)

    for key in typeTableDict.keys():
        tableName = '{}\{}.csv'.format(path, key)
        hjio.writeCsvbyList(typeTableDict[key], tableName)

    return





class CMarketDict:
    def __init__(self):
        self.MHD_Dict = {}
        self.MDH_Dict = {}
        self.summaryDict = {}
        # k,v   market,dict
        #               k,v  level, dict
        #                           k,v   datatype, dict
        #                                           k,v   host,data
        self.shszDict = {}
        self.shszSummary = {}
        self.shsz_MLHD_Dict = {}

    def summaryDictInit(self):
        for market in self.MDH_Dict.keys():
            self.summaryDict[market] = {}

            for datatype in self.MDH_Dict[market].keys():
                self.summaryDict[market][datatype] = CStatData()
                AllDataObj = self.MDH_Dict[market][datatype]
                count = len(AllDataObj)
                fieldReal = {}
                for host in AllDataObj.keys():
                    dataObj = AllDataObj[host]
                    if dataObj.field_count not in fieldReal.keys():
                        fieldReal[dataObj.field_count] = 1
                    else:
                        fieldReal[dataObj.field_count] += 1
                    self.summaryDict[market][datatype].file_count += dataObj.file_count
                    self.summaryDict[market][datatype].record_count += dataObj.record_count
                    self.summaryDict[market][datatype].storage_count += dataObj.storage_count
                self.summaryDict[market][datatype].storage_count //= 1000
                # self.summaryDict[market][datatype].record_count *= 4 / 1000
                self.summaryDict[market][datatype].count = count
                self.summaryDict[market][datatype].field_count = getMaxValueKey(fieldReal)


    # 获取所有市场的分类数据
    def getDatatypeFieldList(self, datatype='day', field=STAT_KEY_FIELD_CNT):
        marketList = list(marketChn.keys())
        # print(marketList)
        dataList = []
        for market in marketList:
            if datatype not in self.summaryDict[market].keys():
                #有些市场没有特定的数据，这些数据置0
                dataList.append(0)
                continue
            dataList.append(self.summaryDict[market][datatype].getField(field))

        return (marketList, dataList)

    # 获取指定市场全部数据分类的数据
    def getMrketFieldlist(self, market='shase', field=STAT_KEY_FIELD_CNT):
        if market not in self.summaryDict.keys():
            return ([],[],[])

        datatypeList = list(self.summaryDict[market].keys())
        dataList = []
        hostCntList = []
        for datatype in self.summaryDict[market].keys():
            dataDict =  self.summaryDict[market][datatype]
            data = 0
            hostCnt = 0
            for host in dataDict.keys():
                data = dataDict[host].getField(field)

                hostCnt = len(dataDict[host])
            dataList.append(data)
            hostCntList.append(hostCnt)
        return (datatypeList, dataList, hostCntList)

    # 获取站点数据信息
    def gethostFieldList(self, market='shase', datatype='day', field=STAT_KEY_FIELD_CNT):
        hostdict = {}
        hostlist = []
        vallist = []
        if market not in self.MDH_Dict.keys():
            print(market, self.MDH_Dict.keys())
            return ([],[])
        if datatype not in self.MDH_Dict[market].keys():
            print(datatype, self.MDH_Dict[market].keys())
            return ([],[])

        datahandle = self.MDH_Dict[market][datatype]
        for host in datahandle.keys():
            hostdict[host] = datahandle[host].getField(field)
        # print(hostdict)
        sortedDict = sorted(hostdict.items(), key=lambda d: d[1], reverse=False)

        for host,val in sortedDict:
            hostlist.append(host)
            vallist.append(val)
        return (hostlist, vallist)

    # 沪深lv2数据处理
    def shszSummaryInit(self):
        for market in self.shszDict.keys():
            for level in self.shszDict[market].keys():
                for datatype in self.shszDict[market][level].keys():
                    if market not in self.shszSummary.keys():
                        self.shszSummary[market] = {}
                    if level not in self.shszSummary[market].keys():
                        self.shszSummary[market][level] = {}
                    self.shszSummary[market][level][datatype] = CStatData()
                    fieldReal = {}
                    dataDict = self.shszDict[market][level][datatype]
                    for host in dataDict.keys():
                        dataObj = dataDict[host]

                        if dataObj.field_count not in fieldReal.keys():
                            fieldReal[dataObj.field_count] = 1
                        else:
                            fieldReal[dataObj.field_count] += 1
                        self.shszSummary[market][level][datatype].file_count += dataObj.file_count
                        self.shszSummary[market][level][datatype].storage_count += dataObj.storage_count
                        self.shszSummary[market][level][datatype].record_count += dataObj.record_count
                    self.shszSummary[market][level][datatype].storage_count //= 1000
                    self.shszSummary[market][level][datatype].count = len(dataDict)
                    self.shszSummary[market][level][datatype].field_count = getMaxValueKey(fieldReal)

    def getShszDatafield(self, datatype='day', field=STAT_KEY_FIELD_CNT):
        marketList = []
        dataList = []

        for market in self.shszSummary.keys():
            for level in self.shszSummary[market].keys():
                marketList.append('{}-{}'.format(marketChn[market], level))
                datadict = self.shszSummary[market][level]
                if datatype not in datadict.keys():
                    dataList.append(0)
                    continue
                dataList.append(datadict[datatype].getField(field))

        return (marketList, dataList)

    def getAllMarketHostSummary(self, market, field, isSorted=True):
        hostlist = list(self.MHD_Dict[market].keys())
        dataDict = {}
        for host in hostlist:
            data = 0
            for datatype in self.MHD_Dict[market][host].keys():
                data += self.MHD_Dict[market][host][datatype].getField(field)
            if field == STAT_KEY_STOREAGE_CNT:
                data //= 1000
            dataDict[host] = data
        if isSorted:
            dataDict = dictSortedByVal(dataDict)
        # else:
        #     dataDict = dictSortedByKey(dataDict)
        # # print(dataDict.keys())
        return (list(dataDict.keys()), list(dataDict.values()))

    def getShszHostSummary(self, market, level, field, isSorted=True):
        # print(market, level, field)
        if market not in self.shsz_MLHD_Dict.keys():
            return ([], [])
        if level not in self.shsz_MLHD_Dict[market].keys():
            return ([], [])
        tarDict = self.shsz_MLHD_Dict[market][level]
        hostlist = list(tarDict.keys())
        dataDict = {}
        for host in hostlist:
            data = 0
            # if host == 'nw_hq_shsz_200_120' and market == 'shase':
            #     print(id(tarDict[host]), tarDict[host].keys())
            for datatype in tarDict[host].keys():
                # 最新当天的数据不统计
                if datatype == DATA_FILE_LATEST_REAL:
                    continue
                data += tarDict[host][datatype].getField(field)
                # if host == 'hwy_hq_mobsh_36_46' and market == 'shase' and field == STAT_KEY_STOREAGE_CNT:
                #     print(host, datatype, field, tarDict[host][datatype].getField(field), data)
                #     print(host, datatype, field, data)
            if field == STAT_KEY_STOREAGE_CNT:
                data //= 1000
            dataDict[host] = data
        if isSorted:
            dataDict = dictSortedByVal(dataDict)
        # if 'hwy_hq_zhu_246_214' in dataDict.keys():
        #     print(dataDict['hwy_hq_zhu_246_214'])
        # else:
        #     dataDict = dictSortedByKey(dataDict)
        return (list(dataDict.keys()), list(dataDict.values()))

# 获取字典计数中，获取计数数值最大的key
def getMaxValueKey(tdict):
    if len(tdict) == 0:
        return 0
    max_key, max_val = list(tdict.items())[0]
    for key,val in tdict.items():
        if val > max_val:
            max_val = val
            max_key = key
    return max_key


siMarketDict = CMarketDict()
def MarketDataInit(type='kline'):
    dataHostDict = {}
    if type == 'real':
        dataHostDict = host_market_singleday
    else:
        dataHostDict = statistic_data
    for host in dataHostDict.keys():
        hostData = dataHostDict[host]
        for market in hostData.keys():
            marketData = hostData[market]

            # 检查host的市场近期是否更新, 近期没有更新的则不计入统计数据字典
            if checkIsOutofdate(host, market):
                continue

            for datatype in marketData.keys():
                dataObj = marketData[datatype]
                # print(datatype)
                if market not in siMarketDict.MHD_Dict.keys():
                    siMarketDict.MHD_Dict[market] = {}
                    siMarketDict.MDH_Dict[market] = {}

                # 构建 market-host-datatype-dataobj字典
                if host not in siMarketDict.MHD_Dict[market].keys():
                    siMarketDict.MHD_Dict[market][host] = {}
                siMarketDict.MHD_Dict[market][host][datatype] = dataObj

                # 构建 market-datatype-host-dataobj字典
                if datatype not in siMarketDict.MDH_Dict[market].keys():
                    siMarketDict.MDH_Dict[market][datatype] = {}
                siMarketDict.MDH_Dict[market][datatype][host] = dataObj

                # 构建沪深特殊字典
                if market in shszSet:
                    level = SHSZ_LV1
                    if dataObj.lv2flag:
                        level = SHSZ_LV2
                    if market not in siMarketDict.shszDict.keys():
                        siMarketDict.shszDict[market] = {}
                        siMarketDict.shsz_MLHD_Dict[market] = {}
                    if level not in siMarketDict.shszDict[market].keys():
                        siMarketDict.shszDict[market][level] = {}
                        siMarketDict.shsz_MLHD_Dict[market][level] = {}

                    if datatype not in siMarketDict.shszDict[market][level].keys():
                        siMarketDict.shszDict[market][level][datatype] = {}
                    siMarketDict.shszDict[market][level][datatype][host] = dataObj

                    if host not in siMarketDict.shsz_MLHD_Dict[market][level].keys():
                        siMarketDict.shsz_MLHD_Dict[market][level][host] = {}
                    siMarketDict.shsz_MLHD_Dict[market][level][host][datatype] = dataObj

                    # 查找问题站点
                    # if market == 'sznse' and level == SHSZ_LV1 and DATA_FILE_HISTICKS == datatype:
                    #     print('special host:', host)



    siMarketDict.summaryDictInit()
    siMarketDict.shszSummaryInit()

    return

# storage = x Bytes
storageUnit = ['B', 'KB', 'MB', 'GB']
storageStep = 1000
def getAutoStorage(storage, limitBits=4):
    division = pow(10, limitBits)
    index = 1
    while storage // division > 0 and index < len(storageUnit)-1:
        index += 1
        storage //= storageStep
    res = '0'
    if storage != 0:
        res = '{} {}'.format(storage, storageUnit[index])
    return res

def getAutoStorageList(storagelist, limitBits=4):
    for index in range(len(storagelist)):
        storagelist[index] = getAutoStorage(storagelist[index])
    return storagelist

def marketnameChnese(listname):
    reslist = []
    for name in listname:
        reslist.append(marketChn[name])
    return reslist

def dictSortedByVal(unsortedDict, reverseFlag=False):
    return dict(sorted(unsortedDict.items(), key=lambda d: d[1], reverse=reverseFlag))

def dictSortedByKey(unsortedDict, reverseFlag=False):
    return dict(sorted(unsortedDict.items(), key=lambda d: d[0], reverse=reverseFlag))

def checkIsOutofdate(hostname, market, cmpdate=20210730):
    isOut = False
    if hostname not in host_updatetime.keys():
        return True
    if market not in host_updatetime[hostname].keys():
        return True
    date = host_updatetime[hostname][market]

    if date <= cmpdate:
        isOut = True
        # print(date)
        print("out of date: {} {}".format(hostname, market))
    return isOut

def init(path):
    pathKline = '{}/kline'.format(path)
    pathReal = '{}/real'.format(path)
    filelist = getFileList(pathKline)
    historyKlinedataProc(filelist)

    filelistReal = getFileList(pathReal)
    historyRealdataProc(filelistReal)

    # MarketDataInit('kline')
    MarketDataInit('real')