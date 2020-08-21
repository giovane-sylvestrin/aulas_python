"""
19)

Escreva um programa que acha os anagramas em uma lista de palavras (duas palavras são anagramas
se uma palavra pode ser formada rearranjando as letras de outra)

    anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
    [['eat', 'ate', 'tea], ['done', 'node'], ['soup']]
"""
anagrams = ['eat', 'ate', 'done', 'tea', 'soup', 'node']

print(len(anagrams))
word = list(range(len(anagrams)))

for i in range(len(anagrams)):
    word[i] = list(anagrams[i])

print(word[3])

print(len(word[0]))

for i in range(len(word)):
    for j in range(len(word)):
        if j != i:
            if len(word[i]) == len(word[j]):
                cont = 0
                #print(f'{i} e {j}')
                for k in range(len(word[i])):
                    for w in range(len(word[i])):
                        if word[i][k] == word[j][w]:
                            cont += 1
                #print(cont)
                if cont == len(word[i]):
                    print(f'{anagrams[i]} e {anagrams[j]} são anagramas')




