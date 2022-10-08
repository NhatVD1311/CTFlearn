data = [0xC5,0xD9,0xCA,0xCE,0xC7,0xED,0xFF,0xE8]
qword_4018 = [0xDD,0x9B,0xE7,0xF4,0xCE,0xD2,0xEE,0xD0]
qword_4020 = [0xC5,0xCA,0xC7,0xCE,0xC8,0xE2,0xF4,0xCE]

byte_4028 = 0xCF
byte_4029 = 0xF4
byte_402A = 0xD6
xor = 0XAB

flag = ''
flag1 = ''
flag2 = ''
flag3 = '' 
for i in data:
    flag1 += chr(i ^ xor)
for i in qword_4018:
    flag2 += chr(i ^ xor)   
for i in qword_4020:
    flag3 += chr(i ^ xor)
    
flag = flag1[::-1] + flag2[::-1] + flag3[::-1] + chr(byte_4028 ^ xor) + chr(byte_4029 ^ xor) + chr(byte_402A ^ xor)
print(flag)
