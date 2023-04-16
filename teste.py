  
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

n = 0; 

print("Sobre a função a qual vamos achar a raiz, me diga:\n")
n = int(input("Qual o grau da função?\n"))
vector = []
for i in range(n):
    ni = 0
    ni = int(input("Digite o número da função: "))
    vector.append(ni)
print(function(vector, 1))

