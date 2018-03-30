import mysqlData

print "Welcome to MySQL to Cassandra Converter\r\n"
print "Powered by Me haha\r\n"
print "Let's start!"
def getValues():
    host = raw_input("Type the host you want to connect\r\n")
    user = raw_input("Type the username you will use to connect to database\r\n")
    password = raw_input("Type the "+user+"'s password, don't worry, your password will be only used in this session\r\n")
    database = raw_input("Type the database you want to convert\r\n")

    if (host and user and password and database):
        mysqlDT = mysqlData.mysqlData()
        mysqlDT.database_name = database
        mysqlDT.host = host
        mysqlDT.user = user
        mysqlDT.password = password
        dump = "create keyspace "+mysqlDT.database_name+" ;\r\n"
        tabelas = []
        tabelas = mysqlDT.connectMySQL(mysqlDT,"show tables")
        opt = raw_input("Do you want to list the tables? (Y/N)\r\n")
        if opt=="Y":
            print tabelas
        opt = raw_input("Type the table you want to convert\r\n")
        if opt:
            dump+=mysqlDT.convertDataStructure(mysqlDT,opt)
            dump+=mysqlDT.convertData(mysqlDT,opt)
            f = open(database+"-"+opt+"-toCassandra.nosql","a")
            f.write(dump)
            f.close()





        if tabelas == False:
            opt = raw_input("Error while connecting, do you want to retry?(Y\N)\r\n")
            if opt == "Y":
                getValues()
            else:
                exit()
    else:
        print ("I think you're missing something, let's try again\r\n")
        getValues()


getValues()