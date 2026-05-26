names = []
song_intro = "Adieu, adieu, to "

try:
    while True:
        name = input("Davai imya: ")
        names.append(name)
except KeyboardInterrupt:
    new_names = names[:-1]
    last_name = names[-1]
    song = f"{song_intro}{', '.join(new_names)} and {last_name}"    
    print(song)