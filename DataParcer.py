import csv
import statistics

def calcular_mediana():
    nome_arquivo = 'repos.csv'  
    lista_dias_desde_criacao = []

    with open(nome_arquivo, 'r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        
        for linha in leitor:
            dias_desde_criacao = float(linha['dias_desde_criacao'])  
            lista_dias_desde_criacao.append(dias_desde_criacao)

    mediana = statistics.median(lista_dias_desde_criacao)

    print(f"A mediana da idade é: {mediana}")
    

if __name__ == "__main__":
    calcular_mediana()