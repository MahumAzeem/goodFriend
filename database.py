from pydantic import BaseModel
from friend import Friend
from connect_database import Database
import datetime

class addFriend:
    def add(self, Friend):
        #Name and birthdate are mandatory

        cql_columns = "id"
        cql_values = "uuid()"

        parameters = ["name", "birthdate", "allergies", "pronouns", "avatar", "optional1", "optional2", "optional3", "optional4"]
        for key in Friend:
            if key[1]:
                information = key[1]
                if 'optional' in key[0]:
                    print(information)
                else:
                    if key[0] == 'birthdate':
                        dts = key[1]
                        information = dts.strftime('%Y/%m/%d')
                    cql_columns = cql_columns + ", " + key[0]
                    cql_values = cql_values + ", '" + information + "'"

        cql_command = "insert into friend_information (" + cql_columns + ") values ( " + cql_values + ")"
        print(cql_command)

#BIG PROBLEM!!!! HAD TO CONVERT THE DATETIME TO A STRING IN ORDER TO CONCAT!!!
#EITHER NEED TO DO A SEPARATE DB UPDATE, OR CHANGE THE DB COLUMN TO A STRING!!!

#        newDatabase = Database()
#        newDatabase.execute(cql_command)
#        newDatabase.close()


f = addFriend()
friend = Friend(name= "stella brown", birthdate= 2000-10-10, allergies="apples", pronouns = "he", optional1 = {"Snacks": "Gummy bears"})
f.add(friend)
