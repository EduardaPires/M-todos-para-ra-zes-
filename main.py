import math as m 
import array as ary

n = 0;
a=0;
b=0; 

def expoent(c, expo):
  newc = 1
  for i in range(expo):
    newc = newc*c
  return newc
  
def function(vector, c):
  func = 0
  for i in range(n): #afinal o i chega ao n ou é menor que ele?
    func = func + expoent(c, n-1-i)*vector[i]
  return func;

def bissection(vector, a, b, tolerance):
  dif = b - a #depois adaptar para outros casos, por ex se b for menor que a
  # print(a, b, n)
  while (dif > (tolerance)):
    c = (a+b)/2
    if (function(vector, a)*function(vector, c)>0):
      a=c
      #print(c)
    elif (function(vector, b)*function(vector, c)>0):
      b=c
      #print(c)
    dif = b - a
  return a,b;
  
def fPosition():
  return 0;
  
def nRaphson():
  return 0;
  
def lIteration():
  return 0;

print("Sobre a função a qual vamos achar a raiz, me diga:\n")
n = int(input("Qual o grau da função?\n"))
n = n+1
vector = []
for i in range(n):
    ni = 0
    ni = int(input("Digite o número  da função: "))
    vector.append(ni)
a = float(input("Qual o A (menor número) do intervalo inicial?\n"))
b = float(input("E o B?\n"))
tolerance = float(input("Qual a tolerância? \n"))
tolerance = tolerance * 2;
#method = input("Qual método quer usar para calcular a raíz? (digite B para bisseção, F para falsa posição, N para newton-raphson e I para iteração linear.\n)")
method = "B" #ver como resolver problema do input
if (method=="B"):
  a,b=bissection(vector, a, b, tolerance)
elif (method == "F"):
  raiz = fPosition(vector)
elif (method == "N"):
  raiz = nRaphson(vector)
elif (method == "I"):
  raiz = lIteration(vector)
else:
  print("Letra não reconhecida.\n")
print("{:.2f}".format(a))
print("{:.2f}".format(b))