n=0
a=0
b=0
n2=0

def expoent(c, expo):
  newc = 1
  for i in range(expo):
    newc = newc*c
  return newc
  
def function(vector, c, num):
  func = 0
  for i in range(num): #afinal o i chega ao n ou é menor que ele?
    func = func + expoent(c, n-1-i)*vector[i]
  return func;

def bissection(vector, a, b, tolerance):
  dif = b - a #depois adaptar para outros casos, por ex se b for menor que a
  # print(a, b, n)
  while (dif > (tolerance)):
    c = (a+b)/2
    if (function(vector, a, n)*function(vector, c, n)>0):
      a=c
      #print(c)
    elif (function(vector, b, n)*function(vector, c, n)>0):
      b=c
      #print(c)
    dif = b - a
  return a,b;
  
def fPosition(vector, a, b, tolerance):
  dif = b - a #depois adaptar para outros casos, por ex se b for menor que a
  # print(a, b, n)
  while (dif > (tolerance)):
    c = (a*function(vector, b, n)-(b*function(vector, a, n)))/(function(vector, b, n)-function(vector, a, n))
    if (function(vector, a, n)*function(vector, c, n)>0):
      a=c
      #print(c)
    elif (function(vector, b, n)*function(vector, c, n)>0):
      b=c
      #print(c)
    dif = b - a
  return a,b;
  
def nRaphson(vector, derivative, a, b, tolerance):
  dif = b - a 
  c = (a+b)/a
  while (dif > (tolerance)):
    c = c - (function(vector, c, n)/function(derivative, c, n2))
    if (function(vector, a, n)*function(vector, c, n)>0):
      a=c
      print("caso a")
    elif (function(vector, b, n)*function(vector, c, n)>0):
      b=c
      print("caso b")
    dif = b - a
  return a,b;
  
def lIteration():
  return 0;

def createFunction(num):
  array = []
  for i in range(num):
      ni = 0
      ni = int(input("Digite o número  da função: "))
      array.append(ni)
  return array;

print("Sobre a função a qual vamos achar a raiz, me diga:\n")
n = int(input("Qual o grau da função?\n"))
n = n+1
vector = createFunction(n)
a = float(input("Qual o A (menor número) do intervalo inicial?\n"))
b = float(input("E o B?\n"))
tolerance = float(input("Qual a tolerância? \n"))
tolerance = tolerance * 2;
#method = input("Qual método quer usar para calcular a raíz? (digite B para bisseção, F para falsa posição, N para newton-raphson e I para iteração linear.\n)")
#method = "B" #ver como resolver problema do input
#method = "F"
method = "N"
#method = "I"
if (method=="B"):
  a,b= bissection(vector, a, b, tolerance)
elif (method == "F"):
  a,b = fPosition(vector, a, b, tolerance)
elif (method == "N"): #ver se faz além da função normal o input da deriva pra esse caso
  print("Agora informe sobre a derivada: ")
  n2 = int(input("Qual o grau da função?\n"))
  n2 = n2+1
  derivative = createFunction(n2)
  a,b = nRaphson(vector, derivative, a, b, tolerance) #rever algoritmo!!!
elif (method == "I"): #ver como fazer se n tiver o x
  a,b = lIteration(vector, a, b, tolerance)
else:
  print("Letra não reconhecida.\n")
  
print("{:.2f}".format(a)) #arrendondamento ou concatenação? ver se faço op
print("{:.2f}".format(b))