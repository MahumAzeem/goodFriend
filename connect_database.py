from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

import config

class Database:
    def __init__(self):
        path = config.DB_PATH
        user = config.USERNAME
        password = config.PASSWORD

        cloud_config= {
            'secure_connect_bundle': path,
            'init-query-timeout': 10,
            'connect_timeout': 10,
            'set-keyspace-timeout': 10
        }
        auth_provider = PlainTextAuthProvider(user, password)
        self.cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = self.cluster.connect('friends')
    
    def execute(self, command):
        #REVISIT FOR INPUT SANITIZATION
        row = self.session.execute(command)
        #if row:
        #    for x in row:
        #        print(x)
        #else:
        #    print("An error occurred.")
    
    def executeSelect(self, command):
        row = self.session.execute(command)
        if row:
            return row
        else:
            print("Select query returned nothing.")

    def close(self):
        self.cluster.shutdown()
        self.session.shutdown()

