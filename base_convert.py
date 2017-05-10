
def base_convert(n,b):
    assert b in [2,10,16,36]
    result=''
    if b==2:
        result= bin(n)
    elif b==10:
        result= int(n)
    elif b==16:
        result= hex(n)
    elif b==36:
        result='  '
        while n != 0:
            n, i = divmod(n, 36)
            result += alphabet[i]
    return str(result)[2:]

number = 0
def trc(n):
    result=[]
    if n==0: result += str(0)
    elif n==1: result += str(1)
    else:
        n, x = divmod(n, 36)
        trc(n)
        if x < 10: result += str(x)
        else: result += chr(x+87)
    return result
alphabet='0123456789abcdefghijklmnopqrstuvwxyz'
base36=''
while number != 0:
    number, i = divmod(number, len(alphabet))
    base36 = alphabet[i] + base36
print(base36)
#print(trc(number))

n,r=divmod(10,6)

print(base_convert(299,36))