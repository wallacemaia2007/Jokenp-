palavras=('geovanna','santos','martins','Amor','da','minha','vida','eu','te','amo','muitao')
for p in palavras:
    print(f'\nA palavra {p} tem as vogais: ',)
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')