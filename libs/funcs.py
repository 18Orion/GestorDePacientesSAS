from datetime import date
from datetime import datetime
import requests
from platform import system
from urllib.request import urlretrieve
from subprocess import check_call
import sys

def toSpanishDate(unformattedDate):
    if type(unformattedDate) is int:
        return date.fromordinal(unformattedDate).strftime("%d-%m-%Y")
    elif type(unformattedDate) is date:
        return unformattedDate.strftime("%d-%m-%Y")

def toOrdinal(unformattedDate, spanish=False):
    if spanish:
        dateList=unformattedDate.split("-")
        ordinalDate=date.fromisoformat(dateList[2]+"-"+dateList[1]+"-"+dateList[0]).toordinal()     #YYYY-MM-DD
        return ordinalDate
    elif type(unformattedDate) is date:
        return unformattedDate.toordinal()

def isValidNUSHA(nusha):
    return (len(nusha)==10)and(nusha.isnumeric())

def formatNUSHA(nusha):
    formattedNusha=""
    for i in range(10-len(str(nusha))):
        formattedNusha+="0"
    formattedNusha+=str(nusha)
    return formattedNusha

def inputLogin():
    user=input("Usuario: ")
    passwd=input("Contraseña: ")
    cred=(user, passwd)
    return cred

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def update(packageType, version="latest"):
    if version=="latest":
        version = (getLatestVersion(), system())
    else:
        version = (version, system())
    print("Descargando version "+version[0]+" para la plataforma "+version[1])
    match packageType:
        case "source":
            sourceName="GestorDePacientesRadioterapia"+"-"+version[0].replace("v", "")+".zip"
            #urlretrieve("https://github.com/18Orion/GestorDePacientesRadioterapia/archive/refs/tags/"+version[0]+".zip", "source.zip")
            urlretrieve("https://github.com/18Orion/GestorDePacientesRadioterapia/archive/refs/heads/main.zip", "release.zip")
        case "compiled":
            if version[1]=="Linux":
                urlretrieve("https://github.com/18Orion/GestorDePacientesRadioterapia/releases/latest/download/linuxRelease.zip", "release.zip")
            elif version[1]=="Windows":
                urlretrieve("https://github.com/18Orion/GestorDePacientesRadioterapia/releases/latest/download/winRelease.zip", "release.zip")

def getLatestVersion():
    return requests.get("https://github.com/18Orion/GestorDePacientesRadioterapia/releases/latest").url.split("/").pop()

def getVersionInt(version):
    return int(version.replace("v","").replace(".",""))

def getNameListFromFile(file, error):
    nameList=["Sin escoger"]
    try:
        f=open(file,"r")
        for line in f:
            if line[0]!='#':
               nameList.append(line.replace("\n",""))
        f.close()
        return nameList
    except:
        f=open(file,"w")
        f.write(error)
        f.close()
        return nameList

def installDependencies(requirementsFile):
    packages=[]
    f=open(requirementsFile,"r")
    for package in f:
        packages.append(package)
    f.close()
    print("Instalando dependencias...")
    for i in range(len(packages)):
        printProgressBar(i, len(packages), suffix=packages[i])
        pipInstall(package=packages[i])
    printProgressBar(len(packages), len(packages), suffix="Todo instalado")
    print("\n")

def pipInstall(package):
    check_call([sys.executable, "-m", "pip", "install", package, "--break-system-packages", "--quiet"])