import tkinter as tk
import mysql.connector

root = tk.Tk()
root.title("Cadastro de Clientes")
root.geometry("350x400")

def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()
    cpf = entry_cpf.get()
    endereco = entry_endereco.get()
    cidade = entry_cidade.get()
    estado = entry_estado.get()
    print(nome, email, senha, cpf, endereco, cidade, estado)

    conectar = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="db_teste"
    )
    cursor = conectar.cursor()
    insert = f"INSERT INTO cliente (nome, email, senha, cpf, endereco, cidade, estado) VALUES ('{
        nome}', '{email}', '{senha}', '{cpf}', '{endereco}', '{cidade}', '{estado}')"

    try:
        cursor.execute(insert)
        conectar.commit()
        print("Cliente cadastrado")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        cursor.close()
        conectar.close()


# AQUI COMEÇA OS WIDGETS
root.columnconfigure(1, minsize=10)

fonte_titulo = ("Arial", 16, "bold")
label_espaco = tk.Label(root, text="Cadastro", font=fonte_titulo)
label_espaco.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="n")

label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_nome = tk.Entry(root)
entry_nome.grid(row=1, column=1, padx=10, pady=5)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=5, sticky="e")

entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=5)

label_senha = tk.Label(root, text="Senha:")
label_senha.grid(row=3, column=0, padx=10, pady=5, sticky="e")

entry_senha = tk.Entry(root)
entry_senha.grid(row=3, column=1, padx=10, pady=5)

label_cpf = tk.Label(root, text="CPF:")
label_cpf.grid(row=4, column=0, padx=10, pady=5, sticky="e")

entry_cpf = tk.Entry(root)
entry_cpf.grid(row=4, column=1, padx=10, pady=5)

label_endereco = tk.Label(root, text="Endereço:")
label_endereco.grid(row=5, column=0, padx=10, pady=5, sticky="e")

entry_endereco = tk.Entry(root)
entry_endereco.grid(row=5, column=1, padx=10, pady=5)

label_cidade = tk.Label(root, text="Cidade:")
label_cidade.grid(row=6, column=0, padx=10, pady=5, sticky="e")

entry_cidade = tk.Entry(root)
entry_cidade.grid(row=6, column=1, padx=10, pady=5)

label_estado = tk.Label(root, text="Estado:")
label_estado.grid(row=7, column=0, padx=10, pady=5, sticky="e")

entry_estado = tk.Entry(root)
entry_estado.grid(row=7, column=1, padx=10, pady=5)

button_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar)
button_cadastrar.grid(row=8, column=0, columnspan=2, pady=10)
# AQUI TERMINA OS WIDGETS

root.mainloop()
