# Importação do conteúdo do framework PeeWee
# Tipos de campo, Model, conexão com sqlite, etc
from peewee import *

# Importar bibliotecas de data e hora para preencher automaticamente
from datetime import datetime 

# Iniciar a conexão com o seu arquivo de banco de dados
meu_bd = SqliteDatabase("meus_dados.db")

class MinhaBase(Model):
    class Meta:
        database = meu_bd

class Estudante(MinhaBase):
    nome = CharField()
    matricula = CharField(unique=True)
    curso = CharField(default="Técnico em Informática")

    def __str__(self):
        return self.nome

class TipoProtocolo(MinhaBase):
    nome = CharField()

    def __str__(self):
        return self.nome

class Protocolo(MinhaBase):
    estudante = ForeignKeyField(Estudante)
    justificativa = CharField()
    data_hora = DateTimeField(default=datetime.now)
    tipo = ForeignKeyField(TipoProtocolo)

    def __str__(self):
        return f"Procolo: {self.id} - {self.estudante.nome}"

# Depois de criar as classes, conecta no banco de dados
meu_bd.connect()

# Cria as tabelas para as classes, caso não existam
meu_bd.create_tables([Estudante, TipoProtocolo, Protocolo])

