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
contagem = 1
while contagem <=100:
  print(contagem)
  contagem+=1

#Questão 5
contagem = 1000
fatorial = 1

while contagem > 0:
    fatorial *= contagem
    contagem -= 1
print(fatorial)

#Questão 6
