import pwn

def decipher(): 
    a= bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
    ba = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
    bc = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
    dacb = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

    b = pwn.xor(a,ba)
    c = pwn.xor(b,bc)

    d = bytes.decode(pwn.xor(dacb,a,c,b),"utf-8")

    return d

    



print(decipher())



