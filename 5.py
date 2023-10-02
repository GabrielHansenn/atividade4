def alterar_nota_aluno(arquivo_notas, nome_aluno, nota_velha, nota_nova):
    linhas = []
    with open(arquivo_notas, "r") as arquivo_leitura:
        for linha in arquivo_leitura:
            if nome_aluno in linha:
                linha = linha.replace(nota_velha, nota_nova)
            linhas.append(linha)
    with open(arquivo_notas, "w") as arquivo_escrita:
        arquivo_escrita.writelines(linhas)

alterar_nota_aluno("notas.txt", "Gabriel", "6.5", "8.7")