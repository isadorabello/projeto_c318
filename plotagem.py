import matplotlib.pyplot as plt
import seaborn as sns

def plt_planos_vendidos(dataset):
    plt.figure(figsize=(10, 6))
    sns.histplot(dataset['ID_PLANO'], bins=30, kde=True)
    plt.title('Distribuição dos Planos Vendidos')
    plt.xlabel('Planos Vendidos')
    plt.show()



def plt_valor_mensalidade(dataset):
    plt.figure(figsize=(10, 6))
    sns.histplot(dataset['VCM'], bins=30, kde=True)
    plt.title('Distribuição dos Valores de Mensalidade')
    plt.xlabel('Valor da Mensalidade')
    plt.show()

def plt_faixa_etaria(dataset):
    plt.figure(figsize=(10, 6))
    sns.histplot(dataset['CD_FAIXA_ETARIA'], bins=30, kde=True)
    plt.title('Distribuição de Vendas por faixas de idade')
    plt.xlabel("""Faixa etária
            (01)  00 (zero) a 18 (dezoito) anos;
            (02)  19 (dezenove) a 23 (vinte e três) anos;
            (03)  24 (vinte e quatro) a 28 (vinte e oito) anos;
            (04)  29 (vinte e nove) a 33 (trinta e três) anos;
            (05)  34 (trinta e quatro) a 38 (trinta e oito) anos;
            (06)  39 (trinta e nove) a 43 (quarenta e três) anos;
            (07)  44 (quarenta e quatro) a 48 (quarenta e oito) anos;
            (08)  49 (quarenta e nove) a 53 (cinquenta e três) anos;
            (09)  54 (cinquenta e quatro) a 58 (cinquenta e oito) anos;
            (10)  59 (cinquenta e nove) anos ou mais.""")
    plt.show()

def plt_por_regiao(dataset):
    plt.figure(figsize=(10, 6))
    sns.histplot(dataset['NM_REGIAO'], bins=30, kde=True)
    plt.title('Distribuição das vendas pelas regiões do Brasil')
    plt.xlabel('Vendas por regiões')
    plt.show()

def plt_vendas_por_estado(dataset):
    plt.figure(figsize=(10, 6))
    sns.histplot(dataset['SG_UF'], bins=30, kde=True)
    plt.title('Distribuição das vendas pelos estados brasileiros')
    plt.xlabel('Vendas por estados brasileiros')
    plt.show()

def plt_tipo_x_mensalidade(dataset):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='ID_PLANO', y='VCM', data=dataset)
    plt.title('Relação entre Tipo do plano(ID plano) e Valor da Mensalidade')
    plt.xlabel('Tipo do plano (ID)')
    plt.ylabel('Valor da Mensalidade')
    plt.show()

def plt_tipo_x_idade(dataset):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='CD_FAIXA_ETARIA', y='ID_PLANO', data=dataset)
    plt.title('Relação entre Faixa Etária e Tipo do plano(ID plano)')
    plt.xlabel("""Faixa etária
                (01)  00 (zero) a 18 (dezoito) anos;
                (02)  19 (dezenove) a 23 (vinte e três) anos;
                (03)  24 (vinte e quatro) a 28 (vinte e oito) anos;
                (04)  29 (vinte e nove) a 33 (trinta e três) anos;
                (05)  34 (trinta e quatro) a 38 (trinta e oito) anos;
                (06)  39 (trinta e nove) a 43 (quarenta e três) anos;
                (07)  44 (quarenta e quatro) a 48 (quarenta e oito) anos;
                (08)  49 (quarenta e nove) a 53 (cinquenta e três) anos;
                (09)  54 (cinquenta e quatro) a 58 (cinquenta e oito) anos;
                (10)  59 (cinquenta e nove) anos ou mais.""")
    plt.ylabel('Tipo do plano (ID)')
    plt.show()


def plt_tipo_x_estados(dataset):
    plt.figure(figsize=(15, 6))
    plt.subplot(1, 2, 1)
    sns.scatterplot(x='ID_PLANO', y='NM_REGIAO', data=dataset)
    plt.title('Relação entre Tipo do plano(ID plano) e Regiões Brasileiras')
    plt.xlabel('Tipo do plano (ID)')
    plt.ylabel('Regiões Brasileiras')
    plt.subplot(1, 2, 2)
    sns.scatterplot(x='ID_PLANO', y='SG_UF', data=dataset)
    plt.title('Relação entre Tipo do plano(ID plano) e Estados Brasileiros')
    plt.xlabel('Tipo do plano (ID)')
    plt.ylabel('Estados Brasileiros')
    plt.show()

