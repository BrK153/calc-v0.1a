import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import webbrowser

def atualizar_display(numero):
    display.config(state=tk.NORMAL)
    display.insert(tk.END, numero)
    display.config(state=tk.DISABLED)

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
        display.insert(tk.END, "0")  # Exibir o número 0
        display.config(state=tk.DISABLED)

def limpar_display():
    display.config(state=tk.NORMAL)
    display.delete(1.0, tk.END)
    display.config(state=tk.DISABLED)

def excluir_caractere():
    display.config(state=tk.NORMAL)
    display.delete('end-2c')
    display.config(state=tk.DISABLED)

def calcular_porcentagem():
    expressao = display.get(1.0, tk.END)
    try:
        numero, porcentagem = expressao.split('+')
        numero = float(numero.strip())
        porcentagem = float(porcentagem.strip().replace('%', ''))
        resultado = calcular_porcentagem_real(numero, porcentagem)
        display.config(state=tk.NORMAL)
        display.delete(1.0, tk.END)
        display.insert(tk.END, str(resultado))
        display.config(state=tk.DISABLED)
    except (ValueError, ZeroDivisionError, IndexError):
        display.config(state=tk.NORMAL)
        display.delete(1.0, tk.END)
        display.insert(tk.END, "Erro")
        display.config(state=tk.DISABLED)

def calcular_porcentagem_real(numero, porcentagem):
    resultado = numero + (numero * (porcentagem / 100))
    return resultado

def avaliar_expressao(expressao):
    try:
        expressao = expressao.replace(' ', '')
        expressao = expressao.replace('×', '*').replace('÷', '/')
        resultado = eval(expressao)
        return resultado
    except (SyntaxError, TypeError, ZeroDivisionError, NameError):
        return None

def exibir_mensagem():
    messagebox.showinfo("Aviso", "Aplicativo em fase de teste!", icon='warning')

def abrir_github(event):
    webbrowser.open_new("https://github.com/BrK153/calc-v0.1a/issues")

janela = tk.Tk()
janela.title("Calculadora")
janela.configure(background='#222222')

display = tk.Text(janela, height=2.5, width=40, bd=4.5, relief=tk.SUNKEN)
display.config(state=tk.DISABLED, bg='#222222', fg='white')
display.pack(pady=10)

botoes = [
    ['AC', '⇦', '%', '/'],
    ['7', '8', '9', '×'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['?', '0', '.', '='],
]

for linha in botoes:
    frame = tk.Frame(janela, bg='#F00000')
    frame.pack()
    for valor in linha:
        if valor == '=':
            botao = ttk.Button(frame, text=valor, width=5, command=exibir_resultado, style='Equal.TButton')
        elif valor == '/':
            botao = ttk.Button(frame, text=valor, width=5, command=lambda x=valor: atualizar_display(x), style='Operator.TButton')
        elif valor in ('×', '-', '+'):
            botao = ttk.Button(frame, text=valor, width=5, command=lambda x=valor: atualizar_display(x), style='Operator.TButton')
        elif valor == '⇦':
            botao = ttk.Button(frame, text=valor, width=5, command=excluir_caractere, style='Delete.TButton')
        elif valor == 'AC':
            botao = ttk.Button(frame, text=valor, width=5, command=limpar_display, style='Clear.TButton')
        elif valor == '%':
            botao = ttk.Button(frame, text=valor, width=5, command=calcular_porcentagem, style='Operator.TButton')
        elif valor == '?':
            botao = ttk.Button(frame, text=valor, width=5, command=exibir_mensagem, style='Question.TButton')
        else:
            botao = ttk.Button(frame, text=valor, width=5, command=lambda x=valor: atualizar_display(x), style='Number.TButton')
        botao.pack(side=tk.LEFT)

rodape_frame = tk.Frame(janela, bg='#222222') #background do app
rodape_frame.pack(side=tk.BOTTOM, pady=10)

rodape = tk.Label(rodape_frame, text="(Criado por @joku.moba)", bg='#222222', fg='white', font=('Arial', 5, 'italic'))
rodape.pack(side=tk.LEFT)

github_label = tk.Label(rodape_frame, text="[REPORT BUGS ON GITHUB]", bg='#222222', fg='blue', font=('Arial', 5, 'italic'), cursor='hand2')
github_label.pack(side=tk.LEFT)
github_label.bind("<Button-1>", abrir_github)

versao = tk.Label(rodape_frame, text="calc v0.2b", bg='#222222', fg='white', font=('Arial', 3, 'italic'))
versao.pack(side=tk.LEFT, padx=10)

style = ttk.Style()
style.configure('Equal.TButton', font=('Arial', 14, 'bold'), background='#1ed633', foreground='green')
style.configure('Operator.TButton', font=('Arial', 14, 'bold'), background='#FF5722', foreground='white')
style.configure('Number.TButton', font=('Arial', 14, 'bold'), background='#FFFFFF', foreground='#222222')
style.configure('Delete.TButton', font=('Arial', 14, 'bold'), background='#f06b13', foreground='orange')
style.configure('Clear.TButton', font=('Arial', 14, 'bold'), background='#F06b13', foreground='orange')
style.configure('Question.TButton', font=('Arial', 14, 'bold'), background='#f06b13', foreground='orange')

janela.mainloop()
