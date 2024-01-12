"""
    Conexão com SQL Server e inserção de dados
 
 """

import pyodbc

from config import db_config
import mysql.connector

# Acesse as credenciais do arquivo de configuração
db_host = db_config['host']
db_user = db_config['user']
db_password = db_config['password']
db_name = db_config['database']

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+db_host+';DATABASE='+db_name+';UID='+db_user+';PWD='+db_password)
cursor = cnxn.cursor()


def insere(dados):
        try:
      
            cursor = cnxn.cursor()
            cursor.execute("truncate table CONTROLE_DIFAL")
        
            for index, row in dados.iterrows():
                cursor.execute("INSERT INTO CONTROLE_DIFAL (filial, nota_fiscal, data_cadastro, cliente, cfop, descricao_op, valor, difal, fcp, juros_multa, uf, total, percentual, controle_pagamento, data_pagamento, nfd, valor_nfd) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?); ", 
                            (row.Filial), (row.Nota_Fiscal), (row.Data), (row.Cliente), (row.CFOP), (row.Descriçao_da_Operaçao), (row.Valor), (row.Difal), (row.FCP), (row.JUROS_MULTA), (row.UF), (row.Total), (row.Percentual), (row.Controle_de_Pagamento), (row.Data_Pagamento), (row.NFD), (row.Valor_NFD))
            
            cnxn.commit()
        except Exception as e:
            print(f"Error: ", e)

def atualiza():
    try:
        """
            UPDATE CONTROLE_DIFAL SET
        """
    except Exception as e:
            print(f"Error: ", e)




#consulta()