#!/usr/bin/env python3
import tkinter as tk

# Função para atualizar o display com o número selecionado
def atualizar_display(numero):
    display.config(state=tk.NORMAL)
    display.insert(tk.END, numero)
    display.config(state=tk.DISABLED)

# Função para exibir o resultado no display
def exibir_resultado():
    expressao = display.get(1.0, tk.END)
    resultado = avaliar_expressao(expressao)
    if resultado is not None:
        display.config(state=tk.NORMAL)
        display.delete(1.0, tk.END)
        display.insert(tk.END, str(resultado))
        display.config(state=tk.DISABLED)
    else:
        display.config(state=tk.NORMAL)
        display.delete(1.0, tk.END)
        display.insert(tk.END, "Erro")
        display.config(state=tk.DISABLED)

# Função para limpar o display
def limpar_display():
    display.config(state=tk.NORMAL)
    display.delete(1.0, tk.END)
    display.config(state=tk.DISABLED)

# Função para avaliar a expressão matemática
def avaliar_expressao(expressao):
    try:
        # Remove espaços em branco
        expressao = expressao.replace(' ', '')
        # Substitui os símbolos de operação por operadores matemáticos
        expressao = expressao.replace('×', '*').replace('÷', '/')
        # Avalia a expressão
        resultado = eval(expressao)
        return resultado
    except (SyntaxError, TypeError, ZeroDivisionError, NameError):
        return None

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.configure(background='#222222')  # Definindo a cor de fundo da janela

# Cria o display
display = tk.Text(janela, height=2, width=20, bd=3, relief=tk.SUNKEN)
display.config(state=tk.DISABLED, bg='#222222', fg='white')  # Definindo a cor de fundo e cor do texto do display
display.pack(pady=10)

# Cria os botões
botoes = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['.', '0', '⇦'],
    ['+', '-', '×'],
    ['÷', None, '=']
]

for linha in botoes:
    frame = tk.Frame(janela, bg='#222222')  # Definindo a cor de fundo do frame
    frame.pack()
    for valor in linha:
        if valor == '=':
            botao = tk.Button(frame, text=valor, width=5, command=exibir_resultado, bg='#222222', fg='white')
        elif valor == '⇦':
            botao = tk.Button(frame, text=valor, width=5, command=limpar_display, bg='#222222', fg='white')
        elif valor is None:
            botao = tk.Button(frame, text='', width=5, state=tk.DISABLED)  # Botão indisponível
        else:
            botao = tk.Button(frame, text=valor, width=5, command=lambda x=valor: atualizar_display(x), bg='#222222', fg='white')
        botao.pack(side=tk.LEFT)

# Cria o rótulo com o texto da borda final
rodape_frame = tk.Frame(janela, bg='#222222')  # Definindo o frame para agrupar os rótulos
rodape_frame.pack(side=tk.BOTTOM, pady=10)

rodape = tk.Label(rodape_frame, text="(Created by @joku.moba)", bg='#222222', fg='white', font=('Arial', 5, 'italic'))
rodape.pack(side=tk.LEFT)

versao = tk.Label(rodape_frame, text="calc v0.1a", bg='#222222', fg='white', font=('Arial', 2, 'italic'))
versao.pack(side=tk.LEFT, padx=10)

# Inicia o loop da janela
janela.mainloop()