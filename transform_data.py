import pandas as pd 

def filter_data_ENEM_MG(path: str):

    chunks = []
    for chunk in pd.read_csv(path, delimiter=";", encoding="ISO-8859-1", chunksize=50000):

        data = chunk.query("SG_UF_RESIDENCIA == 'MG'")
        chunks.append(data)
        
            
    data = pd.concat(chunks)
    data.to_csv("data_ENEM_MG.csv", sep=";", encoding="UTF-8", index=False )

def filter_data_ENEM_present(path: str):

    data = pd.read_csv(path, sep=";", encoding="utf-8")

    # Verifica se a pessoa estava presente na prova x, cod de presença == 1 (via dic dados)
    data = data.loc[ (data.TP_PRESENCA_CN == 1 ) | 
                     (data.TP_PRESENCA_CH == 1 ) |
                     (data.TP_PRESENCA_LC == 1 ) |
                     (data.TP_PRESENCA_MT == 1 )]

    data.to_csv("data_ENEM_MG_present.csv", sep=";", encoding="UTF-8", index=False )

def filter_data_ENEM_score_not_zero(path: str):

    data = pd.read_csv(path, sep=";", encoding="utf-8")

    exames = ["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_MT", "NU_NOTA_LC", "NU_NOTA_REDACAO"]

    data["NU_NOTA_TOTAL"] = data[exames].sum(axis=1)
    
    data = data.loc[data.NU_NOTA_TOTAL > 0]

    print(data.NU_NOTA_TOTAL)
    data.to_csv("data_ENEM_MG_present_score_not_zero.csv", sep=";", encoding="UTF-8", index=False)


def main():

    path_original = "./enem_2019/DADOS/MICRODADOS_ENEM_2019.csv"
    filter_data_ENEM_MG(path_original)

    path_enem = "/home/annap/Documentos/IGTI/Eng_Dados/Modulo1/TP_Enem_2019/data_ENEM_MG.csv"
    filter_data_ENEM_present(path_enem)
   
    filter_data_ENEM_score_not_zero(path_enem)

if __name__ == "__main__":
    main()