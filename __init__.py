import mysqlData

print "Welcome to MySQL to Cassandra Converter\n"
print "Powered by Me haha\n"
print "Let's start!"
def getValues():
    host = raw_input("Type the host you want to connect\n")
    user = raw_input("Type the username you will use to connect to database\n")
    password = raw_input("Type the "+user+"'s password, don't worry, your password will be only used in this session\n")
    database = raw_input("Type the database you want to convert\n")

    if (host and user and password and database):
        mysqlDT = mysqlData.mysqlData()
        mysqlDT.database_name = database
        mysqlDT.host = host
        mysqlDT.user = user
        mysqlDT.password = password
        dump = "create keyspace "+mysqlDT.database_name+" with replication={'class' : 'SimpleStrategy', 'replication_factor' : 3;\n"
        dump += "use "+mysqlDT.database_name+";"
        tabelas = []
        tabelas = mysqlDT.connectMySQL(mysqlDT,"show tables")
        opt = raw_input("Do you want to list the tables? (Y/N)\n")
        if opt=="Y":
            print tabelas
        opt = raw_input("Type the table you want to convert\n")
        if opt:
            dump+=mysqlDT.convertDataStructure(mysqlDT,opt)
            dump+=mysqlDT.convertData(mysqlDT,opt)
            f = open(database+"-"+opt+"-toCassandra.cql","a")
            f.write(dump)
            f.close()
        if tabelas == False:
            opt = raw_input("Error while connecting, do you want to retry?(Y\N)\n")
            if opt == "Y":
                getValues()
            else:
                exit()
    else:
        print ("I think you're missing something, let's try again\n")
        getValues()


getValues()