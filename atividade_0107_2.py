palavras = ["python", "asimov", "código", "web", "progamação"]
maior_palavra = palavras[0]
menor_palavra = palavras[0]
for palavra in palavras:
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra
    if len(palavra) < len(menor_palavra):
        menor_palavra = palavra
print("A maior palavara é:", maior_palavra)
print("A menor palavra é:", menor_palavra)
