
import os
import setting
import csv
import datetime
import xlwt
import xlrd

iobuf = ''
iobufLen = 10
logpath = ''
logcount = 0
logname = 'historyData_process_{}.log'
logSizeDefault = 1024 * 1024 * 5   #bytes


slash = '\\'

rootpath = setting.rootpath
# fucntion
def makepath(root, sub):
    pathSeq = (root, sub)
    return slash.join(pathSeq)

def  wirteCSV(strInfo, path, wroot = False):
    if wroot:
        path = makepath(rootpath, path)
    dirCC(path)
    with open(path, 'w+') as fp:
        fp.write(strInfo)

def writeCsvbyList(linelist, path):
    fp = open(path, 'w', newline='')
    cfpw = csv.writer(fp)
    for line in linelist:
        cfpw.writerow(line)
    fp.close()


def wirteText(strInfo, path):
    dirCC(path)
    with open(path, 'w+') as fp:
        fp.write(strInfo)

def readFile(path, mode = 'r'):
    with open(path, mode) as fp:
        return fp.read()


def dirCC(path):
    pathlist = path.split(os.path.sep)
    for i in range(1,len(pathlist)):
        prefixPath = (os.path.sep).join(pathlist[:i])
        if not os.path.exists(prefixPath):
            os.mkdir(prefixPath)
    return prefixPath


def init(filepath):
    global logpath
    logpath = filepath


def writelog(strLoginfo):
    global iobuf
    dtNow = datetime.datetime.now()
    lineinfo = "{} {}\n".format(dtNow, strLoginfo)
    iobuf += lineinfo
    if len(iobuf) >= iobufLen:
        clearbuf()
    return

def clearbuf(strTail=''):

    global iobuf
    global logcount
    iobuf += strTail
    logfile = logpath + logname.format(logcount)

    try:
        filesize = os.path.getsize(logfile)
        if filesize > logSizeDefault:
            logcount += 1
            logfile = logpath + logname.format(logcount)
    except:
        pass

    with open(logfile, 'a') as fp:
        fp.write(iobuf)
    iobuf = ''


def writeExcel(file, sheetdict):
    fExcel = xlwt.Workbook()
    for sheetName in sheetdict.keys():
        sheet = fExcel.add_sheet(sheetName, cell_overwrite_ok=True)
        rowidx = 0
        for row in sheetdict[sheetName]:
            colidx = 0
            for unit in row:
                sheet.write(rowidx, colidx, unit)
                colidx +=1
            rowidx += 1
    fExcel.save(file)