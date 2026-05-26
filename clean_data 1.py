def clean(d):
    clean_data = [k for k in d if isinstance(k, int) and k > 0]
    print (clean_data)
    print (sum(clean_data))


raw_data = [100, "error", -50, 200, None, 300, "unknown", 450]
clean_data = clean(raw_data)