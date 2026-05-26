def report(fd):
    total_report = {}
    for dat in fd:
        d = dat.split(":")
        if len(d) < 3:
            continue
        time1, time2, machine, *temps = d
        if machine in total_report:
            total_report[machine].append(temps)
        elif temps != []:
            total_report[machine] = [temps]
        else:
            pass
    
    for mac, temp in total_report.items():
        flat = {mac: [item for sub in temp for item in sub]}
        #print(flat)
        flat = {mac: [(sum(int(item) for item in flat[mac]))/len(flat[mac])]}
        print(f"Станок: {mac} | Средняя температура: {flat[mac][0]}")



def main():
    factory_data = [
    "08:00:Press_01:45:47:46",          # 3 датчика температуры
    "08:05:Robot_Arm:32:34",            # 2 датчика
    "08:10:Press_01:50:52:51:53:55",    # 5 датчиков!
    "08:15:Robot_Arm:30",               # 1 датчик
    "08:20:Broken_Link",                # Битая строка (ошибка связи)
    "08:25:Press_01:48:49"              # 2 датчика
]
    
    report(factory_data)

main()