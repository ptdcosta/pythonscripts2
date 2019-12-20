import pandas as pd

# Mapear os ficheiros recebidos
Custos_G13 = ''
Custos_AV = ''
Custos_SPN = ''
Custos_SPN_CEO = ''
Custos_YES = ''
Custos_PMT = ''
Custos_HSTP = ''
Custos_JR = ''
Custos_CA = ''
Custos_JLS = ''
Custos_JLS_RSA = ''
Custos_VE = ''
Custos_MAO = ''
Custos_RB = ''

print("Ficheiros Mapeados")

# Preparar ficheiros apagando linhas e colunas desnecessárias
df_G13_R = pd.read_excel(Custos_G13, header=19, skiprows=1)
df_G13 = df_G13_R.drop(df_G13_R.columns[0], axis=1)

df_AV_R = pd.read_excel(Custos_AV, header=19, skiprows=1)
df_AV = df_AV_R.drop(df_AV_R.columns[0], axis=1)

df_SPN_R = pd.read_excel(Custos_SPN, header=19, skiprows=1)
df_SPN = df_SPN_R.drop(df_SPN_R.columns[0], axis=1)

df_SPN_CEO_R = pd.read_excel(Custos_SPN_CEO, header=19, skiprows=1)
df_SPN_CEO = df_SPN_CEO_R.drop(df_SPN_CEO_R.columns[0], axis=1)

df_YES_R = pd.read_excel(Custos_YES, header=19, skiprows=1)
df_YES = df_YES_R.drop(df_YES_R.columns[0], axis=1)

df_PMT_R = pd.read_excel(Custos_PMT, header=19, skiprows=1)
df_PMT = df_PMT_R.drop(df_PMT_R.columns[0], axis=1)

df_HSTP_R = pd.read_excel(Custos_HSTP, header=19, skiprows=1)
df_HSTP = df_HSTP_R.drop(df_HSTP_R.columns[0], axis=1)

df_JR_R = pd.read_excel(Custos_JR, header=19, skiprows=1)
df_JR = df_JR_R.drop(df_JR_R.columns[0], axis=1)

df_CA_R = pd.read_excel(Custos_CA, header=19, skiprows=1)
df_CA = df_CA_R.drop(df_CA_R.columns[0], axis=1)

df_JLS_R = pd.read_excel(Custos_JLS, header=19, skiprows=1)
df_JLS = df_JLS_R.drop(df_JLS_R.columns[0], axis=1)

df_JLS_RSA_R = pd.read_excel(Custos_JLS_RSA, header=19, skiprows=1)
df_JLS_RSA = df_JLS_RSA_R.drop(df_JLS_RSA_R.columns[0], axis=1)

df_VE_R = pd.read_excel(Custos_VE, header=19, skiprows=1)
df_VE = df_VE_R.drop(df_VE_R.columns[0], axis=1)

df_MAO_R = pd.read_excel(Custos_MAO, header=19, skiprows=1)
df_MAO = df_MAO_R.drop(df_MAO_R.columns[0], axis=1)

df_RB_R = pd.read_excel(Custos_RB, header=19, skiprows=1)
df_RB = df_RB_R.drop(df_RB_R.columns[0], axis=1)

print("Colunas e Linhas Apagadas")
# Gerar ficheiros finais para next step
df_G13.to_excel("CustosG13_Output.xlsx")
df_AV.to_excel("CustosAV_Output.xlsx")
df_SPN.to_excel("CustosSPN_Output.xlsx")
df_SPN_CEO.to_excel("CustosSPN_CEO_Output.xlsx")
df_YES.to_excel("CustosYES_Output.xlsx")
df_PMT.to_excel("CustosPMT_Output.xlsx")
df_HSTP.to_excel("CustosHSTP_Output.xlsx")
df_JR.to_excel("CustosJR_Output.xlsx")
df_CA.to_excel("CustosCA_Output.xlsx")
df_JLS.to_excel("CustosJLS_Output.xlsx")
df_JLS_RSA.to_excel("CustosJLS_RSA_Output.xlsx")
df_VE.to_excel("CustosVE_Output.xlsx")
df_MAO.to_excel("CustosMAO_Output.xlsx")
df_RB.to_excel("CustosRB_Output.xlsx")
print("Ficheiro Intermédio Criado")
