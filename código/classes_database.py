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
        return f"[nº registro: {self.id}] nome: {self.nome} | telefone: {self.telefone} | endereco: {self.endereco}"

class Filme(Database):
    diretor = CharField()
    duracao_minutos = IntegerField()
    titulo = CharField()
    ano_lancamento = CharField()

    def __str__(self):
        return f"título: {self.titulo} | ano: {self.ano_lancamento} | duração: {self.duracao_minutos}"

class Locacao(Database):
    cliente = ForeignKeyField(Cliente)
    filme = ForeignKeyField(Filme)
    dt_locacao = DateTimeField()
    dt_devolucao = DateTimeField()
    valor = DecimalField()
    devolvido=BooleanField(default=False)
    def __str__(self):

        msg = f"""
        ======== REGISTRO DE LOCAÇÃO ========
        Ocorreu nesta data  '{self.dt_locacao}'  uma locação do filme
        
        :: {self.filme}
        :: para o cliente:  {self.cliente},
        
        com um prazo de 14 dias para devolução.
        Se o filme não for devolvido até {self.dt_devolucao} o cliente deverá ser multado em {(self.valor*2)} R$."""

        return msg


# Depois de criar todas as suas classes
# Vamos criar o banco de dados e as tabelas
meu_bd.connect()
meu_bd.create_tables([Cliente, Filme, Locacao])