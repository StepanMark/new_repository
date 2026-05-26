def log_table(spisok):
    log_names = []
    for log in spisok:
        if not log in log_names:
            log_names.append(log)
    log_quant = dict(zip(log_names, ("0" * len(log_names))))
    
    
    for num in spisok:
        if num in log_names:
            log_quant[num] = int(log_quant[num]) + 1

    log_over2 = {}
    for key, value in log_quant.items():
        if value > 2:
            log_over2[key] = value
            
    print(log_over2)



def main():
    log_input = ["login", "update", "login", "error", "login", "update", "error", "error", "logout"]
    log_table(log_input)

main()