def plt_idade_x_mensalidade(dataset):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='CD_FAIXA_ETARIA', y='VCM', data=dataset)
    plt.title('Relação entre Faixa Etária e Valor da Mensalidade')
    plt.xlabel("""Faixa etária
                (01)  00 (zero) a 18 (dezoito) anos;
                (02)  19 (dezenove) a 23 (vinte e três) anos;
                (03)  24 (vinte e quatro) a 28 (vinte e oito) anos;
                (04)  29 (vinte e nove) a 33 (trinta e três) anos;
                (05)  34 (trinta e quatro) a 38 (trinta e oito) anos;
                (06)  39 (trinta e nove) a 43 (quarenta e três) anos;
                (07)  44 (quarenta e quatro) a 48 (quarenta e oito) anos;
                (08)  49 (quarenta e nove) a 53 (cinquenta e três) anos;
                (09)  54 (cinquenta e quatro) a 58 (cinquenta e oito) anos;
                (10)  59 (cinquenta e nove) anos ou mais.""")
    plt.ylabel('Valor da Mensalidade')
    plt.show()


def plt_regiao_x_mensalidade(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='NM_REGIAO', y='VCM', data=data)
    plt.title('Relação entre Regiões Brasileiras e Valor da Mensalidade')
    plt.xlabel('Regiões Brasileiras')
    plt.ylabel('Valor da Mensalidade')
    plt.show()

def plt_estado_x_mensalidade(dataset):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='SG_UF', y='VCM', data=dataset)
    plt.title('Relação entre Estados Brasileiro e Valor da Mensalidade')
    plt.xlabel('Estados Brasileiros')
    plt.ylabel('Valor da Mensalidade')
    plt.show()

def plt_idade_x_estado(dataset):
    plt.figure(figsize=(15, 6))
    plt.subplot(1, 2, 1)
    sns.scatterplot(x='CD_FAIXA_ETARIA', y='NM_REGIAO', data=dataset)
    plt.title('Relação entre Faixa Etária e Regiões Brasileiras')
    plt.xlabel('Faixa etária')
    plt.ylabel('Regiões Brasileiras')
    plt.subplot(1, 2, 2)
    sns.scatterplot(x='CD_FAIXA_ETARIA', y='SG_UF', data=dataset)
    plt.title('Relação entre Faixa Etária e Estados Brasileiros')
    plt.xlabel('Faixa etária')
    plt.ylabel('Estados Brasileiros')
    plt.text(-12, 40,"""Faixa etária
                (01)  00 (zero) a 18 (dezoito) anos;
                (02)  19 (dezenove) a 23 (vinte e três) anos;
                (03)  24 (vinte e quatro) a 28 (vinte e oito) anos;
                (04)  29 (vinte e nove) a 33 (trinta e três) anos;
                (05)  34 (trinta e quatro) a 38 (trinta e oito) anos;
                (06)  39 (trinta e nove) a 43 (quarenta e três) anos;
                (07)  44 (quarenta e quatro) a 48 (quarenta e oito) anos;
                (08)  49 (quarenta e nove) a 53 (cinquenta e três) anos;
                (09)  54 (cinquenta e quatro) a 58 (cinquenta e oito) anos;
                (10)  59 (cinquenta e nove) anos ou mais.""")
    plt.show()


def plt_concentracao_geral(lat_long):
    lat_long.plot(kind='scatter', x='longitude', y='latitude')

def plt_concentracao_regiao(lat_long):
    lat_long.plot(kind='scatter', x='longitude', y='latitude')

def plt_concentracao_uf(lat_long):
    lat_long.plot(kind='scatter', x='longitude', y='latitude')

def plt_concentracao_cidade(data):
    data.plot(kind='scatter', x='longitude', y='latitude')
    plt.show()

