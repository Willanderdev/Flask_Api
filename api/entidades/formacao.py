class Formacao():
    def __init__(self, nome, descricao, professores):
        self.__nome = nome
        self.__descricao = descricao
        self.__professores = professores


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def professores(self):
        return self.__professores

    @professores.setter
    def professores(self, professores):
        self.__professores = professores



    