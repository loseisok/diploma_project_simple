import wmi
from playsound import playsound
import time

w = wmi.WMI(namespace="root\OpenHardwareMonitor")
for _ in range(1):
    temperature_infos = w.Sensor()
    for sensor in temperature_infos:
        if sensor.SensorType == "Temperature":
            if sensor.Name in ["CPU Package", "GPU Core"]:
                print(sensor.Name)
            # print(sensor.Min)
            # print(sensor.Max)
                print(sensor.Value)
            # print(sensor.SensorType)
                if sensor.Value >= 50:
                    playsound('D:\\Python\\diploma\\beep.wav')
    # time.sleep(1)

    # load = w.Sensor()
    # for loade in load:
    #     if loade.SensorType == "Fan":
    #         print(loade.Name)
    #         print(loade.Value)