def plt_mensalidade_x_regiao(data, regiao):
    plt.figure(figsize=(16, 20))
    plt.subplot(3, 2, 1)
    sns.histplot(data['VCM'], bins=30, kde=True)
    plt.title('Relação entre quantidade de assinantes e Valor da Mensalidade')
    plt.xlabel('Valor da Mensalidade')
    plt.ylabel('Quantidade de assinantes')
    plt.subplot(3, 2, 2)
    sns.histplot(data['ID_PLANO'], bins=30, kde=True)
    plt.title('Relação entre quantidade de assinantes e Tipo do plano(ID plano)')
    plt.xlabel('Tipo do plano (ID)')
    plt.ylabel('Quantidade de assinantes')
    plt.subplot(3, 2, 3)
    sns.histplot(data['CD_FAIXA_ETARIA'], bins=30, kde=True)
    plt.title('Relação entre quantidade de assinantes e Faixa Etária')
    plt.xlabel('Faixa Etária')
    plt.ylabel('Quantidade de assinantes')
    plt.subplot(3, 2, 4)
    sns.scatterplot(x='CD_FAIXA_ETARIA', y='VCM', data=data)
    plt.title('Relação entre Valor da Mensalidade e Faixa Etária')
    plt.xlabel('Faixa Etária')
    plt.ylabel('Valor da Mensalidade')
    plt.subplot(3, 2, 5)
    sns.scatterplot(x='CD_FAIXA_ETARIA', y='ID_PLANO', data=data)
    plt.title('Relação entre Tipo do plano(ID plano) e Faixa Etária')
    plt.xlabel('Faixa Etária')
    plt.ylabel('Tipo do plano(ID plano)')
    plt.subplot(3, 2, 6)
    sns.scatterplot(x='ID_PLANO', y='VCM', data=data)
    plt.title('Relação entre Tipo do plano(ID plano) e Valor da Mensalidade')
    plt.xlabel('Tipo do plano(ID plano)')
    plt.ylabel('Valor da Mensalidade')
    print(f"""Região analisada: {regiao}
            
            Faixa etária
                (01)  00 (zero) a 18 (dezoito) anos;
                (02)  19 (dezenove) a 23 (vinte e três) anos;
                (03)  24 (vinte e quatro) a 28 (vinte e oito) anos;
                (04)  29 (vinte e nove) a 33 (trinta e três) anos;
                (05)  34 (trinta e quatro) a 38 (trinta e oito) anos;
                (06)  39 (trinta e nove) a 43 (quarenta e três) anos;
                (07)  44 (quarenta e quatro) a 48 (quarenta e oito) anos;
                (08)  49 (quarenta e nove) a 53 (cinquenta e três) anos;
                (09)  54 (cinquenta e quatro) a 58 (cinquenta e oito) anos;
                (10)  59 (cinquenta e nove) anos ou mais.""")
    plt.show()


def plt_tipo_x_mensalidade_estado(data, uf, regiao):
    plt.figure(figsize=(16, 20))
    plt.subplot(3, 2, 1)
    sns.histplot(data
    ['VCM'], bins=30, kde=True)
    plt.title('Relação entre quantidade de assinantes e Valor da Mensalidade')
    plt.xlabel('Valor da Mensalidade')
    plt.ylabel('Quantidade de assinantes')
    plt.subplot(3, 2, 2)
    sns.histplot(data
    ['ID_PLANO'], bins=30, kde=True)
    plt.title('Relação entre quantidade de assinantes e Tipo do plano(ID plano)')
    plt.xlabel('Tipo do plano (ID)')
    plt.ylabel('Quantidade de assinantes')
    plt.subplot(3, 2, 3)
    sns.histplot(data
    ['CD_FAIXA_ETARIA'], bins=30, kde=True)
    plt.title('Relação entre quantidade de assinantes e Faixa Etária')
    plt.xlabel('Faixa Etária')
    plt.ylabel('Quantidade de assinantes')
    plt.subplot(3, 2, 4)
    sns.scatterplot(x='CD_FAIXA_ETARIA', y='VCM', data=data
    )
    plt.title('Relação entre Valor da Mensalidade e Faixa Etária')
    plt.xlabel('Faixa Etária')
    plt.ylabel('Valor da Mensalidade')
    plt.subplot(3, 2, 5)
    sns.scatterplot(x='CD_FAIXA_ETARIA', y='ID_PLANO', data=data
    )
    plt.title('Relação entre Tipo do plano(ID plano) e Faixa Etária')
    plt.xlabel('Faixa Etária')
    plt.ylabel('Tipo do plano(ID plano)')
    plt.subplot(3, 2, 6)
    sns.scatterplot(x='ID_PLANO', y='VCM', data=data
    )
    plt.title('Relação entre Tipo do plano(ID plano) e Valor da Mensalidade')
    plt.xlabel('Tipo do plano(ID plano)')
    plt.ylabel('Valor da Mensalidade')
    print(f"""Estado analisado: {uf} - {regiao}
            
            Faixa etária
                (01)  00 (zero) a 18 (dezoito) anos;
                (02)  19 (dezenove) a 23 (vinte e três) anos;
                (03)  24 (vinte e quatro) a 28 (vinte e oito) anos;
                (04)  29 (vinte e nove) a 33 (trinta e três) anos;
                (05)  34 (trinta e quatro) a 38 (trinta e oito) anos;
                (06)  39 (trinta e nove) a 43 (quarenta e três) anos;
                (07)  44 (quarenta e quatro) a 48 (quarenta e oito) anos;
                (08)  49 (quarenta e nove) a 53 (cinquenta e três) anos;
                (09)  54 (cinquenta e quatro) a 58 (cinquenta e oito) anos;
                (10)  59 (cinquenta e nove) anos ou mais.""")
    plt.show()

