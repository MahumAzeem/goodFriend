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
        self.session = self.cluster.connect('friends')
    
    def execute(self, command):
        #REVISIT FOR INPUT SANITIZATION
        row = self.session.execute(command).one()
        #if row:
        #    print(row[0])
        #else:
        #    print("An error occurred.")

    def close(self):
        self.cluster.shutdown()
        self.session.shutdown()


#Using the function
#newDatabase = Database()
#newDatabase.execute("insert into friend_information ( id, name, birthday, pronouns, allergies) Values ( uuid(), 'Alice Smith', 1368438171000, 'She/her', 'Peanuts')")
#newDatabase.close()

#insert into friend_information ( id, name, birthday, pronouns, allergies, col1_name, col1_info, col2_name, col2_info, col3_name, col3_info, col4_name, col4_info) Values ( uuid(), 'Alice Smith', 1368438171000, 'She/her', 'Peanuts', ...);