class Pessoa: # Inicializando
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.genero = ""
# Fim inicialização
Franco = Pessoa() # inserção de dados
Franco.nome = "Franco"
Franco.idade = 1234
Franco.genero = "Masculino"
# Fim inserção de dados
print(Franco) # Imprimindo dados
print(Franco.nome)
print(Franco.idade)
print(Franco.genero)
# Fim impressão de dados