def plt_tipo_x_mensalidade_cidade(data, c_escolhida, uf, regiao):
    plt.figure(figsize=(16, 20))
    plt.subplot(3, 2, 1)
    sns.histplot(data['VCM'], bins=30, kde=True)
    plt.title('Relação entre quantidade de assinantes e Valor da Mensalidade')
    plt.xlabel('Valor da Mensalidade')
    plt.ylabel('Quantidade de assinantes')
    plt.subplot(3, 2, 2)
    sns.histplot(data['ID_PLANO'], bins=30, kde=True)
    plt.title('Relação entre quantidade de assinantes e Tipo do plano(ID plano)')
    plt.xlabel('Tipo do plano (ID)')
    plt.ylabel('Quantidade de assinantes')
    plt.subplot(3, 2, 3)
    sns.histplot(data['CD_FAIXA_ETARIA'], bins=30, kde=True)
    plt.title('Relação entre quantidade de assinantes e Faixa Etária')
    plt.xlabel('Faixa Etária')
    plt.ylabel('Quantidade de assinantes')
    plt.subplot(3, 2, 4)
    sns.scatterplot(x='CD_FAIXA_ETARIA', y='VCM', data=data)
    plt.title('Relação entre Valor da Mensalidade e Faixa Etária')
    plt.xlabel('Faixa Etária')
    plt.ylabel('Valor da Mensalidade')
    plt.subplot(3, 2, 5)
    sns.scatterplot(x='CD_FAIXA_ETARIA', y='ID_PLANO', data=data)
    plt.title('Relação entre Tipo do plano(ID plano) e Faixa Etária')
    plt.xlabel('Faixa Etária')
    plt.ylabel('Tipo do plano(ID plano)')
    plt.subplot(3, 2, 6)
    sns.scatterplot(x='ID_PLANO', y='VCM', data=data)
    plt.title('Relação entre Tipo do plano(ID plano) e Valor da Mensalidade')
    plt.xlabel('Tipo do plano(ID plano)')
    plt.ylabel('Valor da Mensalidade')
    print(f"""Município analisado: {c_escolhida} - {uf} - {regiao}
            
            Faixa etária
                (01)  00 (zero) a 18 (dezoito) anos;
                (02)  19 (dezenove) a 23 (vinte e três) anos;
                (03)  24 (vinte e quatro) a 28 (vinte e oito) anos;
                (04)  29 (vinte e nove) a 33 (trinta e três) anos;
                (05)  34 (trinta e quatro) a 38 (trinta e oito) anos;
                (06)  39 (trinta e nove) a 43 (quarenta e três) anos;
                (07)  44 (quarenta e quatro) a 48 (quarenta e oito) anos;
                (08)  49 (quarenta e nove) a 53 (cinquenta e três) anos;
                (09)  54 (cinquenta e quatro) a 58 (cinquenta e oito) anos;
                (10)  59 (cinquenta e nove) anos ou mais.""")
    plt.show()
