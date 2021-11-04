import unittest
import sys, os.path, re

sys.path.insert(0, '/home/randall/Dev/azure/db_client_processor/db_client')
bin_path = os.path.dirname(os.path.realpath(__file__))
lib_path = os.path.abspath(bin_path)

import db_client

class Testdb_client(unittest.TestCase):

    #def setUp(self):
    #    mode = 'unittest'
    #    self.app = db_client.azure_sql_db()
    
    def test_dbconnection(self):
        self.app = db_client.azure_sql_db()
        self.app.conn_cursor()
        # we have a working database connection

if __name__=='__main__':
    unittest.main()