##Elaborando a prova pratica 06 de python P00
##Nome : Rafael Augusto        RA: 22508717

class Animal:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    # --- GETS ---
    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

    # --- SETS ---
    def set_nome(self, nome):
        if len(nome.strip()) == 0:
            print("Erro: o nome não pode ser vazio.")
        else:
            self._nome = nome

    def set_idade(self, idade):
        if idade < 0:
            print("Erro: a idade não pode ser negativa.")
        else:
            self._idade = idade

    # --- MÉTODOS ÚTEIS COMUNS ---
    def emitir_som(self):
        print(f"{self._nome} está emitindo um som genérico.")

    def envelhecer(self):
        self._idade += 1
        print(f"{self._nome} agora tem {self._idade} anos.")


# -----------------------------------------------------------
# Subclasse 1
class Mamifero(Animal):
    def __init__(self, nome, idade, especie, habitat, possui_pelos=True):
        super().__init__(nome, idade)
        self._especie = especie
        self._habitat = habitat
        self._possui_pelos = possui_pelos

    # --- GETS ---
    def get_especie(self):
        return self._especie

    def get_habitat(self):
        return self._habitat

    def get_possui_pelos(self):
        return self._possui_pelos

    # --- SETS ---
    def set_especie(self, especie):
        self._especie = especie

    def set_habitat(self, habitat):
        self._habitat = habitat

    def set_possui_pelos(self, possui_pelos):
        if not isinstance(possui_pelos, bool):
            print("Erro: o atributo 'possui_pelos' deve ser True ou False.")
        else:
            self._possui_pelos = possui_pelos

    # --- MÉTODO PRÓPRIO ---
    def amamentar(self):
        print(f"O mamífero {self._nome} está amamentando seus filhotes.")


# -----------------------------------------------------------
# Subclasse 2
class Ave(Animal):
    def __init__(self, nome, idade, especie, cor_das_penas, pode_voar=True):
        super().__init__(nome, idade)
        self._especie = especie
        self._cor_das_penas = cor_das_penas
        self._pode_voar = pode_voar

    # --- GETS ---
    def get_especie(self):
        return self._especie

    def get_cor_das_penas(self):
        return self._cor_das_penas

    def get_pode_voar(self):
        return self._pode_voar

    # --- SETS ---
    def set_especie(self, especie):
        self._especie = especie

    def set_cor_das_penas(self, cor):
        if len(cor.strip()) == 0:
            print("Erro: a cor das penas não pode ser vazia.")
        else:
            self._cor_das_penas = cor

    def set_pode_voar(self, pode_voar):
        if not isinstance(pode_voar, bool):
            print("Erro: o atributo 'pode_voar' deve ser True ou False.")
        else:
            self._pode_voar = pode_voar

    # --- MÉTODO PRÓPRIO ---
    def cantar(self):
        print(f"A ave {self._nome} está cantando alegremente.")
