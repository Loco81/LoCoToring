from libraries import *




drive_ = os.environ['USERPROFILE'][0]+":\\"
files_ = sys._MEIPASS+'\\Files\\'
#files_ = 'C:\\Users\\LoCo\\Desktop\\LoCoToring\\Code\\Files\\'
data_ = f'{drive_}Windows\\'
#data_ = ''

clr.AddReference(f'{files_}OpenHardwareMonitorLib.dll') 
from OpenHardwareMonitor.Hardware import Computer # type: ignore





c = Computer()
c.Open()
types = []
lener = 0
# c.MainboardEnabled = True # get the Info about Mainboard
c.CPUEnabled = True # get the Info about CPU
if len(c.Hardware) > lener:
    lener+=1
    types.append('CPU')
c.RAMEnabled = True # get the Info about Memory
if len(c.Hardware) > lener:
    lener+=1
    types.append('RAM')
c.GPUEnabled = True # get the Info about GPU
if len(c.Hardware) > lener:
    lener+=1
    types.append('GPU')
c.HDDEnabled = True # get the Info about Hards
if len(c.Hardware) > lener:
    lener+=1
    types.append('HDD')
if len(c.Hardware) > lener:
    lener+=1
    types.append('HDD2')
# c.FanControllerEnabled = True # get the Info about Fans


############################## Fill Headers
hardwares = {}
for k in range(len(c.Hardware)):
    catch = {'Name'}
    for i in c.Hardware[k].Sensors:
        header = i.Identifier.ToString().split('/')[3]
        try: int(header)
        except: catch.add(header)
        else: catch.add(i.Identifier.ToString().split('/')[2])
    d = dict()
    for i in catch:
        d[i] = dict()
    hardwares[types[k]] = d
    catch.clear()
###########################################

class monitoring_thread(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    newInfo = QtCore.pyqtSignal(dict)
    FPS = QtCore.pyqtSignal(int)
    
    @QtCore.pyqtSlot()

    def starter(self):
        while True:
            ############################# Fill Data
            for k in range(len(c.Hardware)):
                hardware = c.Hardware[k]
                hardware.Update()
                hardwares[types[k]]['Name'] = hardware.Name
                for i in hardware.Sensors:
                    header = i.Identifier.ToString().split('/')[3]
                    try: int(header)
                    except: hardwares[types[k]][header][i.Name] = i.get_Value()
                    else: hardwares[types[k]][i.Identifier.ToString().split('/')[2]][i.Name] = i.get_Value()
            self.newInfo.emit(hardwares)
            time.sleep(0.4)
        self.finished.emit()
        c.Close()