class Pessoa: # Inici
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.genero = ""
        def __eq__(self, pessoa):
            if(type(self) != type(pessoa)):
                return False
            return ((self.nome == pessoa.nome) and (self.idade == pessoa.idade) and (self.genero == pessoa.genero))
        def __nq__(self, pessoa):
            return (not self == pessoa)
pessoa1 = Pessoa()
pessoa2 = Pessoa()
print(pessoa1 == pessoa2)
print(pessoa1 != pessoa2)