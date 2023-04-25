import math
import cmath
n=0
a=0
b=0
n2=0
#atualizar no github

# def findRootofNumber(c, root): #num que quero fazer a raiz e raiz; ex: 36=c, root=2
#   division=0
#   indice=c #36
#   answer=1
#   while(c!=1):
#       repetition=0
#       for i in range(indice): #0
#           if (i>1):
#               while (c%i == 0): #ver como é o && de python
#                   c = c/i #18/9/3/1
#                   division=i #armazena valor que c dividio por ele n sobra nada #2/3/3
#                   repetition = repetition+1 #1/2/1/2
#                   if (repetition == root):
#                       answer = answer*division #2/3; 2*3=6
#                       repetition=0
#                       break
#   return answer

# def calculatephiX(vectorphi, x):
#   nexpo = n-1
#   vectorphi.remove[0] #ver se é assim
#   phiX = findRootofNumber(function(vectorphi, x, nexpo), nexpo) #c é o num que vou calcular do momento
#   return phiX

def calculatephiX(vectorphi, x):
  #vectorphi.remove[0]
  nexpo = n-1
  x = function(vectorphi, x, nexpo)
  x = x - expoent(x, n-1)*vectorphi[0]
  x = x ** (1/(nexpo-1))
  return x
  
def expoent(c, expo):
  newc = 1
  for i in range(expo):
    newc = newc*c
  return newc
  
def function(vector, c, num):
  func = 0
  for i in range(num): #afinal o i chega ao n ou é menor que ele?
    func = func + expoent(c, n-1-i)*vector[i]
  return func

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
  c = (a+b)/2 #divide por 2, não? ****************
  while (dif > (tolerance)):
    c = c - (function(vector, c, n)/function(derivative, c, n2))
    if (function(vector, a, n)*function(vector, c, n)>0):
      a=c
    elif (function(vector, b, n)*function(vector, c, n)>0):
      b=c
    dif = b - a
  return a,b;
  
# def lIteration(vector, a, b, tolerance):
#   dif = b - a #
#   c = (a+b)/2
#   x = function(vector, c, n)  #calcula ja pra saber se ja encaixa, aí n precisa entrar no while
#   if (x<0):
#     x = x * -1
#   vectorphi = vector
#   while (x > tolerance): #fica enquanto x, o resultado da função apos calcula o phix, é maior q a tolerancia
#     c = calculatephiX(vectorphi, c) #é sempre o mesmo phi, só o x inserido nele q vai mudar
#     x = function(vector, c, n)
#     if (x<0):
#       x = x * -1
#     if (x>tolerance):
#       c=x
#   a = c+tolerance #ver se da certo e como se ve os intervalos no metodo em si, e n a raiz
#   b = c-tolerance
#   return a,b
  # while (dif > (tolerance)):
  #   c = calculatephiX(vector, c)
  #   if (function(vector, a, n)*function(vector, c, n)>0):
  #     a=c
  #   elif (function(vector, b, n)*function(vector, c, n)>0):
  #     b=c
  #   dif = b - a
  # return a,b;

def lIteration():
  #caso fixo pois n consegui fazer pro geral
  x = -1
  i =0
  tolerance = 0.00001
  iterarions = 100
  while math.fabs(math.pow(x, 2) - math.exp(x)) > tolerance:
    xk = -math.sqrt(math.exp(x))
    x = xk
    i = i+1
    if (i>= iterarions):
      break
  a = x+tolerance
  b = x-tolerance
  print("Caso fixo:\n")
  print(f"Tolerância definida: {0.00001}")
  print(f"Iterações máximas: {iterarions}")
  print(f"Iterações feitas: {i}")
  return a,b    

# def lIteration(vector, a, b, tolerance):
#   #caso fixo pois n consegui fazer pro geral
#   x = (a+b)/2
#   vectorphi = vector
#   func = function(vector, x, n)
#   if (func.real < 0.0):
#     func = func * -1
#   while math.fabs(func) > tolerance:
#     # xk = -math.sqrt(math.exp(x))
#     xk = calculatephiX(vectorphi, x)
#     x = xk
#     func = function(vector, x, n)
#     if (func.real < 0.0):
#       func = func * -1
#   a = x+tolerance
#   b = x-tolerance
#   return a,b    

def createFunction(num):
  array = []
  for i in range(num):
      ni = 0
      ni = int(input("Digite o número  da função: "))
      array.append(ni)
  return array;

method = input("Qual método quer usar para calcular a raíz? (digite B para bisseção, F para falsa posição, N para newton-raphson e I para iteração linear.\n)")
if (method != "I"):
  print("Agora sobre a função a qual vamos achar a raiz, me diga:\n")
  n = int(input("Qual o grau da função?\n"))
  n = n+1
  vector = createFunction(n)
  a = float(input("Qual o A (menor número) do intervalo inicial?\n"))
  b = float(input("E o B?\n"))
  tolerance = float(input("Qual a tolerância? \n"))
  tolerance = tolerance * 2;
  if (method=="B"): #certo
    a,b= bissection(vector, a, b, tolerance)
  elif (method == "F"): #arrumar pois há casos em que ambos os intervalos são o mesmo num (talvez esteja associado ao arrdedonandamento, se sim fazer if pra esse caso); pelo menos o resultado ta correto
    a,b = fPosition(vector, a, b, tolerance)
  elif (method == "N"): #ver se faz além da função normal o input da deriva pra esse caso #certo
    print("Agora informe sobre a derivada: ")
    n2 = int(input("Qual o grau da função?\n"))
    n2 = n2+1
    derivative = createFunction(n2)
    a,b = nRaphson(vector, derivative, a, b, tolerance) #rever algoritmo!!!
  else:
    print("Letra não reconhecida.\n")
else:
    # elif (method == "I"): #dando errado (debug e analise do metodo em si, calculos de c, ver video)
  a,b = lIteration()
print("{:.5f}".format(a)) #arrendondamento ou concatenação? ver se faço op
print("{:.5f}".format(b)) #obs: observar casos em que o int pode acabar sendo a raiz, para deixar exatamente um intervalo em que ela esteja no MEIO
#ver outras funções 
#rever F (if prov ajuda), N (caso de a ou b dar raiz), e I (ta bem longe, debugar e rever metodo) **********
#lembrar de sincronizar e entregar no classroom