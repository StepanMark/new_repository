file = input("File name, mazfaka? ").lower().strip()
match file:
    case c if c.endswith(".gif"):
        print ("image/gif")
    case c if c.endswith((".jpg", "jpeg")):
        print ("image/jpeg")
    case c if c.endswith(".png"):
        print ("image/png")
    case c if c.endswith(".pdf"):
        print ("text/pdf")
    case c if c.endswith(".zip"):
        print ("archive/zip")    
    case _:
        print ("eblusha")