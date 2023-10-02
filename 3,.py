def copia_arquivo_sem_comentarios(origem, destino):
    with open(origem, "r") as arquivo_velho, open(destino, "w") as arquivo_novo:
        for linha in arquivo_velho:
            if not linha.strip().startswith("//"):
                arquivo_novo.write(linha)

copia_arquivo_sem_comentarios("velho.txt", "novo.txt")