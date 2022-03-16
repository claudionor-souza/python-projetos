from time import sleep
print('>' * 30)
print('{:^30}'.format('CONSUMO DE COMBUSTIVEL '))
print('<' * 30)
print(''' ESCOLHA UM COMBUSTIVEL:
[1]Etanol
[2]Gasolina
[3]Diesel''')
sleep(2)
opcao = int(input('Opção: '))
resposta = opcao
sleep(2)
if resposta == 1:
    print(f'[1]Etranol')
elif resposta == 2:
    print('[2]Gasolina')
else:
    print(f'Diesel')
combustivel = float(input('Preço/litro (R$): '))
km_litro = float(input('Km / L: '))
km_inicial = float(input('Km origem: '))
km_percorrido = float(input('Km percorrido: '))
km_destino = km_percorrido + km_inicial - km_inicial
km_atual = km_inicial + km_percorrido
valor_km = combustivel / km_litro
custo_total = combustivel / km_litro * km_percorrido
print(f'Percurso total: {km_destino}')
print(f'Km atual: {km_atual}')
print(f'Valor por km: {valor_km:.2f}')
print(f'Custo total do abastecimento: R${custo_total:.2f}')
