from random import SystemRandom
  
l = int(input("Cuantos caracteres necesitas?"))

mi = "abcdefghijklmnopqrstuvwxyz"
ma = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
sim = ":;'#)(][}{><-+-/^%$_"
  
aleatorio = SystemRandom() 

p = " " 

while l > 0: 
 p = p + aleatorio.choice(mi+num+ma+sim)
 l=l-1 
  
print("Tu contraseña segura es:",p)
