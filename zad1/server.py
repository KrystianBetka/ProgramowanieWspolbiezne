import time

while True:
    try:
        time.sleep(1)
        with open('dane.txt',"r") as f:
            liczba = f.read()
            if(liczba):
                result = int(liczba) * 2
                f.close()
                with open('wyniki.txt',"w") as w:
                    w.write(str(result))
            else :
                with open('wyniki.txt',"w") as w:
                    w.write("")
    except FileNotFoundError:
        pass