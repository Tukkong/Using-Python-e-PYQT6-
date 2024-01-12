import sys
from datetime import datetime
from pathlib import Path

import pandas as pd
from PySide6.QtWidgets import (QFileDialog,
                               QApplication, QMainWindow, QTableWidgetItem, QLineEdit)

import database as db
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.combo_box = None
        self.setupUi(self)
        self.edit_line = QLineEdit(self)
        self.setWindowTitle("Aplicação Controle Difal")

        #self.tableWidget.cellClicked.connect(self.on_cell_clicked)

        # Create a button
        button = self.btnImport
        # Connect the button to the function
        button.clicked.connect(self.open_file_dialog)

        buttonListar = self.btnListar
        buttonListar.clicked.connect(self.consulta)

        buttonSalvar = self.btnSalvar
        buttonSalvar.clicked.connect(self.update_cell)

        self.comboBox2.addItems(['Selecione o item ', 'Pago', 'Pago Antecipadamente', 'Devolvido(Não Pagar)',
                                       'Devolvido(Restituir)', 'Não Pagar', 'Pago Parcial', 'Não Pagar 6949',
                                     'Pagar Parcial'])

    def update_cell(self):
        cursor = db.cnxn.cursor()
        selected_items = self.tableWidget.selectedItems()

        # if not selected_items:
        #     return

        selected_row = selected_items[0].row()
        selected_column = selected_items[0].column()
        selected_content = self.tableWidget.item(selected_row, selected_column).text()
        id_valor = self.tableWidget.item(selected_row, 0).text()

        try:
            #query = "UPDATE CONTROLE_DIFAL SET controle_pagamento = ? WHERE id= ?"
            cursor.execute("UPDATE CONTROLE_DIFAL SET controle_pagamento = ?  WHERE id= ?", selected_content, id_valor)
            cursor.commit()
        except Exception as e:
            print(f"Erro ao atualizar o banco de dados: {e}")
        print(f'Célula selecionada: ({selected_column}, {selected_column})')
        print(f'Contéudo selecionado: ({selected_content})')
        print(id_valor)


    # def combo(self):
    #     for row in range(self.tableWidget.columnCount()):
    #         self.combo_box = QComboBox()
    #         # for col in range(self.tableWidget.columnCount()):
    #         self.combo_box.addItems(['Selecione o item ', 'Pago', 'Pago Antecipadamente', 'Devolvido(Não Pagar)',
    #                                  'Devolvido(Restituir)', 'Não Pagar', 'Pago Parcial', 'Não Pagar 6949',
    #                                  'Pagar Parcial'])
    #
    #         self.tableWidget.setCellWidget(row, 14, self.combo_box)
    #
    #     # self.tableWidget.cellChanged.connect(self.salvar_opcao)

    def salvar_opcao(self):
        # Atualizar a opção no banco de dados ao fechar o aplicativo
        # for row in range(self.tableWidget.rowCount()):
            cursor = db.cnxn.cursor()
            row=0
            if self.on_cell_clicked:

                id_value = self.tableWidget.item(row, 0).text()

                opcao = self.comboBox2.currentText()

                # Atualizar no banco de dados
                cursor.execute("UPDATE CONTROLE_DIFAL SET controle_pagamento = ? WHERE id = ?", (opcao, id_value))
                cursor.commit()
            print(id_value)
            print(opcao)
            print(row)
            # Fechar a conexão com o banco de dados
            cursor.close()

    # Popula coluna Controle de Pagamento
    '''def pegaTextoCombo(self):
        for row in range(self.tableWidget.columnCount()):
            combo_box = QComboBox()
            combo_box.addItems([' ', 'Pago', 'Pago Antecipadamente', 'Devolvido(Não Pagar)',
                                'Devolvido(Restituir)', 'Não Pagar', 'Pago Parcial', 'Não Pagar 6949', 'Pagar Parcial'])
            combo_box.activated.connect(self.pegaTextoCombo)
            self.tableWidget.setCellWidget(row, 14, combo_box)
        valor = combo_box.currentText()
        print(valor)
        cursor = db.cnxn.cursor()
        sql = """INSERT INTO CONTROLE_DIFAL (controle_pagamento) VALUES (?)"""
        cursor.execute(sql, valor)
        cursor.close()'''

    def button_clicked(self):
        cursor = db.cnxn.cursor()
        item = self.tableWidget.currentItem()
        # linha_selecionada = self.tableWidget.currentRow()
        # coluna_selecionada = self.tableWidget.currentColumn()

        # update_query = f"UPDATE CONTROLE_DIFAL SET '{coluna_selecionada}' = ? WHERE {self.tableWidget.item(linha_selecionada, coluna_selecionada).text()}"
        # cursor.execute(update_query)
        # print(list(item))
        # print(coluna_selecionada)
        # print(linha_selecionada)
        # print(self.tableWidget.activated.connect(self.pegaTextoCombo))

    '''def cell_changed(self, row, col):
        # Capturar a mudança de célula e obter o ID da linha correspondente
        item_id = int(self.tableWidget.item(row, 0).text())

        # Obter o valor editado na célula
        new_value = self.tableWidget.item(row, col).text()

        # Atualizar o banco de dados com base no ID da linha e coluna alterada
        
        self.update_database(item_id, col, new_value)
        sinal = self.tableWidget.cellChanged
        
    def update_database(self, item_id, col, new_value):
        # Atualizar o banco de dados SQL Server com base no ID da linha e coluna alterada
        try:
            cursor = db.cnxn.cursor()
            # Construir a consulta de atualização dinâmica
            coluna = self.tableWidget.horizontalHeaderItem(col).text()
            print(coluna)
            update_query = f"UPDATE CONTROLE_DIFAL SET ? = ? WHERE id = ?"
            cursor.execute(update_query, coluna, new_value, item_id)
            cursor.commit()
            cursor.close()
            print("Atualização bem-sucedida!")

        except Exception as e:
            print(f"Erro ao atualizar o banco de dados: {e}")'''

    # Salvando atualizando toda a tabela
    def update_data(self):
        cursor = db.cnxn.cursor()
        for row in range(self.tableWidget.rowCount()):
            id_column = 0
            id_value = self.tableWidget.item(row, id_column).text()

            fcp = self.tableWidget.item(row, 9).text()
            juros_multa = self.tableWidget.item(row, 10).text()

            data_pagamento = self.tableWidget.item(row, 15).text()
            nfd = self.tableWidget.item(row, 16).text()
            valor_nfd = self.tableWidget.item(row, 17).text()
            observacao = self.tableWidget.item(row, 18).text()

            # Atualizar os dados no banco de dados
            try:
                cursor.execute("""UPDATE CONTROLE_DIFAL SET  
                                    fcp=?, juros_multa=?, 
                                    data_pagamento=?, nfd=?, valor_nfd=?, observacao=?
                                WHERE id=?""", (float(fcp), float(juros_multa),
                                                datetime.strptime(data_pagamento, '%d/%m/%Y'),
                                                int(nfd), float(valor_nfd), observacao, int(id_value)))
            except Exception as e:
                print(f"Erro ao atualizar o banco de dados: {e}")

                cursor.commit()
        #self.salvar_opcao()

    '''def combo(self):
        self.combo_box = QComboBox()
        lista = []
        for row in range(self.tableWidget.columnCount()):
            self.combo_box = QComboBox()
            self.combo_box.setEditable(True)
            #for col in range(self.tableWidget.columnCount()):
            self.combo_box.addItems([' ', 'Pago', 'Pago Antecipadamente', 'Devolvido(Não Pagar)',
                                'Devolvido(Restituir)', 'Não Pagar', 'Pago Parcial', 'Não Pagar 6949', 'Pagar Parcial'])
            
            self.tableWidget.setCellWidget(row, 14, self.combo_box)
        if self.tableWidget.currentCellChanged():
            cursor = db.cnxn.cursor()
            sql = """
                SELECT controle_pagamento
                    
                FROM dbo.CONTROLE_DIFAL cd
            """
            cursor.execute(sql)'''

    # Consulta no banco e preenche a Table Widget
    def consulta(self):
        cursor = db.cnxn.cursor()
        sql = """
            SELECT id
                ,filial
                ,nota_fiscal
                ,CONVERT(varchar(10), data_cadastro, 103) AS 'Data Cadastro'
                ,cliente
                ,cfop
                ,descricao_op
                ,valor
                ,difal
                ,fcp
                ,juros_multa
                ,uf
                ,ROUND((cd.difal + cd.fcp + cd.juros_multa), 2) as total
                ,CONCAT(ROUND((cd.total / NULLIF(cd.valor, 0)) * 100, 0), '%') AS percentual
                ,controle_pagamento
                ,CONVERT(varchar(10), data_pagamento, 103) AS 'Data de Pagamento'
                ,nfd
                ,valor_nfd
                ,observacao
            FROM dbo.CONTROLE_DIFAL cd
        """
        cursor.execute(sql)
        self.fetchall = cursor.fetchall()
        records = self.fetchall

        self.tableWidget.setRowCount(len(records))
        self.tableWidget.setColumnCount(len(records[0]))
        self.tableWidget.setColumnWidth(4, 300)
        self.tableWidget.setColumnWidth(3, 140)
        self.tableWidget.setColumnWidth(1, 50)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(2, 90)
        self.tableWidget.setColumnWidth(5, 50)
        self.tableWidget.setColumnWidth(6, 170)
        self.tableWidget.setColumnWidth(14, 200)
        self.tableWidget.setColumnWidth(15, 150)

        #self.combo()

        row_index = 0
        for value_tuple in records:
            col_index = 0
            for value in value_tuple:
                self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(value)))
                col_index += 1
            row_index += 1
        cursor.close()

    # Busca o arquivo e trata os dados para a inserção no SQL Server
    def open_file_dialog(self):
        filename, ok = QFileDialog.getOpenFileName(
            self,
            "Select a File",
            "${HOME}",
            "Data File (*.xlsx *.csv *.dat);; Docs (*.txt )"
        )
        if filename:
            caminho = Path(filename)
            print(caminho)
            data = pd.read_excel(caminho, sheet_name="Lançamentos")

            data['Data_Pagamento'] = data['Data_Pagamento'].fillna(" ", inplace=False)
            data['JUROS_MULTA'] = data['JUROS_MULTA'].fillna(0.00, inplace=False)
            data['Valor'] = data['Valor'].fillna(0.00, inplace=False)
            data['FCP'] = data['FCP'].fillna(0.0, inplace=False)
            data['Valor_NFD'] = data['Valor_NFD'].fillna(0.00, inplace=False)
            data['Controle_de_Pagamento'] = data['Controle_de_Pagamento'].fillna("Selecione", inplace=False)
            data['UF'] = data['UF'].fillna(" ", inplace=False)
            data['NFD'] = data['NFD'].fillna(" ", inplace=False)
            data['Observação'] = data['Observação'].fillna(" ", inplace=False)

            # data = data.fillna(0.0, inplace=False)
            data = round(data, 2)

            # print(data.info())
            # print(data.isnull().sum())

            db.insere(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    app.exec()
