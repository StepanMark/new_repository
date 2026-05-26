months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

new_date = ""

while new_date == "":
    user_input = input("Kakaya data? ")
    try:
        int(user_input.split("/")[0]) <=12 and int(user_input.split("/")[1]) <= 31
        y = user_input.split("/")[2]
        m = user_input.split("/")[0]
        d = user_input.split("/")[1]
        new_date = f"{y}:{m}:{d}"
    except ValueError:
        pass
        
    if user_input.split(", ")[0].split(" ")[0] in months:
        y = user_input.split(", ")[1]
        m = months.index(user_input.split(", ")[0].split(" ")[0])+1
        d = user_input.split(", ")[0].split(" ")[1]
        new_date = f"{y}:{m}:{d}"
        break
    else:
        pass

print(new_date)