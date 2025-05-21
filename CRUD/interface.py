from tkinter import *
from crud.create_products import criar_produto
from crud.list_products import listar_produtos
from crud.update_products import atualizar_produtos
from crud.delete_products import deletar_produtos

def interface():
    window = Tk()
    window.title('Gerenciamento de Estoque')
    window.geometry('300x300')

    content = Frame(window)
    content.grid()

    def main_interface():
        for conteudo in content.winfo_children():
            conteudo.destroy()
    
        Label(content, text='Selecione a opção desejada').grid(column=0, row=0, padx=70, pady=10)
        Button(content, text='Criar Produtos', command=create_interface).grid(column=0, row=1, padx=70, pady=10)
        Button(content, text='Listar Produtos', command=list_interface).grid(column=0, row=2, padx=70, pady=10)
        Button(content, text='Atualizar Produtos', command=update_interface).grid(column=0, row=3, padx=70, pady=10)
        Button(content, text='Deletar Produtos', command=delete_interface).grid(column=0, row=4, padx=70, pady=10)
        

    def create_interface():
        for conteudo in content.winfo_children():
            conteudo.destroy()

        Label(content, text='Nome do Produto').grid(column=0, row=0)
        nome_entry = Entry(content)
        nome_entry.grid(column=1, row=0)

        Label(content, text='Valor').grid(column=0, row=1)
        valor_entry = Entry(content)
        valor_entry.grid(column=1, row=1)

        def criar():
            nome = nome_entry.get()
            valor = valor_entry.get()
            criar_produto(nome, valor)
            main_interface()


        Button(content, text='Criar', command=criar).grid(column=0, row=2, padx=50, pady=10)
        Button(content, text='Voltar', command=main_interface).grid(column=1, row=2, padx=50, pady=10)

    def list_interface():
        for conteudo in content.winfo_children():
            conteudo.destroy()

        produtos = listar_produtos()

        Label(content, text="Produtos Cadastrados:").grid(column=0, row=0, padx=85, pady=10)

        for i, produto in enumerate(produtos):
            Label(content, text=(produto)).grid(column=0, row=i+1)

        Button(content, text='Voltar', command=main_interface).grid(column=0, row=len(produtos)+2, columnspan=2, padx=50, pady=10)

    def update_interface():
        
        for conteudo in content.winfo_children():
            conteudo.destroy()


        Label(content, text="Novo Nome").grid(column=0, row=0)
        new_name_entry = Entry(content)
        new_name_entry.grid(column=1, row=0)

        Label(content, text="Novo Valor").grid(column=0, row=1)
        new_value_entry = Entry(content)
        new_value_entry.grid(column=1, row=1)

        Label(content, text="ID do Produto").grid(column=0, row=2)
        id_entry = Entry(content)
        id_entry.grid(column=1, row=2)

        def atualizar():
            new_name = new_name_entry.get()
            new_value = new_value_entry.get()
            id_product = id_entry.get()

            atualizar_produtos(new_name,  new_value, id_product)   
            main_interface()

        Button(content, text='Atualizar Produto', command=atualizar).grid(column=0, row=3, pady=10, padx=25)
        Button(content, text='Voltar', command=main_interface).grid(column=1, row=3, pady=10, padx=25)

    def delete_interface():
        
        for conteudo in content.winfo_children():
            conteudo.destroy()  

        Label(content, text='Nome do Produto').grid(column=0, row=0, pady=10, padx=10)
        nome_entry = Entry(content)
        nome_entry.grid(column=1, row=0, pady=10, padx=10) 

        def deletar():
            nome = nome_entry.get()
            deletar_produtos([nome])
            main_interface()


        Button(content, text='Deletar Produto', command=deletar).grid(column=0, row=2, pady=10, padx=25)
        Button(content, text='Voltar', command=main_interface).grid(column=1, row=2, pady=10, padx=25)  
        
    main_interface()
    window.mainloop()

interface()