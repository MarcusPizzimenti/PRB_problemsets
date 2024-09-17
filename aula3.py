#!/usr/bin/env python3
# Sequência original
dna_primario = "5'ATGCAGGGGAAACATGATTCAGGAC3'"

# Remove as marcações de extremidade (5' e 3') para processar a sequência
dna_sem_limites = dna_primario[2:-2]

# Cria uma tabela de tradução para múltiplas substituições
tabela = str.maketrans('ATGC','TACG')
# Aplica a tradução usando a tabela
complemento = dna_sem_limites.translate(tabela)

# Adiciona as marcações de extremidade novamente
complemento_atualizado = f"3' {complemento} 5'"

# Imprime o complemento
print(complemento_atualizado)

# Complemento reverso sem marcações
complemento_rev = complemento[::-1]

# Complemento reverso sem marcações
complemento_rev_marc = f"5' {complemento_rev} 3'"
print(complemento_rev_marc)
