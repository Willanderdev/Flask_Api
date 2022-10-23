class Usuario():
    def __init__(self, nome, email, senha, is_admin):
        self.__nome = nome
        self.email = email
        self.senha = senha
        self.__is_admin = is_admin

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email


    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        self.__is_admin = is_admin

