#leia o preco de um produto e mostre o seu novo preço com 5% de desconto

num = float(input('Digite o preço: R$ '))

pricenew = num*0.95
difprice = num-pricenew

print('O novo preço é R$ {:.2f}. Você economizou R$ {:.2f}.'.format(pricenew, difprice))
