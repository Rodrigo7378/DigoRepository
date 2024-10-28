import tkinter as tk
from tkinter import ttk, filedialog
from pytubefix import YouTube
import os

def baixar_video():
    """
    Baixa o vídeo do YouTube na pasta de Downloads do usuário.
    """
    link = entrada_link.get()
    try:
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        
        # Obtém o caminho da pasta Downloads do usuário
        pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads") 
        
        stream.download(pasta_downloads)
        status_label.config(text="Download concluído!")
    except Exception as e:
        status_label.config(text=f"Erro ao baixar o vídeo: {e}")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Baixador de Vídeos do YouTube por Rodrigão, o Delicioso.")

# Rótulo e entrada para o link do vídeo
link_label = ttk.Label(janela, text="Insira o Link do vídeo, o Vídeo será baixado na maior resolução possível:")
link_label.grid(row=0, column=0, padx=5, pady=5)
entrada_link = ttk.Entry(janela, width=50)
entrada_link.grid(row=0, column=1, padx=5, pady=5)

# Botão para baixar o vídeo
botao_baixar = ttk.Button(janela, text="Baixar", command=baixar_video)
botao_baixar.grid(row=1, column=0, columnspan=2, pady=10)

# Rótulo para exibir o status do download
status_label = ttk.Label(janela, text="")
status_label.grid(row=2, column=0, columnspan=2, pady=5)

janela.mainloop()