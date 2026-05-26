def report(rl):
    
    error_logs = []
    try:
        for r in rl:
            if "rror:" in r: #чтобы не упустить error в верхнем и нижнем регистре
                error_logs.append(r.title())
    except Exception:
        pass


    clean_logs = []        
    for el in error_logs:
        clean_logs.append(el.split(":Error:"))
    
    sum_logs = {}
    for name, number in clean_logs:
        if not name in sum_logs:
            sum_logs.update({name: int(number)})
        else:
            sum_logs[name] += int(number)
    
    return(sum_logs)

def display(sl):

    print() #отступ для красоты
    for name, number in sorted(sl.items()):
        print(f"Станок {name} стоял {number/60:.2f} ч.")

def top_st(rl):

    sort_logs = sorted(rl.items(), key=lambda item: item[1], reverse = True)
    print() #отступ для красоты
    print(f"Дольше всех стоял станок {sort_logs[0][0]} - целых {sort_logs[0][1]/60:.2f} ч.")

def main():
    raw_logs = [
    "CNC_Router_A:Success:0",
    "Lathe_M3:Error:15",
    "CNC_Router_A:Error:5",
    "Press_X1:Success:0",
    "Lathe_M3:Error:10",
    "CNC_Router_A:Error:20",
    "Press_X1:Error:45",
    "Lathe_M3:Success:0",
    "Unknown_Device:Invalid:999" # "Битая" строка
    ]

    rep_logs = report(raw_logs)

    display(rep_logs)
    top_st(rep_logs)

main()    