class Jogador():
    def __init__(self, id_jogador = None, nome = None, data_nascimento = None, cpf = None, cep = None):
        self.id_jogador = id_jogador
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.cep = cep
        
    def validarCpf(cpf: str) -> bool:
        pass

    def validarCep(cep:str) -> bool:
        pass
    
    def to_dict(self):
        return {
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "cpf": self.cpf,
            "cep": self.cep
        }
        
    def convert_to_objetc(self, jogador: tuple):
        return Jogador(jogador[0], jogador[1], jogador[2], jogador[3], jogador[4])

class Torneio():
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano