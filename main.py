import customtkinter 
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_contacao_moeda

customtkinter.set_appearance_mode("system")  
customtkinter.set_default_color_theme("green")

# Criação do frame
janela = customtkinter.CTk()
janela.geometry("500x500")
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas",font=("Arial",35))
titulo.pack(padx=10, pady=20)

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])

dic_conversoes_disponiveis = conversoes_disponiveis()

# Frame para agrupar seleção de moedas
frame_selecao = customtkinter.CTkFrame(janela)
frame_selecao.pack(pady=10)

# Moeda de Origem (coluna 0)
texto_moeda_origem = customtkinter.CTkLabel(frame_selecao, text="Moeda de Origem:", font=("Arial", 14))
texto_moeda_origem.grid(row=0, column=0, padx=10, pady=5)
campo_moeda_origem = customtkinter.CTkOptionMenu(
    frame_selecao, 
    values=list(dic_conversoes_disponiveis.keys()),
    command=carregar_moedas_destino
)
campo_moeda_origem.grid(row=1, column=0, padx=10, pady=5)

# Moeda de Destino (coluna 1)
texto_moeda_destino = customtkinter.CTkLabel(frame_selecao, text="Moeda de Destino:", font=("Arial", 14))
texto_moeda_destino.grid(row=0, column=1, padx=10, pady=5)
campo_moeda_destino = customtkinter.CTkOptionMenu(
    frame_selecao, 
    values=["Selecione a origem primeiro"]
)
campo_moeda_destino.grid(row=1, column=1, padx=10, pady=5)

# Botão de Converter
def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_contacao_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moeda.configure(text=f"Cotação: 1 {moeda_origem} = {cotacao} {moeda_destino}")

botao_converter = customtkinter.CTkButton(
    janela, 
    text="Converter", 
    font=("Arial", 18), 
    command=converter_moeda
)
botao_converter.pack(pady=15)


# Label para exibir resultado
texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="", font=("Arial", 16))
texto_cotacao_moeda.pack(pady=10)

# Lista de moedas disponíveis
lista_moeda = customtkinter.CTkScrollableFrame(janela)
lista_moeda.pack(pady=10)

moedas_disponiveis = nomes_moedas()
for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(lista_moeda, text=f"{codigo_moeda}: {nome_moeda}") 
    texto_moeda.pack(anchor="w")

janela.mainloop()