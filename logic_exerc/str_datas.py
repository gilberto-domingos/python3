'''
dentificar os participantes assíduos em todas as palestras e criar um conjunto geral de participação, utilizando estruturas de dados do tipo set em Python:
'''

palestra1 = {
    "Marley Beltran",
    "Allen Black",
    "Flynn Adams",
    "Ajay Copeland",
    "Keziah Shaw",
    "Junaid Hogan",
    "Leanne Fields",
}

palestra2 = {
    "Tara Blackwell",
    "Jared Salas",
    "Samira Sykes",
    "Junaid Hogan",
    "Leanne Fields",
}

palestra3 = {
    "Flynn Adams",
    "Ajay Copeland",
    "Keziah Shaw",
    "Leanne Fields",
    "Junaid Hogan",
}

# Participantes assíduos em todas as palestras
participantesAssiduos = palestra1 & palestra2 & palestra3

# Participação geral em todas as palestras
participacaoGeral = palestra1 | palestra2 | palestra3

# Ordenando participacaoGeral em ordem alfabética
participacaoOrdenada = sorted(participacaoGeral)

# Exibindo resultados
print("Pessoas que participaram de todas as palestras:")
for participante in participantesAssiduos:
    print(participante)

print("\nPresença geral:")
for participante in participacaoOrdenada:
    print(participante)
