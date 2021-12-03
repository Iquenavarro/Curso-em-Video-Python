#mostre os primeiros elementos da sequencia de fibonacci

user = int(input('Quantos numeros da sequencia de Fibonacci deseja mostrar: fn = '))

prevfn = 0
fn = 1
nextfn = 0
index = 0

while index < user:
    prevfn = fn
    fn = nextfn
    nextfn = (fn + (prevfn))
    print('f{} = {}'.format(index, fn))
    index += 1
print('Fim')