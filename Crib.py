# encoding=utf8  

def strxor(a, b):     # xor two strings of different lengths, esta funcion es dada por el profesor Dan Boneh y su fin es calcular la funcion xor de dos strings de tamaños diferentes
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

cipher1 = "315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba5025b8cc57ee59418ce7dc6bc41556bdb36bbca3e8774301fbcaa3b83b220809560987815f65286764703de0f3d524400a19b159610b11ef3e"
cipher2 = "234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3a9f1cb74151f6d551f4480c82b2cb24cc5b028aa76eb7b4ab24171ab3cdadb8356f"
cipher1 = cipher1.decode('hex')
cipher2 = cipher2.decode('hex')
xored3 = strxor(cipher2,cipher1)
#print xored3.encode('hex')
#Acá entramos en la parte 'interactiva' del codigo, pues el usuario deberá ensayar palabras que posiblemente estém en alguno de los dos textos originales, e ir armando una frase larga o 'crib' que mas tarde servirá para sacar la llave original
i=0
for i in range(len(xored3)):
	crib = "Euler would probably enjoy that now his theorem becomes a corner stone of crypto - Annonymous on Euler's theorem"#texto recobrado completo, perteneciente al segundo texto cifrado, pues su tamao es equivalente
	#crib = ' factor the number '
	crib2 = crib.encode('hex')
	exam = strxor(crib,xored3[i:])
	print exam

if  len(crib2) == len (cipher2.encode('hex')) or len(word2) == len (cipher1.encode('hex')):
	print 'Genial, ya tenemos un mensaje totalmente descifrado, que servirá para generar una buena porción de la llave original'
	print 'Mensaje descifrado (crib): '+crib
#aca comparamos los tamaños del posible crib recobrado con los textos cifrados para ver a cual pertenece segun comparacion de tamao

#crib = "We can factor the number 15 with quantum computers. We can also factor the number 15 with a dog trained "
#crib = "Euler would probably enjoy that now his theorem becomes a corner stone of crypto - Annonymous on Euler's theorem"
#una vez tenemos un crib o texto descifrado y tenemos la certeza se que este pertenece a un texto cifrado, vamos a sacar la clave K xoreando este texto con el crib
crib = "Euler would probably enjoy that now his theorem becomes a corner stone of crypto - Annonymous on Euler's theorem"
key = strxor(crib,cipher2)
print "Llave calculada: "+ key.encode('hex')#<--------------esto mostrara la llave, que en teoria deberia ser "o parecer" un numero aleatorio

#Probemos, ahora con esta llave, al xorearla con el texto cifrado dos, deberia dar en teoria el crib que hemos sacado
euler = strxor(cipher2,key)#tenemos un ganador para la llave, sin embargo esta es solo una porcion de la llave, va a tomar mas trabajo el conseguir la clave mas larga, pero la pregunta es, es necesaria la llave entera?
#print "Euler: "+euler.encode('ascii')
if crib == euler.encode('ascii'):
	print 'La llave, de hecho, funciona.'
else:
	print 'Error, la llave no genera el mismo texto en plano (crib) al usara con el texto cifrado'

key = "66396e89c9dbd8cc9874352acd6395102eafce78aa7fed28a07f6bc98d29c50b69b0339a19f8aa401a9c6d708f80c066c763fef0123148cdd8e802d05ba98777335daefcecd59c433a6b268b60bf4ef03c9a611098bb3e9a3161edc7b804a33522cfd202d2c68c57376edba8c2ca5002"
cipher11 = "32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904"
#El texto cifrado de arriba (cipher11), es el cual debemos descifrar
#Miremos su tamaño y comparemoslo con la clave, para ver si esta clave será capaz de desencriptar el texto entero, o le harán falta bits
if len(key) >= len(cipher11):
	print 'En este caso la llave servirá para descifrar el texto completo!'
else:
	print 'Se necesitará otro ataque de crib dragging a un texto cifrado de mayor tamaño...'
key = key.decode('hex')
cipher11 = cipher11.decode('hex')
res = strxor(cipher11,key)

print 'Mensaje a descifrar: '+res