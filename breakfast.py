def main():
    time = input("Skoka vremya? ")
    norm_time = convert(time)
    eda(norm_time)

def convert (t):
    t_split = t.split(":")
    hrs = float(t_split[0])
    min = float(t_split[1])
    result = hrs + min/60
    return (round(result, 2))

def eda(v):
    if 7.0 <= v <= 8.0:
        print ("Zavtrak")
    elif 13.0 <= v <= 14.0:
        print ("Obed")
    elif 18.0 <= v <= 19.0:
        print ("Uzhin")
    else:
        print ("Nehui zhrat blyat")

main()