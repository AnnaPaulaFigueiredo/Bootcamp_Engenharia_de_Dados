# Média de notas ENEM  baseadas em querys no Pandas 
Esse projeto ilustra uma análise sobre os dados do ENEM 2019 para os alunos residentes no estado de Minas Gerais.

## Base de dados
A base de dados foi retirada do programa dados abertos do governo federal, [Micro dados Inep](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados). O script trabalha com o download automático dos [microdados do enem 2019](http://download.inep.gov.br/microdados/microdados_enem_2019.zip) no arquivo extract_site.py. Onde é feito o download de forma automática e a extração do zipfile.

## Preparação do ambiente de execução
Para rodar os arquivos é necessário:
- [Python 3: necessário para executar os projetos.py.](https://www.python.org/downloads/)
- [Numpy: para realização de cálculos.](https://pypi.org/project/numpy/)
- [Pandas: manipulação e análise de dados.](https://pandas.pydata.org/)
- [Requests: requisições HTTP.](https://pypi.org/project/requests/)
- [IO: lidar com arquivos de E/S.](https://docs.python.org/3/library/io.html)
- [ZipFile: compactar e descompactar arquivos.](https://docs.python.org/3/library/zipfile.html#module-zipfile)

## Construção
### extract_site.py :
  extrai os dados do site, e realiza sua extração  zipFile.
### transform_data.py : 
  faz o carregamento da base para a memória, utilizando chunks, e processa filtrando os alunos do Estado de Minas Gerais. Tem como saída, dois novos dataset. 

- data_ENEM_MG_present.csv : Possui os dados dos estudantes de Minas Gerais, presentes para a realização da prova.

- data_ENEM_MG_present_score_not_zero.csv : Possui os dados dos estudantes de Minas Gerais presentes para a realização da prova e que não tiraram nota zero, como nota final, ou seja, sum(all_score) > 0 .

### analyze.py: 
  faz o carregamento dos dados gerados em transform_data.py, para a memória, e realiza as questões do Trabalho Prático, são elas :
1. Qual é a média da nota em matemática de todos os alunos mineiros ?
2. Qual é a média da nota de Linguagens e Códigos de todos os alunos mineiros ?
3. Qual é a média da nota em Ciências Humanas dos alunos do sexo FEMININO mineiros ?
4. Qual é a média da nota em Ciências Humanas dos alunos do sexo MASCULINO mineiros ?
5. Qual é a média da nota em matemática dos alunos do sexo FEMININO que moram na cidade de Montes Claros ?
6. Qual é a média da nota em Matemática dos alunos do município de Sabará que possuem TV por assinatura na residência ?
7. Qual é a média da nota em Ciências Humanas dos alunos mineiros que possuem dois fornos de micro-ondas em casa ?
8. Qual é a nota média em Matemática dos alunos mineiros cuja mãe completou a pós-graduação ?
9. Qual é a nota média em Matemática dos alunos de Belo Horizonte e de Conselheiro Lafaiete ?
10. Qual é a nota média em Ciências Humanas dos alunos mineiros que moram sozinhos ?
11. Qual é a nota média em Ciências Humanas dos alunos mineiros cujo pai completou Pós Graduação e possuem renda familiar entre R$ 8.982,01 e R$ 9.980,00 ?
12. Qual é a nota média em Matemática dos alunos do sexo FEMININO que moram em Lavras e escolheram "Espanhol" como língua estrangeira ?
13. Qual é a nota média em Matemática dos alunos do sexo Masculino que moram em Ouro Preto ?
14. Qual é a nota média em Ciências Humanas dos alunos surdos ?
15. Qual é a nota média em Matemática dos alunos do sexo FEMININO que moram em Belo Horizonte, Sabará, Nova Lima e Betim e possuem dislexia ?
