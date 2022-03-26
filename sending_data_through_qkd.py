import keypolarizer
text="THIS IS A LONG MESSAGE BEING SENT THROUGH QKD"
print("The text to be sent is ",text)
data=[char for char in text]
print("Here the text that is being is sent is seperated to single characters giving us the list = ",data)
out=''
emp=[0]*len(data)

for i in range(0,len(data)):
    temp=data[i]
    res = ''.join(format(ord(i), '08b') for i in temp)
    emp[i]=res
print("Now each character is concerted into the binary equivalent of their ascii value for transmission which can be seen here = ")
print(emp)
for i in range(0,len(emp)):
    send=([char for char in emp[i]])
    alicenewphot=[0]*len(send)
    def newsend():
        for i in range(0,len(send)):
            if(send[i]=='0' and keypolarizer.newpol[i]=='p'):
                alicenewphot[i]='v'
            elif(send[i]=='0' and keypolarizer.newpol[i]=='x'):
                alicenewphot[i]='r'
            elif(send[i]=='1' and keypolarizer.newpol[i]=='x'):
                alicenewphot[i]='l'
            elif(send[i]=='1' and keypolarizer.newpol[i]=='p'):
                alicenewphot[i]='h'
            else:
                print(send[i])
        return(alicenewphot)
    newsend()
    print("This is the stream of photons being sent for each of the characters",alicenewphot)
    bindata=[0]*len(alicenewphot)
    def finalar():
        for i in range(0,len(alicenewphot)):
            if(keypolarizer.newpol[i]=='p' and alicenewphot[i]=='v'):
                bindata[i]=0
            elif(keypolarizer.newpol[i]=='p' and alicenewphot[i]=='h'):
                bindata[i]=1
            elif(keypolarizer.newpol[i]=='x' and alicenewphot[i]=='r'):
                bindata[i]=0
            elif(keypolarizer.newpol[i]=='x' and alicenewphot[i]=='l'):
                bindata[i]=1
            else:
                print("Error in transmission")
        return bindata
    finalar()
    print("This is the binary data recived after being sent through the polarizers",bindata)

    s = [str(i) for i in bindata]
        
        # Join list items using join()
    res = int("".join(s))
    def BinaryToDecimal(binary):
            
        binary1 = binary
        decimal, i, n = 0, 0, 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary//10
            i += 1
        return (decimal)
    decimal_data = BinaryToDecimal(res)
    
    out= out + chr(decimal_data)
    
print("This is the text recived after QKD ",out)

