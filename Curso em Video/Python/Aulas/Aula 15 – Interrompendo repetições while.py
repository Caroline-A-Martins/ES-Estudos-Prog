n = s = 0
while True:  # Faz com que o codigo funcione infinitamente, só pode ser parado com o break
    n = int(input('Digite um número: '))
    print(n)
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
