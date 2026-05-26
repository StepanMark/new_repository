def sklei(id, nam):
    return(dict(zip(id, nam)))
  

def user_update (old):
    new_name = input("New user - ")
    new_id = input("New ID - ")
    old[new_id] = new_name

def main():
    ids = [101, 102, 103, 104]
    names = ["Alice", "Bob", "Charlie", "David"]

    employee_map = sklei(ids, names)
    print(f"Initial map: {employee_map}")

    user_update(employee_map)
    print(f"Updated map: {employee_map}")
main()