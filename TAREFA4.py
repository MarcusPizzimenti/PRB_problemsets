#!/usr/bin/env python3

#Questão 1

coisas_favoritas = ['Café','Formula1','Academia','Viajar','Amigos']  # Lista das coisas que eu gosto
print(coisas_favoritas)   # Imprime minha lista
print(coisas_favoritas[2]) # Imprime o elemento do meio da lista (lembrando que no python, o índice começa em 0)

coisas_favoritas[2] = 'Sabiá' # Troca o elemento do meio ("Academia") por "Sabiá"
print(coisas_favoritas) # Imprime a lista com a mudança do elemento do meio (lembre-se que listas são mutáveis)

#coisas_favoritas.append('Correr') # Adiciona um novo elemento ao final da lista ('Correr')
print(coisas_favoritas)
coisas_favoritas.insert(0,'Tênis') # Adiciona um novo elemento ao começo da lista ('Tênis')  
#print(coisas_favoritas)
coisas_favoritas.insert(3,'Frutas') # Insere um novo elemento a posição 3 da lista (lembrando que o índice começa em 0)
#print(coisas_favoritas)
coisas_favoritas.pop() # Remove o último elemento da lista 
#print(coisas_favoritas)

coisas_favoritas.remove('Tênis') # remove o elemento 'Tênis' da lista (começo da lista) 
#print(coisas_favoritas)
coisas_favoritas.pop(3) # Remove o elemento que está na posição 3 da lista
#print(coisas_favoritas)

coisas_favoritas_string = ", ".join(coisas_favoritas) # Cria uma string, juntando os elementos da lista, os quais são separados por uma vírgula
print(coisas_favoritas_string)

#Questão 2
taxa = "sapiens, erectus, neanderthalensis" # Cria a variável chamada 'taxa' 
print(taxa) # Imprime a variável 'taxa'
print(taxa[1]) # Imprime a posição 1 da variável taxa ('a', pois cada caracter é um elemento distinto)
print(type(taxa)) # O tipo de variável da 'taxa' é uma string (<class 'str'>)
split_taxa = taxa.split(', ') # Divide a variável taxa em plavras individuais
print(split_taxa)
species = split_taxa # Determina que a variável species é igual a variável split_taxa
print(species)
print(species[1]) #Imprime o elemento 1 da lista species, já que foi utilizado '.split', aparece "erectus"
print(type(species)) # O tipo de arquivo da variável species é uma lista
sorted_species = sorted(species) # Organiza a lista em ordem alfabética
print(sorted_species)
print(sorted(split_taxa, key=len)) # Organiza a lista pelo comprimento (lenght) de cada string

#Questão 3
# Método 1
my_list = ['a','bb','ccc']
list_copy = my_list # Ambas as listas foram alteradas porque apenas foi copiado um ponteiro para a lista original quando escreve-se copy_list=my_list, ou seja, não se criou uma cópia independente
print(my_list)
list_copy.append('dddd')
print(my_list)

# Método 2
my_list2 = ['a', 'bb', 'ccc']
list_copy2 = my_list2.copy() # Dessa forma, a lista 'list_copy2' é alterada, e a lista 'my_list2' não
print(my_list2)
list_copy2.append('dddd')
print(my_list2)

#Questão 4
contagem = 1  # Inicia a contagem a partir de 1     
while contagem <=100: # Condicional para o loop
  print(contagem) # Dentro do loop, imprime cada número desde que cumpra a condicional (números menores e iguais a 100)
  contagem+=1 # A contagem vai aumentando de 1 a 100, um número por um

#Questão 5
contagem = 1000  # Inicia a contagem a partir de 1000
fatorial = 1 # Inicia a multiplicação necessária na fatoração

while contagem > 0:  # Condicional para o loop  
    fatorial *= contagem # Realização da multiplicação associada a fatorar (3! = 3*2*1)
    contagem -= 1 # A contagem vai reduzindo de 1000 a 1, um número por um
print(fatorial) # Imprime o resultado final de 1000 fatorial

#Questão 6
numeros = [101,2,15,22,95,33,2,27,72,15,52]

for numero in iter(numeros):  # Iterador, passa de número a número na lista
    if numero % 2 == 0:   # Condicional para um número ser par: o resto da divisão deve ser 0
      print(numero) # Imprime os números que atingiram a condição supracitada

#Questão 7      
numeros = [101,2,15,22,95,33,2,27,72,15,52]
numeros_ordenados = sorted(numeros)  # Organiza de maneira crescente os números da lista

soma_par = 0  
soma_impar = 0   # Inicializa duas variávies (soma_par e soma_impar) com valor zero, estas representarão soma dos nº pares e ímpares

for numero in numeros_ordenados: 
    print(numero)
    if numero % 2 == 0:  # se o número for par, o resto da divisão será igual a 0
        soma_par += numero  # se o número for par (satisfaz a condição if), ele é adicionado a variável soma_par
    else:
        soma_impar += numero  # caso a condição if não seja atendida (número é ímpar), ele é adicionado a variável soma_impar 
print("Soma dos números pares:", soma_par, "\nSoma dos números ímpares:", soma_impar) #Imprime no formato string-variável soma, para as duas variáveis. '\n' indica uma quebra de linha

#Questão 8
for numero in range(0,100):  # para o numero que esteja entre 0 e 99; range(0,100) exclui 100
    print(numero)
for numero in range(1,101):  # para o numero que esteja entre 1 e 100, range(1,101) exclui 101
    print(numero)

#Questão 9
[print(numero) for numero in range(1,101)] # Usa compreensão de lista para imprimir todos os numeros de 1 a 100

#Questão 10
import sys # Importa o módulo sys, que dá acesso a variáveis e funções como sys.argv

começo = int(sys.argv[1]) # variável começo é convertida para numero inteiro, e é o primeiro argumento fornecido pelo usuário na linha de comando (lembre-se que sys.arv[0] se refere ao nome do arquivo do script)  

final = int(sys.argv[2]) + 1 # o segundo argumento da linha de comando (excluindo o sys.argv[0]) e o converte em um número inteiro. Em seguida, soma 1 a este valor. 

[print (num) for num in range(começo,final)] # imprime os números entre os numeros colocados na linha de comando (TAREFA4.py 3 5, irá imprimir 3 4 5)
[print (num) for num in range(começo,final) if num % 2 != 0] # faz o mesmo que a linha anterior mas adiciona uma condição: só será impresso os números que forem ímpares (resto da divisão por 2 diferente de 0)

#Questão 11
dna_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for dna in dna_list:    # inicia um loop que percorre cada elemento da lista dna_list
    comprimento_dna = len(dna) # para cada elemento, a função len() calcula o comprimento de nucleotídeos do dna 
    print(f"{comprimento_dna}\t{dna}") # Imprime a variável comprimento_dna e o respectivo elemento da lista, '\t' mostra uma tabulação entre estas duas impressões 

#Questão 12
dna_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

tupla_dna = [(len(dna),dna) for dna in dna_list]  # Gera um lista de tuplas em que cada tupla contém o comprimento da sequencia e a própria sequencia
print(tupla_dna)


#Questão 13
dna_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for indice in range(len(dna_list)): #range(len(dna_list)) cria um iterador que percorre todos os indices da lista; cada vez que loop roda, indice assume o valor de um número da sequência gerada por range(len(nt_list)), sendo o indice atual da lista
    print(f"{indice + 1}\t{len(dna_list[indice])}\t{dna_list[indice]}") # imprime o número da posição, o comprimento da sequência e a sequência, todos separados por tabulação, usando formatação de string.  
