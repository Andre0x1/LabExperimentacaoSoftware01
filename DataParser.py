import csv
import statistics
import pandas as pd
import matplotlib.pyplot as plt

def calcular_media_criacao():
    nome_arquivo = 'repos.csv'  
    lista_dias_desde_criacao = []
    with open(nome_arquivo, 'r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
            dias_desde_criacao = float(linha['dias_desde_criacao'])  
            lista_dias_desde_criacao.append(dias_desde_criacao/365)

    media = statistics.mean(lista_dias_desde_criacao)

    print(f"A media da idade é: {(media)}")

    plt.hist(lista_dias_desde_criacao, bins=10, edgecolor='k', alpha=0.75)
    

    plt.title("Histograma Media de Idades")
    plt.xlabel("Dados")
    plt.ylabel("Valores")
    plt.savefig("RQ1.jpg")





def calcular_media_pull_request():


    nome_arquivo = 'repos.csv'  
    lista_pull_requests_aceitas = []

    with open(nome_arquivo, 'r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
                pull_requests_aceitas = float(linha['n_pull_requests'])  
                lista_pull_requests_aceitas.append(pull_requests_aceitas)

    media = statistics.mean(lista_pull_requests_aceitas)
    print(f"A media dos pull requests aceitas é: {(media)}")


    plt.hist(lista_pull_requests_aceitas, bins=100, edgecolor='k', alpha=0.75)
    plt.title("Histograma media pull requests")
    plt.xlabel("Dados")
    plt.ylabel("Valores")
    plt.savefig("RQ2.jpg")
    plt.close()



def calcular_media_releases():

    
    nome_arquivo = 'repos.csv'  
    lista_n_releases = []
    with open(nome_arquivo, 'r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
           n_releases = float(linha['n_releases'])  
           lista_n_releases.append(n_releases)

    media = statistics.mean(lista_n_releases)

    print(f"A media dos releases é: {(media)}")

    plt.hist(lista_n_releases, bins=10, edgecolor='k', alpha=0.75)
    plt.title("Histograma media releases")
    plt.xlabel("Dados")
    plt.ylabel("Valores")
    plt.savefig("RQ3.jpg")
    plt.close()



def calcular_media_dias_desde_atualizacao():

    
    nome_arquivo = 'repos.csv'  
    lista_dias_desde_atualizacao = []
    with open(nome_arquivo, 'r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
           dias_desde_atualizacao = float(linha['dias_desde_atualizacao'])  
           lista_dias_desde_atualizacao.append(dias_desde_atualizacao)

    media = statistics.mean(lista_dias_desde_atualizacao)

    print(f"A media dos dias desde atualizacao é: {(media)}")
    plt.hist(lista_dias_desde_atualizacao, bins=10, edgecolor='k', alpha=0.75)
    plt.title("Boxplot")
    plt.xlabel("Dados")
    plt.ylabel("Valores")
    plt.savefig("RQ4.jpg")
    plt.close()

def calcular_moda_linguagem():
    nome_arquivo = 'repos.csv'  
    df = pd.read_csv(nome_arquivo)

    linguagens_desejadas = ['JavaScript', 'Python', 'Java', 'C#', 'PHP']
    df_filtrado = df[df['linguagem'].isin(linguagens_desejadas)]

    moda = df_filtrado['linguagem'].mode()

    if moda.empty:
        return "Nenhum valor encontrado para as linguagens desejadas."
    else:
        print("A linguagem mais popular é:",  moda)
    
    contagem_linguagens = {linguagem: 0 for linguagem in linguagens_desejadas}
    contagem_outros = 0


    for linguagem in df['linguagem']:
        if linguagem in contagem_linguagens:
            contagem_linguagens[linguagem] += 1
        else:
            contagem_outros += 1

    contagem_linguagens['Outros'] = contagem_outros
    linguagens = list(contagem_linguagens.keys())
    contagens = list(contagem_linguagens.values())
    

    plt.bar(linguagens, contagens, edgecolor='k', alpha=0.75)
    plt.title("Contagem de Linguagens")
    plt.xlabel("Linguagens")
    plt.ylabel("Contagem")
    plt.xticks(rotation=45) 


    plt.tight_layout()
    plt.savefig("RQ5.jpg")
    plt.close()

def calcular_media_issues():

    nome_arquivo = 'repos.csv'  
    lista_n_issues = []
    with open(nome_arquivo, 'r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
           n_issues = float(linha['n_issues']) 
           if n_issues > 0:
                n_issues_fechadas = float(linha['n_issues_fechadas'])  
                percentual_fechado = ((n_issues_fechadas*100))/n_issues
           else:
                percentual_fechado = 0
           lista_n_issues.append(percentual_fechado)

    media = statistics.mean(lista_n_issues)

    print(f"A media da porcentagem das issues fechadas é: {(media)}")

    plt.hist(lista_n_issues, bins=100, edgecolor='k', alpha=0.75)
    plt.title("Histograma media Issues")
    plt.xlabel("Dados")
    plt.ylabel("Valores")
    plt.savefig("RQ6.jpg")
    plt.close()



def calcular_media_pull_request_linguagem():
    nome_arquivo = 'repos.csv'
    linguagens = ['JavaScript', 'Python', 'Java', 'C#', 'PHP']
    
    linguagem_pull_requests = {linguagem: {'count': 0, 'sum': 0} for linguagem in linguagens}

    with open(nome_arquivo, 'r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        
        for linha in leitor:
            linguagem = linha['linguagem']
            if linguagem in linguagens:
                pull_requests_aceitas = float(linha['n_pull_requests'])
                linguagem_pull_requests[linguagem]['count'] += 1
                linguagem_pull_requests[linguagem]['sum'] += pull_requests_aceitas

    for linguagem in linguagens:
        count = linguagem_pull_requests[linguagem]['count']
        total = linguagem_pull_requests[linguagem]['sum']
        if count > 0:
            media = total / count
            print(f'Média de pull requests para {linguagem}: {media}')


def calcular_media_release_linguagem():
    nome_arquivo = 'repos.csv'
    linguagens = ['JavaScript', 'Python', 'Java', 'C#', 'PHP']
    
    linguagem_pull_requests = {linguagem: {'count': 0, 'sum': 0} for linguagem in linguagens}

    with open(nome_arquivo, 'r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        
        for linha in leitor:
            linguagem = linha['linguagem']
            if linguagem in linguagens:
                pull_requests_aceitas = float(linha['n_releases'])
                linguagem_pull_requests[linguagem]['count'] += 1
                linguagem_pull_requests[linguagem]['sum'] += pull_requests_aceitas

    for linguagem in linguagens:
        count = linguagem_pull_requests[linguagem]['count']
        total = linguagem_pull_requests[linguagem]['sum']
        if count > 0:
            media = total / count
            print(f'Média de releases para {linguagem}: {media}')


def calcular_media_dias_desde_atualizacao_linguagem():
    nome_arquivo = 'repos.csv'
    linguagens = ['JavaScript', 'Python', 'Java', 'C#', 'PHP']
    
    linguagem_pull_requests = {linguagem: {'count': 0, 'sum': 0} for linguagem in linguagens}

    with open(nome_arquivo, 'r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        
        for linha in leitor:
            linguagem = linha['linguagem']
            if linguagem in linguagens:
                pull_requests_aceitas = float(linha['dias_desde_atualizacao'])
                linguagem_pull_requests[linguagem]['count'] += 1
                linguagem_pull_requests[linguagem]['sum'] += pull_requests_aceitas

    for linguagem in linguagens:
        count = linguagem_pull_requests[linguagem]['count']
        total = linguagem_pull_requests[linguagem]['sum']
        if count > 0:
            media = total / count
            print(f'Média de dias desde a atualização para {linguagem}: {media}')
        


if __name__ == "__main__":

    calcular_media_criacao()
    calcular_media_pull_request()
    calcular_media_releases()
    calcular_media_dias_desde_atualizacao()
    calcular_moda_linguagem()
    calcular_media_issues()




    print("RQ07")

    calcular_media_pull_request_linguagem()
    calcular_media_release_linguagem()
    calcular_media_dias_desde_atualizacao_linguagem()