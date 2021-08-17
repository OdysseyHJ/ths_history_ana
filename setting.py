
import hjio



# 文件配置路径
# 分析根路径


slash = '\\'

# 程序运行目录
rootpath = r'./'

def makepath(root, sub):
    pathSeq = (root, sub)
    return slash.join(pathSeq)


# 日志路径
logpath = r'.\log\\'


###################################################
#          history data
###################################################
history_data_path = makepath(rootpath, r'\stat')
table_path = makepath(rootpath, r'\table')
graph_bar_path = makepath(rootpath, r'\graph\bar')
graph_plot_path = makepath(rootpath, r'\graph\plot')
allMarketTablePath = makepath(table_path, r'\allMarketTable.csv')
shszTablePath = makepath(table_path, r'\shszTable.csv')