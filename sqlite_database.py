from PyQt6.QtWidgets import QApplication
from PyQt6.QtSql import QSqlDatabase, QSqlQuery


def create_connection():
    # Inicializar a aplicação (necessário para usar o QtSql)
    app = QApplication([])

    # Nome da conexão (pode ser qualquer string)
    connection_name = "controle_difal.db"

    # Adicionar o driver SQLite
    db = QSqlDatabase.addDatabase("QSQLITE", connection_name)

    # Configurar o nome do banco de dados
    db.setDatabaseName("controle_difal")

    # Tentar abrir a conexão
    if not db.open():
        print("Erro ao abrir a conexão com o banco de dados.")
        return False

    print("Conexão com o banco de dados estabelecida com sucesso.")

    # Executar uma consulta de exemplo
    '''query = QSqlQuery(db)
    query.exec("CREATE TABLE IF NOT EXISTS example_table (id INTEGER PRIMARY KEY, name TEXT)")'''

    # Encerrar a conexão
    db.close()

    return True


def create_table():
    # Verifique se a conexão está aberta
    if not create_connection():
        return

    # Crie uma instância do QSqlQuery para executar consultas SQL
    query = QSqlQuery()

    # Defina a consulta SQL para criar uma tabela
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS controle_difal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filial INTEGER NULL,
            nota_fiscal INTEGER NULL,
            data_cadastro DATE NULL,
            cliente TEXT NULL,
            cfop INTEGER NULL,
            descricao_op TEXT NULL,
            valor REAL NULL,
            difal REAL NULL,
            fcp REAL NULL,
            juros_multa REAL NULL,
            uf TEXT NULL,
            total REAL NULL,
            percentual REAL NULL,
            controle_pagamento TEXT NULL,
            data_pagamento DATE,
            nfd INTEGER NULL,
            valor_nfd REAL NULL,
            observacao TEXT NULL
        );
    '''

    # Execute a consulta SQL
    if not query.exec(create_table_query):
        print(f"Erro ao criar a tabela: {query.lastError().text()}")
    else:
        print("Tabela criada com sucesso.")


# Chame a função para criar a tabela
create_table()

if __name__ == "__main__":
    if create_connection():
        print("Operações no banco de dados podem ser realizadas.")
