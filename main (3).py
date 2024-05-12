def ExA(n):
  if n == 1:
      return 10
  else:
      return ExA(n - 1) + 10

resultado = ExA(5)
print(resultado)
