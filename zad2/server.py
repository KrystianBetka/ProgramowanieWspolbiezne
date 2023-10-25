import os
import time

while True:
    while not os.path.exists("server.txt") or os.stat("server.txt").st_size == 0:
        time.sleep(1)

    with open("server.txt", 'r') as bufor:
        client_name = bufor.readline().strip()

        print("Podaj odpowiedź dla klienta: " + client_name + " (wpisz 'Esc', aby zakończyć):")
        contents = []
        while True:
            line = input()
            if line == 'Esc':
                break
            contents.append(line)
        text = '\n'.join(contents)

        with open(client_name, "w") as response_file:
            response_file.write(text)

        with open("server.txt", "w"):
            pass  

        os.unlink("lockfile")
        print("Koniec, plik zamkowy zlikwidowany")
