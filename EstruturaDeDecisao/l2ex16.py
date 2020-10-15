''' 16) Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
-> Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
-> Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
-> Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; '''

a = int(input("Informe a: "))
b = int(input("Informe b: "))
c = int(input("Informe c: "))

if a != 0:
  if b == 0:
    x1 = (-c/a)**(1/2)
    x2 = -(-c/a)**(1/2) 
    print("x1:",x1)
    print("x2:",x2)
  elif c == 0:
    x1 = 0
    x2 = -b / a
    print("x1:",x1)
    print("x2:",x2)
  else:
    delta = b**2 -(4*a*c)
    if delta < 0:
      print("A equação não possui raízes reais.")
    elif delta == 0:
      x = ((-b + delta**(1/2)) / (2*a))
      print("\nA equação possui apenas uma raiz real\nx:",x)
    else:
      print()
      x1 = ((-b + delta**(1/2)) / (2*a))
      x2 = ((-b - delta**(1/2)) / (2*a))
      print("\nA equação possui duas raízes reais\nx1:", x1, "x2:", x2)
else:
  print("A equação não é do segundo grau")