class Curso():
    def __init__(self, nome, descricao, data_publicacao, formacao):
        self.__nome = nome
        self.__descricao = descricao
        self.__data_publicacao = data_publicacao
        self.__formacao = formacao

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
    def data_publicacao(self):
        return self.__data_publicacao

    @data_publicacao.setter
    def data_publicacao(self, data_publicacao):
        self.__data_publicacao = data_publicacao

    @property
    def formacao(self):
        return self.__formacao

    @formacao.setter
    def formacao(self, formacao):
        self.__formacao = formacao
