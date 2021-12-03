#times campeonato brasileiro mostre os 5 primeiros colocados, os últimos 04 e em que posição está o Vasco

times = ('Flamengo', 'Internacional', 'Atlético - MG', 'São Paulo', 'Fluminense',
         'Grêmio', 'Palmeiras', 'Santos', 'Athletico - PR', 'Bragantino', 'Ceará SC',
         'Corinthians', 'Atlético - GO', 'Bahia', 'Sport Recife', 'Fortaleza',
         'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')

print(f'Os Primeiros 04 colocados são {times[:5]}')
print(f'Os últimos 04 colocados são {times[-4:]}')
print(f'Times em ordem alfabefica: {sorted(times)}')
print('O Vasco está na {} posicao'.format(times.index("Vasco da Gama")+1))
