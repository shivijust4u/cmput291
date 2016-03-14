import sys
import cx_Oracle # the package used for accessing Oracle in Python
import getpass # the package for getting password from user without displaying it



class Database():
    """docstring for DataBase"""
    def __init__(self, statement):

        self.statement = statement

        # get username
        user = input("Username [%s]: " % getpass.getuser())
        if not user:
                user=getpass.getuser()
        
        # get password
        pw = getpass.getpass()

        # The URL we are connnecting to
        conString=''+user+'/' + pw +'@gwynne.cs.ualberta.ca:1521/CRS'
        
        self.connection = cx_Oracle.connect(conString)

        # create a cursor 
        self.curs = connection.cursor()

    def close_connection(self):
        self.curs.close()
        self.connection.close()


    def passive_update(self):

        try:        

            # Execute the desired statement 
            curs.execute(self.statement)
            connection.commit()
            return True

        except cx_Oracle.DatabaseError as exc:
            error, = exc.args
            print( sys.stderr, "Oracle code:", error.code)
            print( sys.stderr, "Oracle message:", error.message)
            return False


    def result_set_update(self):

        try:
            # Establish a connection in Python
            connection = cx_Oracle.connect(conString)

            # create a cursor 
            curs = connection.cursor()

            # Execute the desired statement 
            curs.execute(self.statement)
            connection.commit()

            # get all data and print it
            resultRows = curs.fetchall()
            for row in rows:
                print(row)
            
            # getting metadata
            resultRowsDescription = curs.description

            return [resultRows, resultRowsDescription]


        except cx_Oracle.DatabaseError as exc:
            error, = exc.args
            print( sys.stderr, "Oracle code:", error.code)
            print( sys.stderr, "Oracle message:", error.message)
            return [None, None]



