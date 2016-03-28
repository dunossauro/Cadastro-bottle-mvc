#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -------------- Imports
import sqlite3

# -------------- Criação da tabela
def c_table():
	con = sqlite3.connect('base_usuarios.db')
	cur = con.cursor()
	cur.execute('CREATE TABLE IF NOT EXISTS USUARIOS(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME TEXT NOT NULL, EMAIL TEXT NOT NULL);')

# ------------- Classe para interagir com os outros projetos
class Base:
	def __init__(self):

		# -------------- Cursor do banco
		self.con = sqlite3.connect('base_usuarios.db')
		self.cur = self.con.cursor()

        # -------------- Select
		self.select = 'SELECT ID,NOME,EMAIL FROM USUARIOS'

        # -------------- Insert
		self.insert = 'INSERT INTO USUARIOS (NOME, EMAIL) VALUES (?, ?)'


	def busca(self):
		self.cur.execute(self.select)
		return self.cur.fetchall()

    # -------------- Método que faz inserção no banco
	def inserir_dados(self, nome, email):
		self.cur.execute(self.insert, (nome, email))

	def commit(self):
		self.con.commit()

c_table()
