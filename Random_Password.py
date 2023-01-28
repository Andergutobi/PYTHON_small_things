from random import SystemRandom
  
l = int(input("Cuantos caracteres necesitas?"))

Caracteres = "0123456789:;'#)(][}{><-+-/^%$_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
  
aleatorio = SystemRandom() 

p = " " 

while l > 0: 
 p = p + aleatorio.choice(Caracteres) 
 l=l-1 
  
print("Tu contraseña segura es:",p)
