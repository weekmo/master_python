'''
>>> base_convert(2555,2)
'100111111011'
>>> base_convert(42,2)
'101010'
>>> base_convert(0,2)
'0'
>>> base_convert(2555,10)
'2555'
>>> base_convert(0,10)
'0'
>>> base_convert(4711,10)
'4711'
>>> base_convert(2555,16)
'9fb'
>>> base_convert(0,16)
'0'
>>> base_convert(10,16)
'a'
>>> base_convert(2555,36)
'1yz'
>>> base_convert(0,36)
'0'
'''


def base_convert(n,b):
    assert b in [2,10,16,36]
    try:
        alphabet='0123456789abcdefghijklmnopqrstuvwxyz'
        result=''
        if b==2:
            result = bin(n)
            result=result[2:]
        elif b==10:
            result = int(n)
        elif b==16:
            result= hex(n)
            result=result[2:]
        elif b==36:
            if n==0:
                result=0
            while n != 0:
                n, i = divmod(n, 36)
                result = alphabet[i] + result
        return str(result)
    except TypeError:
        return "Please put integer only!"

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(base_convert(0,2))
    print(base_convert(1,2))
    print(base_convert(299,2))
    print(base_convert(0,10))
    print(base_convert(1,10))
    print(base_convert(299,10))
    print(base_convert(0,16))
    print(base_convert(1,16))
    print(base_convert(299,16))
    print(base_convert(0,36))
    print(base_convert(1,36))
    print(base_convert(299,36))
    print(base_convert(299,3))

