import time

liczba = int(input("Podaj pojedynczą liczbę całkowitą: "))
time.sleep(1)
    
with open("dane.txt","w") as f:
        f.write(str(liczba))
while True:
        try: 
            time.sleep(1)
            with open("wyniki.txt","r") as w:
                wynik= w.read()
                print(f'Wynik dla {liczba} to {wynik}')
                break
        except FileNotFoundError:
            time.sleep(1)