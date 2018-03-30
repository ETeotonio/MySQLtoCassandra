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
        data_struct = "create table "+mysqldt.database_name+"."+table_name+"("
        for item in structure: #it will only convert the most common types, like int, varchar and datetime
            if str(item[1]).startswith("int"):
                data_struct+=item[0]+" int,\n"
            elif str(item[1]).startswith("varchar"):
                data_struct+=item[0]+" text,\n"
            elif str(item[1]).startswith("enum"):
                data_struct+=item[0]+" "+str(item[1]).replace("(","{").replace(")","}")
            else:
                data_struct += item[0] + " " + item[1] + ",\n"
        if data_struct.endswith(",\n"):
            data_struct=data_struct[:-2]
        data_struct+=");\n"
        return data_struct

    def convertData(self,mysqldt,table_name):
        data = self.connectMySQL(mysqldt,"select * from "+table_name)
        table_data = " -- Data\n"
        for item in data:
            tamanho = len(item)
            table_data += "insert into "+table_name+" values"+str((item[0:tamanho-1]))+";\n"
        return table_data
