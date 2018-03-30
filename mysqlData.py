import mysql.connector

class mysqlData():
    def setMysqlData(self,user,password,host,database_name):
        self.user = user
        self.password = password
        self.host = host
        self.database_name = database_name
        return self

    def connectMySQL(self,mysqldt,command):
        try:
            cnx = mysql.connector.connect(user=mysqldt.user,password=mysqldt.password,host=mysqldt.host,database=mysqldt.database_name)
            cursor = cnx.cursor()
            cursor.execute(command)
            tabelas = []
            for item in cursor:
                tabelas.append(item)
            return tabelas
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            print err
            return False

    def convertDataStructure(self,mysqldt,table_name):
        structure = self.connectMySQL(mysqldt,"desc "+table_name)
        data_struct = "create table "+table_name+"("
        for item in structure: #it will only convert the most common types, like int, varchar and datetime
            data_struct+=item[0]+" "+item[1]+",\r\n"
        if data_struct.endswith(","):
            data_struct=data_struct[:-1]
        data_struct+=");\r\n"
        return data_struct

    def convertData(self,mysqldt,table_name):
        data = self.connectMySQL(mysqldt,"select * from "+table_name)
        table_data = " -- Data\r\n"
        for item in data:
            tamanho = len(item)
            table_data += "insert into "+table_name+" values"+str((item[0:tamanho-1]))+";\r\n"
        return table_data
