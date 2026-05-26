def main():
    text = input("Pishi suda ")
    vowels = ("a", "e", "i", "o", "u")
    new_text = ""

    for t in text:
        if t.lower() not in vowels:
            new_text += t

    print (new_text)

main()