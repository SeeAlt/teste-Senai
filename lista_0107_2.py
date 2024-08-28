class Pessoa: # Inicializando
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.genero = ""
def inicialize_pessoa(pessoa):
    pessoa.nome = "Franco"
    pessoa.idade = 1234
    pessoa.genero = "Masculino"
Franco = Pessoa() # inserção de dados
Franco.nome = "Franco"
Franco.idade = 1234
Franco.genero = "Masculino"
# Fim inserção de dados
print(Franco) # Imprimindo dados
print(Franco.nome)
print(Franco.idade)
print(Franco.genero)
inicialize_pessoa(Franco)
print(Franco) # Imprimindo dados
print(Franco.nome)
print(Franco.idade)
print(Franco.genero)
# Fim impressão de dados