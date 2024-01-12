import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt
import pyodbc

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Editar Dados na Table Widget')
        self.setGeometry(100, 100, 600, 400)

        # Criar uma tabela e um botão para salvar
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Nome', 'Valor'])

        self.btnSalvar = QPushButton('Salvar Alterações', self)
        self.btnSalvar.clicked.connect(self.salvarAlteracoes)

        # Layout da janela
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.btnSalvar)

        self.setLayout(layout)

        # Conectar o sinal cellChanged ao método correspondente
        self.tableWidget.cellChanged.connect(self.cellChanged)

        # Preencher a tabela com dados do banco de dados
        self.carregarDadosDoBanco()

    def carregarDadosDoBanco(self):
        # Conectar ao banco de dados
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=172.16.22.212;'
                              'Database=CIGAM;'
                              'UID=sa;'
                              'PWD=Denteck@01')

        cursor = conn.cursor()

        # Executar consulta SQL para obter dados
        cursor.execute('SELECT * FROM CONTROLE_DIFAL')

        # Preencher a tabela com os dados do banco de dados
        row = 0
        for row_data in cursor.fetchall():
            self.tableWidget.insertRow(row)
            for col, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row, col, item)
            row += 1

        conn.close()

    def cellChanged(self, row, col):
        # Capturar a alteração da célula
        item = self.tableWidget.item(row, col)
        if item is not None:
            # Lógica para atualizar o banco de dados com a alteração
            id_coluna = int(self.tableWidget.item(row, 0).text())
            novo_valor = item.text()

            # Conectar ao banco de dados
            conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=172.16.22.212;'
                              'Database=CIGAM;'
                              'UID=sa;'
                              'PWD=Denteck@01')

            cursor = conn.cursor()

            # Executar consulta SQL para atualizar o valor na coluna específica
            query = f"UPDATE CONTROLE_DIFAL SET NomeDaColuna{col + 1} = ? WHERE ID = ?"
            cursor.execute(query, novo_valor, id_coluna)

            # Confirmar a transação e fechar a conexão
            conn.commit()
            conn.close()

    def salvarAlteracoes(self):
        # Método para salvar todas as alterações no banco de dados
        # (pode ser usado para implementar lógica adicional se necessário)
        print("Alterações salvas no banco de dados!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
