p = 46   # public
g = 8     # public
 
alice = 25
bob = 18
a = (g**alice) % p
b = (g ** bob) % p
alicemessage = (B ** alice) % p
bobmessage = (A**bob) % p
print( "Alice private message: ", alicemessage )
print( "Bob private message: ", bobmessage )
print( "\n  Alice Sends Over Public Chanel: " , a )
print( "\n  Bob Sends Over Public Chanel: ", b )
