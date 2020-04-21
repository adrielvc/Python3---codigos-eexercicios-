def ler_arquivo(nome_arquivo):
    # para fazer somente leitura temos R, escrita W, leitura e escrita R+
    arquivo = open(nome_arquivo, 'r')

    #laço para percorrer as linhas fazendo leitura dos dados do arquivo
    for linha in arquivo:
        print(linha)
    arquivo.close()

def salvar_arquivo(nome_arquivo, texto):
    #usamos o W porque a seguinte linha serve para escrever no arquivo
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(texto)

    arquivo.close()
    #quando utilizamos um recurso externo como arqvuios de texto, csv
    #conexão com banco de dados ou webservice temos sempre que fechar o recurso
    #porque se deixamos aberto até que o gerenciador do recurso elimine ele 
    #da memória ele vai ficar travado.a ponto de não conseguirmos acessá-lo
    #para leitura ou escrita