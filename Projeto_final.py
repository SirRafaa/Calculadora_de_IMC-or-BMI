import tkinter as tk
from tkinter import ttk

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura ** 2)
        
        # Verificar gênero para mensagem personalizada
        if genero_var.get() == "Masculino":
            mensagem = f"Seu IMC é: {imc:.2f}. Para homens, o ideal é manter o IMC entre 18.5 e 24.9."
        else:
            mensagem = f"Seu IMC é: {imc:.2f}. Para mulheres, o ideal é manter o IMC entre 18.5 e 25."
        
        label_resultado['text'] = mensagem
    except ValueError:
        label_resultado['text'] = "Digite apenas números para peso e altura."

# Janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("350x250")

# Estilo
style = ttk.Style()
style.configure("TButton", padding=10, relief="flat", background="lightblue")
style.configure("TLabel", font=("Helvetica", 12))

# Variável para armazenar o gênero
genero_var = tk.StringVar()
genero_var.set("Masculino")  # Valor padrão

# Rótulos e campos de entrada
label_peso = ttk.Label(janela, text="Peso (kg):")
label_peso.grid(row=0, column=0, sticky="w")
entry_peso = ttk.Entry(janela)
entry_peso.grid(row=0, column=1)

label_altura = ttk.Label(janela, text="Altura (m):")
label_altura.grid(row=1, column=0, sticky="w")
entry_altura = ttk.Entry(janela)
entry_altura.grid(row=1, column=1)

# Rótulo e Radiobuttons para gênero
label_genero = ttk.Label(janela, text="Gênero:")
label_genero.grid(row=2, column=0, sticky="w")

radio_masculino = ttk.Radiobutton(janela, text="Masculino", variable=genero_var, value="Masculino")
radio_masculino.grid(row=2, column=1, sticky="w")

radio_feminino = ttk.Radiobutton(janela, text="Feminino", variable=genero_var, value="Feminino")
radio_feminino.grid(row=3, column=1, sticky="w")

# Botão calcular
botao_calcular = ttk.Button(janela, text="Calcular IMC", command=calcular_imc)
botao_calcular.grid(row=4, column=0, columnspan=2, pady=10)

# Rótulo para resultado
label_resultado = ttk.Label(janela, text="", font=("Helvetica", 14))
label_resultado.grid(row=5, column=0, columnspan=2)

# Iniciando a aplicação
janela.mainloop()