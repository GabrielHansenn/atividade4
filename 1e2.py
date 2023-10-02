
import random


def arquivador(listaNomes, listaSobrenomes, nomeArquivo):
    arquivoNomes = open(nomeArquivo, 'w')
    for i in range(0, 20):
        altura = round(random.SystemRandom().uniform(1, 2), 2)
        arquivoNomes.write(str(listaNomes[random.randint(0, 19)]))
        arquivoNomes.write(" ")
        arquivoNomes.write(str(listaSobrenomes[random.randint(0, 19)]))
        arquivoNomes.write(" ")
        arquivoNomes.write("Idade: ")
        arquivoNomes.write(str(random.randint(1, 50)))
        arquivoNomes.write(" ")
        arquivoNomes.write("Altura: ")
        arquivoNomes.write(str(altura))
        arquivoNomes.write("\n")
    arquivoNomes.close()

listaNomes = ['Ana', 'Carlos', 'Maria', 'Pedro', 'João', 'Luiza', 'Lucas', 'Julia', 'Rafael', 'Mariana', 'Fernanda', 'Diego', 'Camila', 'Renato', 'Júlia', 'Matheus', 'Laura', 'Gustavo', 'Aline', 'Daniel']

listaSobrenomes= ['Silva', 'Oliveira', 'Santos', 'Costa', 'Pereira', 'Ribeiro', 'Ferreira', 'Almeida', 'Carvalho', 'Gomes', 'Araujo', 'Lima', 'Barbosa', 'Castro', 'Monteiro', 'Melo', 'Braga', 'Fernandes', 'Sousa', 'Gonçalves']

arquivador(listaNomes, listaSobrenomes, 'listaDeNomes.txt')