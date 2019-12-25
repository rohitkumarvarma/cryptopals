from Crypto.Cipher import AES
key = "YELLOW SUBMARINE"
ctlist = []
iv = "\x00" * 16
f = open("10.txt","r")
k = f.readlines()
s ="".join(k)
def AES_decrypt(ct, key):
	cipher = AES.new(key, AES.MODE_ECB)	
	pt=cipher.decrypt(ct)
	return(pt)
def supplyct(s):
    g=-16
    k=0

    for i in range (len(s)//16):
        g = g+16
        k = k+16
        s1 = ""
        for j in range (g,k):
            s1 = s1+s[j]
        ctlist.append(s1)
    return (ctlist)
def plaintext(s):
    mylist = print(supplyct(s))
    for i in range (len(mylist)):
        if i==0:
            pt1 = AES_decrypt(s[0], key)
	#code incomplete
            
            
            
            
