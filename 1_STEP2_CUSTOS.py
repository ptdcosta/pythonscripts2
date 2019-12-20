import pandas as pd

Custos_SPN_EQUIPA = 'CustosSPN_Output.xlsx'
Custos_SPN_CEO = 'CustosSPN_CEO_Output.xlsx'
Custos_AV = 'CustosAV_Output.xlsx'
Custos_G13 = 'CustosG13_Output.xlsx'
Custos_JLS = 'CustosJLS_Output.xlsx'
Custos_JLS_RSA = 'CustosJLS_RSA_Output.xlsx'
Custos_VE = 'CustosVE_Output.xlsx'
Custos_HSTP = 'CustosHSTP_Output.xlsx'
Custos_PMT = 'CustosPMT_Output.xlsx'
Custos_RB = 'CustosRB_Output.xlsx'
Custos_YES = 'CustosYES_Output.xlsx'
Custos_CA = 'CustosCA_Output.xlsx'
Custos_MAO = 'CustosMAO_Output.xlsx'
Custos_JR = 'CustosJR_Output.xlsx'

print("caminho dos ficheiros mapeado")

df_HSTP = pd.read_excel(Custos_HSTP)
df_HSTP1 = df_HSTP[~df_HSTP['VALOR FINAL'].isin(['0', 0, '-'])]

df_PMT = pd.read_excel(Custos_PMT)
df_PMT1 = df_PMT[~df_PMT['VALOR FINAL'].isin(['0', 0, '-'])]

df_G13 = pd.read_excel(Custos_G13)
df_G13_1 = df_G13[~df_G13['VALOR FINAL'].isin(['0', 0, '-'])]

df_JLS_RSA = pd.read_excel(Custos_JLS_RSA)
df_JLS_RSA_1 = df_JLS_RSA[~df_JLS_RSA['VALOR FINAL'].isin(['0', 0, '-'])]

df_VE = pd.read_excel(Custos_VE, 'VE-OUT19')
df_VE1 = df_VE[~df_VE['VALOR FINAL'].isin(['0', 0, '-'])]

df_SPN_EQUIPA = pd.read_excel(Custos_SPN_EQUIPA)
df_SPN_1 = df_SPN_EQUIPA[~df_SPN_EQUIPA['VALOR FINAL'].isin(['0', '-', 0])]

df_RB = pd.read_excel(Custos_RB)
df_RB1 = df_RB[~df_RB['VALOR FINAL'].isin(['0', 0, '-'])]

df_YES = pd.read_excel(Custos_YES)
df_YES1 = df_YES[~df_YES['VALOR FINAL'].isin(['0', 0, '-'])]

print("Data Frames Criadas")

HSTP = df_HSTP1[['BICODE', 'BRAND', 'ACCOUNT', 'TRACKER CUSTOS',
                 'SITE', 'EQUIPA', 'AGENT', 'MOEDA', 'VALOR FINAL']]

PMT = df_PMT1[['BICODE', 'BRAND', 'ACCOUNT', 'TRACKER CUSTOS',
               'SITE', 'EQUIPA', 'AGENT', 'MOEDA', 'VALOR FINAL']]

G13 = df_G13_1[['BICODE', 'BRAND', 'ACCOUNT', 'TRACKER CUSTOS',
                'SITE', 'EQUIPA', 'AGENT', 'MOEDA', 'VALOR FINAL']]

VE = df_VE1[['BICODE', 'BRAND', 'ACCOUNT', 'TRACKER CUSTOS',
             'SITE', 'EQUIPA', 'AGENT', 'MOEDA', 'VALOR FINAL']]

JLS_RSA = df_JLS_RSA_1[['BICODE', 'BRAND', 'ACCOUNT', 'TRACKER CUSTOS',
                        'SITE', 'EQUIPA', 'AGENT', 'MOEDA', 'VALOR FINAL']]

SPN_Team = df_SPN_1[['BICODE', 'BRAND', 'ACCOUNT', 'TRACKER CUSTOS',
                     'SITE', 'EQUIPA', 'AGENT', 'MOEDA', 'VALOR FINAL']]

RB = df_RB1[['BICODE', 'BRAND', 'ACCOUNT', 'TRACKER CUSTOS',
             'SITE', 'EQUIPA', 'AGENT', 'MOEDA', 'VALOR FINAL']]

YES = df_YES1[['BICODE', 'BRAND', 'ACCOUNT', 'TRACKER CUSTOS',
               'SITE', 'EQUIPA', 'AGENT', 'MOEDA', 'VALOR FINAL']]

print("Colunas Mapeadas")

dataframes = [PMT, SPN_Team, G13, JLS_RSA, VE, HSTP, RB, YES]

print("DataFrame Geral Criada")

join = pd.concat(dataframes)

print("Concatenate das DataFrames feito")

join.to_excel("output.xlsx")

print("Tarefa Concluida")
