import os  
import time  
import errno 
import random
random_number = random.randint(1000, 9999)


name = input("Podaj nazwe klienta: ")
name += f"_{random_number}"
print("Twoja zaktualizowana nazwa to ",name)

while True:  
    try:  
        fd = os.open("lockfile", os.O_CREAT|os.O_EXCL|os.O_RDWR)  
        break;  
    except FileExistsError:
        print("Serwer zajęty proszę czekać")
        time.sleep(1)
print("plik zamkowy utworzony") 


print("Podaj tekst dla serwera (wpisz 'Esc', aby zakończyć):")  
contents = [name]
while True:
    line = input()
    if line == 'Esc':
        break
    contents.append(line)


text = '\n'.join(contents)
with open("server.txt","w") as server_file:
    server_file.write(text)

os.close(fd) 


