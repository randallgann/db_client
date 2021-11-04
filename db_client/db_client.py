from dotenv import load_dotenv
load_dotenv()

import os, sys
import pyodbc
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# sql commands
hello_world = "PRINT 'Hello World!'"
create = "CREATE TABLE myfirsttable(ID INT NOT NULL)"
list_name = "SELECT * FROM sys.tables WHERE name = *"
search_objects = "SELECT * FROM sys.objects WHERE name = 'test_table'"
insert_row = "INSERT INTO myfirsttable (ID) VALUES (65981)"
get_rows_of_col = "SELECT ID FROM myfirsttable"

class azure_sql_db():
    
    EXIT_PASS, EXIT_FAIL = 0, 1

    def __init__(self, mode='normal'):
        
        self.server = os.environ.get('SERVER')
        self.database = os.environ.get('DATABASE')
        self.db_username = os.environ.get('DB_USERNAME')
        self.password = os.environ.get('PASSWORD')
        self.driver = os.environ.get('DRIVER')
        self.mode = mode

    def conn_cursor(self):

        with pyodbc.connect('DRIVER='+self.driver+';SERVER=tcp:'+self.server+';PORT=1433;DATABASE='+self.database+';UID='+self.db_username+';PWD='+self.password) as conn:
        #with pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:vvffyf3y2blyq.database.windows.net,1433;Database=SampleDB;Uid=sandbox;Pwd=C!$c0L!nuxPyth0n;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;') as conn:
            with conn.cursor() as cursor:
        
                #cursor.execute(insert_row)
                #print(cursor.messages) 
        
                cursor.execute(get_rows_of_col)
                row = cursor.fetchone()
                while row:
                    print(row[0])
                    row = cursor.fetchone()

                # i had an issue that took me a little while to figure out
                # cursor.messages was returning empty lists when I knew it 
                # should be returning results of queries
                # i had to recheck the microsoft docs and use the above fetchone() code
                # are we talking to and hearing back from the sql server
                # only use fetchone() with queries not insert commands
                #cursor.execute("PRINT 'Hello world!'")
                #print(cursor.messages)

                #cursor.execute("SELECT table_name, table_schema, table_type FROM information_schema.tables ORDER BY table_name ASC")
                #print(cursor.messages)

                # nvarchar used to store unicode - 8000 character max - this datatype used 
                # decimal(8,2) - first digit precision(total digits), second scale(digits to the right of decimal)
                # bool - 0,1 or NULL
                #cursor.execute("CREATE TABLE test_table(ID INT)")
                #print(cursor.messages)

                #cursor.execute("DESC test_table")
                #print(cursor.messages)