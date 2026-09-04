n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
n3 = float(input('terceira nota: '))
media = (n1 + n2 +n3) / 3
print(f'media: {media:.2f}')
if media >= 7:
    print('aprovado')
elif media >= 5:
    print('recuperaao!')
else: 
    print('reprovado')