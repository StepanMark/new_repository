def clean(d):
    cleaned_data = []
    data_sum = 0
    for i in d:
        if isinstance(i, int) and i >0 :
            cleaned_data.append(i)
            data_sum += i

    data_len = len(cleaned_data)
    print (f"{cleaned_data},\n{data_sum},\n{data_len}")
    


raw_data = [100, "error", -50, 200, None, 300, "unknown", 450]
clean_data = clean(raw_data)