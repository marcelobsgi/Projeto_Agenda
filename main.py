import sqlite3, time
conectar =sqlite3.connect(r'C:\Mus projetos\Projeto Agenda\banco\agenda.db')
c = conectar.cursor()

def criar_db():
    c.execute("CREATE TABLE IF NOT EXISTS cadastro(Nome text, Telefone varchar, Email text, Data text)")


try:
    criar_db()
except:
    print('Erro ao criar banco de dados')
else:
    print('Banco de dados criado com sucesso.')


def inserir(n, t, e):
    d =time.strftime('%d/%m/%Y')
    c.execute ('INSERT INTO cadastro VALUES(?, ?, ?, ?)', (n, t, e, d))
    conectar.commit()


def pesquisar(p):
    sql = 'SELECT * FROM cadastro WHERE NOME = ?'
    for row in c.execute(sql, (p,)):
        print(row)


fc = int(input(' Selecione uma opção: 1 - Cadastrar \n 2 - Pesquisar :'))

if fc == 1:

    try:
        print('Cadastro de Agenda.')
        time.sleep(2)
        n = str(input(' Informe seu nome: '))
        t = str(input(' Informe seu telefone: '))
        e = str(input(' Informe seu email: '))
        inserir(n, t, e)

    except:
        print('Erro ao efetuar o cadastro')

    else:
        print('Cadasstro realizado')


elif fc == 2:
    print('aguarde um momento')
    time.sleep(2)
    p = str(input('Informe '))
    pesquisar(p)


else:
    print('opção invalida')



print(input('Aperte a tecla ENTER para finalizar.'))

#para criar o executável no terminal
    #pip install auto-py-to-exe
#em seguida digite o comando
    #auto-py-to-exe
    #ou
    #python -m auto_py_to_exe