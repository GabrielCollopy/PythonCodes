#importar a biblioteca
import mysql.connector as mysql

#criar(instanciar) o objeto de conexão
oConexao = mysql.connect(host = "127.0.0.1", # 127.0.0.1 = Endereço de localhost
                           user = "root",
                           passwd = "alunolab",
                           database = "banco")

#criar(instanciar) o objeto cursor 
oCursor = oConexao.cursor()

consulta = '''
DESCRIBE clientes;
'''

#Executar a consulta
#O metodo connect() executa o comando SQL (consulta)
oCursor.execute(consulta)

#O resultado da consulta é armazenado no cursor
for i in oCursor:
    print(i)

for i in oCursor.description:
    colunas = tuple(i[0])
colunas = tuple([i[0]] for i in oCursor.description)
print(colunas)

print(oCursor.description)
print(oCursor.rowcount)
#print (oCursor.fetchall())

#fecha o banco de dados
'''oConexao.close()'''