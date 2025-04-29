from peewee import *

meu_bd = SqliteDatabase("meus_dados.db")

class Database(Model):
    class Meta:
        database = meu_bd

class Cliente(Database):
    nome = CharField()
    telefone = CharField()
    endereco = CharField()

    def __str__(self):
        return f"Nome: {self.nome} \ Telefone: {self.telefone} \ Endereço: {self.endereco}"

class Filme(Database):
    diretor = CharField()
    duracao_minutos = IntegerField()
    titulo = CharField()
    ano_lancamento = CharField()

class Locacao(Database):
    cliente = ForeignKeyField(Cliente)
    filme = ForeignKeyField(Filme)
    dt_locacao = DateTimeField()
    dt_devolucao = DateTimeField()
    valor = DecimalField()


# Depois de criar todas as suas classes
# Vamos criar o banco de dados e as tabelas
meu_bd.connect()
meu_bd.create_tables([Cliente, Filme, Locacao])