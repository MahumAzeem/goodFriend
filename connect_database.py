from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

class Database:
    def __init__(self):
        cloud_config= {
            'secure_connect_bundle': './secure-connect-goodfriend.zip',
            'init-query-timeout': 10,
            'connect_timeout': 10,
            'set-keyspace-timeout': 10
        }
        auth_provider = PlainTextAuthProvider('kanrieb', 'UVICgirls2020')
        self.cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = self.cluster.connect()
    
    def execute(self, command):
        #REVISIT FOR INPUT SANITIZATION
        row = self.session.execute(command).one()
        if row:
            print(row[1])
        else:
            print("An error occurred.")

    def close(self):
        self.cluster.shutdown()
        self.session.shutdown()


#Using the function
newDatabase = Database()
newDatabase.execute("SELECT * FROM system_schema.keyspaces")
newDatabase.close()