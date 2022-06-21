import json, logging, wmi, os
from requests import get

settingsPathFile = r"C:\Users\gerar\AppData\Local\Red-DiscordBot\Red-DiscordBot\data\gmoney\cogs\CustomCommands\settings.json"
redenv = r"C:\Users\gerar\redenv\Scripts"
processName = 'redbot'
botName = 'gmoney'
messagePrefix = "Servers are currently hosted at the following IP: "
ipAPIURL = 'https://api.ipify.org'

logging.basicConfig(filename='customCommands.log',format='%(asctime)s %(message)s', encoding='utf-8', level=logging.DEBUG)

def checkProcess(processName):
    f = wmi.WMI()
    found = False
    for process in f.Win32_Process():
     
        if processName != process.Name:
            continue
        else:
            found = True
            logging.info(processName + " equals " + process.Name)
            break

    return found

def startBot():
    
    logging.info(os.system("taskkill /im " + processName + ".exe /f"))
    logging.info(os.system('cmd /c "' + "cd " + redenv+' & '+'redbot.exe ' + botName + '"'))



f = open(settingsPathFile)
data = json.load(f)
ip = get(ipAPIURL).content.decode('utf8')

if ip not in (data['414589031223512']['GUILD']['307252558546731009']['commands']['gmoneyservers']['response'] ):
    communicationMsg = messagePrefix + ip
    data['414589031223512']['GUILD']['307252558546731009']['commands']['gmoneyservers']['response'] =  communicationMsg

    with open(settingsPathFile, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    logging.info("IP has changed, custom commands updated. Restarting BOT.")
    startBot()

else:
    print("IP change not detected.")
    if checkProcess('redbot') == False:
        logging.info("Could not find bot. Starting it.")
        startBot()


    





