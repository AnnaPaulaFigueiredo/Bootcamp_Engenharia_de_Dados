from numpy.core.fromnumeric import mean
import pandas as pd 
import numpy as np

def load_data_csv(path):
    
    data = pd.read_csv(path, encoding="utf-8", sep=";")

    return data


def infos (data: pd):

    print("Describe Data: \n", data.describe())
    print("Head + 2: \n", data.head(2))
    print("Columns: \n", data.columns)


def calculate_men_column(data: pd, column: str):

    mean = np.mean(data[column])

    return round(mean, 1)

def calculate_query_mean(data: pd, query: str, column):

    data = data.query(query)

    mean = np.mean(data[column])

    return round(mean, 1)

def main():

    path_present = "/home/annap/Documentos/IGTI/Eng_Dados/Modulo1/TP_Enem_2019/data_ENEM_MG_present.csv"
    path_present_score_total = "/home/annap/Documentos/IGTI/Eng_Dados/Modulo1/TP_Enem_2019/data_ENEM_MG_present_score_not_zero.csv"
    
    df_enem_present = load_data_csv(path_present)
    df_enem_score_total = load_data_csv(path_present_score_total)

   
    #infos(df_enem_present)
  
    #infos(df_enem_score_total)

    # Resultados do TP 1
    # Qual é a média da nota em matemática de todos os alunos mineiros?
    print("---Média Da Nota de Matemática. \nPresentes: {} \nPresentes sem notas zero: {}" \
            .format(calculate_men_column(df_enem_present, "NU_NOTA_MT"), calculate_men_column(df_enem_score_total, "NU_NOTA_MT")))

    # Qual é a média da nota de Linguagens e Códigos de todos os alunos mineiros?
    print("---Média Da Nota de Linguagens e Código. \nPresentes: {} \nPresentes sem notas zero: {}" \
            .format(calculate_men_column(df_enem_present, "NU_NOTA_LC"), calculate_men_column(df_enem_score_total, "NU_NOTA_LC")))

    # Qual é a média da nota em Ciências Humanas dos alunos do sexo FEMININO e MASCULINOS mineiros?
    query = str("TP_SEXO == 'F'")
    print("---Média Da Nota de Ciências Humanas do sexo Feminino. \nPresentes: {} \nPresentes sem notas zero: {}" \
            .format(calculate_query_mean(df_enem_present, query,  "NU_NOTA_CH"), calculate_query_mean(df_enem_score_total, query, "NU_NOTA_CH")))

    query = str("TP_SEXO == 'M'")
    print("---Média Da Nota de Ciências Humanas do sexo Masculino.\nPresentes: {} \nPresentes sem notas zero: {}" \
            .format(calculate_query_mean(df_enem_present, query,  "NU_NOTA_CH"), calculate_query_mean(df_enem_score_total, query, "NU_NOTA_CH")))

    # Qual é a média da nota em matemática dos alunos do sexo FEMININO que moram na cidade de Montes Claros?
    query = str("TP_SEXO == 'F' & NO_MUNICIPIO_RESIDENCIA == 'Montes Claros'")
    print("---Média Da Nota de Matemática do sexo Feminino, Residentes em Montes Claros. \nPresentes: {} \nPresentes sem notas zero: {}" \
            .format(calculate_query_mean(df_enem_present, query,  "NU_NOTA_MT"), calculate_query_mean(df_enem_score_total, query, "NU_NOTA_MT")))

    # Qual é a média da nota em Matemática dos alunos do município de Sabará que possuem TV por assinatura na residência?
    query = str(" NO_MUNICIPIO_RESIDENCIA == 'Sabará' & Q021 == 'B' ")
    print("---Média Da Nota de Matemática dos Alunos, Residentes em Sabará que possuem TV por assinatura. \nPresentes: {} \nPresentes sem notas zero: {}" \
            .format(calculate_query_mean(df_enem_present, query,  "NU_NOTA_MT"), calculate_query_mean(df_enem_score_total, query, "NU_NOTA_MT")))

    # Qual é a média da nota em Ciências Humanas dos alunos mineiros que possuem dois fornos de micro-ondas em casa?
    query = str(" Q016 == 'C' ")
    print("---Média Da Nota de Ciências Humanas dos Alunos que possuem dois fornos de micro-ondas.\nPresentes: {} \nPresentes sem notas zero: {}" \
            .format(calculate_query_mean(df_enem_present, query,  "NU_NOTA_CH"), calculate_query_mean(df_enem_score_total, query, "NU_NOTA_CH")))

    # Qual é a nota média em Matemática dos alunos mineiros cuja mãe completou a pós-graduação?
    query = str(" Q002 == 'G' ")
    print("---Média Da Nota de Matemática dos Alunos, cuja mãe completou a pós-graduação. \nPresentes: {} \nPresentes sem notas zero: {}" \
            .format(calculate_query_mean(df_enem_present, query,  "NU_NOTA_MT"), calculate_query_mean(df_enem_score_total, query, "NU_NOTA_MT")))

    # Qual é a nota média em Matemática dos alunos de Belo Horizonte e de Conselheiro Lafaiete ?
    query = " NO_MUNICIPIO_RESIDENCIA == 'Belo Horizonte' | NO_MUNICIPIO_RESIDENCIA == 'Conselheiro Lafaiete' "
    print("---Média Da Nota de Matemática dos Alunos, residentes e Belo Horizonte e de Conselheiro Lafaiete. \nPresentes: {} \nPresentes sem notas zero: {}" \
            .format(calculate_query_mean(df_enem_present, query,  "NU_NOTA_MT"), calculate_query_mean(df_enem_score_total, query, "NU_NOTA_MT")))

    # Qual é a nota média em Ciências Humanas dos alunos mineiros que moram sozinhos?
    query = " Q005 == 1 "
    print("---Média Da Nota de Ciências Humanas dos Alunos que moram só. \nPresentes: {} \nPresentes sem notas zero: {}" \
            .format(calculate_query_mean(df_enem_present, query,  "NU_NOTA_CH"), calculate_query_mean(df_enem_score_total, query, "NU_NOTA_CH")))

    # Qual é a nota média em Ciências Humanas dos alunos mineiros cujo pai completou Pós Graduação e possuem renda familiar entre R$ 8.982,01 e R$ 9.980,00 ?
    query = " Q001 == 'G' & Q006 == 'M' "
    print("---Média Da Nota de Ciências Humanas dos Alunos cujo pai completou Pós Graduação e possuem renda familiar entre R$ 8.982,01 e R$ 9.980,00. \nPresentes: {} \nPresentes sem notas zero: {}" \
            .format(calculate_query_mean(df_enem_present, query,  "NU_NOTA_CH"), calculate_query_mean(df_enem_score_total, query, "NU_NOTA_CH")))

    # Qual é a nota média em Matemática dos alunos do sexo FEMININO que moram em Lavras e escolheram "Espanhol" como língua estrangeira?
    query = " TP_SEXO == 'F' & NO_MUNICIPIO_RESIDENCIA == 'Lavras' & TP_LINGUA == 1"
    print("---Média Da Nota de Matemática dos Alunos, do sexo FEMININO que escolheram ESPANHOL e residem em Lavras. \nPresentes: {} \nPresentes sem notas zero: {}" \
            .format(calculate_query_mean(df_enem_present, query,  "NU_NOTA_MT"), calculate_query_mean(df_enem_score_total, query, "NU_NOTA_MT")))

    # Qual é a nota média em Matemática dos alunos do sexo Masculino que moram em Ouro Preto?
    query = " TP_SEXO == 'M' & NO_MUNICIPIO_RESIDENCIA == 'Ouro Preto' "
    print("---Média Da Nota de Matemática dos Alunos, do sexo MASCULINO que residem em Ouro Preto. \nPresentes: {} \nPresentes sem notas zero: {}" \
           .format(calculate_query_mean(df_enem_present, query,  "NU_NOTA_MT"), calculate_query_mean(df_enem_score_total, query, "NU_NOTA_MT")))

    # Qual é a nota média em Ciências Humanas dos alunos surdos?
    query = " IN_SURDEZ == 1 "
    print("---Média Da Nota de Ciências Humanas dos Alunos que são Surdos. \nPresentes: {} \nPresentes sem notas zero: {}" \
            .format(calculate_query_mean(df_enem_present, query,  "NU_NOTA_CH"), calculate_query_mean(df_enem_score_total, query, "NU_NOTA_CH")))

    # Qual é a nota média em Matemática dos alunos do sexo FEMININO que moram em Belo Horizonte, Sabará, Nova Lima e Betim e possuem dislexia?
    query = " TP_SEXO == 'F' and IN_DISLEXIA == 1 and (NO_MUNICIPIO_RESIDENCIA == 'Belo Horizonte' | NO_MUNICIPIO_RESIDENCIA == 'Sabará' \
              | NO_MUNICIPIO_RESIDENCIA == 'Nova Lima' | NO_MUNICIPIO_RESIDENCIA == 'Betim') "
    print("---Média Da Nota de Matemática dos Alunos, do sexo FEMININO que residem em Sabará, Belo Horizonte, Betim e Nova Lima, que possuem Dislexia. \nPresentes: {} \nPresentes sem notas zero: {}" \
           .format(calculate_query_mean(df_enem_present, query,  "NU_NOTA_MT"), calculate_query_mean(df_enem_score_total, query, "NU_NOTA_MT")))



if __name__ == "__main__":
    main()