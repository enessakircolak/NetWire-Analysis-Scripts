import sys
with open(sys.argv[1], 'rb') as f:
    hexdata = f.read().hex()
i=0
while True:
    a=int(hexdata[i:i+2],16)
    if(a<36):
        x = hex(a+220 ^ 157)
    else:
        x = hex(a-36 ^ 157)
    if(str(x[2:4])=="c4" or str(x[2:4])=="b1" or str(x[2:4])=="d8" or 
    str(x[2:4])=="c3" or str(x[2:4])=="bc" or str(x[2:4])=="d4" or
    str(x[2:4])=="b0" or str(x[2:4])=="c5" or str(x[2:4])=="9f"):
        i=i+2
    else:
        text_file = open("DecodedLogs.txt", "a")
        if(len(x)==4):
            t=(bytes.fromhex(str(x[2:4])).decode('utf-8'))
            text_file.write(t)
        elif(len(x)==5):
            print("none")
        else:
            t=(bytes.fromhex("0"+str(x[2:3])).decode('utf-8'))
            text_file.write(t)
        text_file.close()
        i=i+2
