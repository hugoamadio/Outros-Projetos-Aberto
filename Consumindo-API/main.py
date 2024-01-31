import tkinter as tk
import requests

def requisicao():
    apiKey = "8189aa34652a84510f59c436858f5e37"
    cidadeInserida = cidade.get()
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidadeInserida}&appid={apiKey}"
    dados = requests.get(link)
    dadosDic = dados.json()
    tempo = dadosDic["weather"][0]["description"]
    label_cidade_atualizavel["text"] = cidadeInserida
    temperatura = dadosDic["main"]["temp"]
    temperaturaArredondada = round(temperatura-273,1)
    label_temperatura_atualizavel["text"] = f"{temperaturaArredondada} °C"

    if tempo in ["clear sky", "Few Clouds", "Partly Cloudy", "Mostly Clear", "Mainly Clear", "Clear with Periods of Clouds"]:
        clima_image = tk.PhotoImage(file="ensolarado.png")
        labelClima.config(image=clima_image)
        labelClima.image = clima_image
    elif "rain" in tempo:
        clima_image = tk.PhotoImage(file="chuvoso.png")
        labelClima.config(image=clima_image)
        labelClima.image = clima_image
    elif "clouds" in tempo:
        clima_image = tk.PhotoImage(file="nublado.png")
        labelClima.config(image=clima_image)
        labelClima.image = clima_image
    print(tempo)

root = tk.Tk()
root.title("Previsão do Tempo")
root.geometry("330x300")


root.configure(bg="#EB6E4B")

espacoLinha = tk.Label(root, text="", bg="#EB6E4B")
espacoLinha.grid(row=0, column=0, columnspan=2)

espacoColuna = tk.Label(root, text="", bg="#EB6E4B")
espacoColuna.grid(row=1, column=0)

procurar = tk.Button(root, text="Procurar", command=requisicao)
procurar.grid(row=1, column=4, columnspan=2, padx=10, pady=10)

fonte = ("Arial", 12, "bold")
labelCidade = tk.Label(root, text="Cidade:", bg="#EB6E4B", font=fonte)
labelCidade.grid(row=1, column=1, padx=10, pady=10)

cidade = tk.Entry(root)
cidade.grid(row=1, column=2, padx=10, pady=10)

cidade_label_var = tk.StringVar()
cidade_label_var.set("")

label_cidade_atualizavel = tk.Label(root, text="", bg="#EB6E4B")
label_cidade_atualizavel.grid(row=2, column=2, columnspan=3, padx=10, pady=10)

label_temperatura_atualizavel = tk.Label(root,text="", bg="#EB6E4B")
label_temperatura_atualizavel.grid(row=3, column=2, columnspan=3, padx=10, pady=10)

clima = tk.StringVar()
clima.set("")
clima_image = tk.PhotoImage()

labelClima = tk.Label(root, image=clima_image, bg="#EB6E4B")
labelClima.grid(row=2, column=1, columnspan=3, padx=10, pady=10)


root.mainloop()