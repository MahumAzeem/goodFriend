from pydantic import BaseModel
from friend import Friend
from connect_database import Database
import datetime

class addFriend:
    def add(self, Friend):
        #Name and birthdate are mandatory
        #DB format: riend_information ( id UUID PRIMARY KEY, name text, birthdate text, pronouns text, 
            #allergies text, phone_number text, col1_name text, col1_info text, col2_name text, col2_info text, 
            #col3_name text, col3_info text, col4_name text, col4_info text);

        cql_columns = "id"
        cql_values = "uuid()"
        optional_counter = 1

        parameters = ["name", "birthdate", "allergies", "phone_number", "pronouns", "avatar", "optional1", "optional2", "optional3", "optional4"]
        for key in Friend:
            if key[1]:
                information = key[1]
                if 'optional' in key[0]:
                    info_list = list(information.items())
                    cql_columns = cql_columns + ", col" + str(optional_counter) +"_name, col" + str(optional_counter) +"_info"
                    cql_values = cql_values + ", '" + info_list[0][0] + "', '"+ info_list[0][1] +"'"
                    optional_counter += optional_counter
                else:
                    if key[0] == 'birthdate':
                        dts = key[1]
                        information = dts.strftime('%Y/%m/%d')
                    cql_columns = cql_columns + ", " + key[0]
                    cql_values = cql_values + ", '" + information + "'"

        cql_command = "insert into friend_information (" + cql_columns + ") values ( " + cql_values + ")"
        #print(cql_command)

        newDatabase = Database()
        newDatabase.execute(cql_command)
        newDatabase.close()


#f = addFriend()
#friend = Friend(name= "stella brown", birthdate= 2000-10-10, allergies="apples", pronouns = "she", optional1 = {"Snacks": "Gummy bears"}, optional2 = {"Interests": "Plants"})
#f.add(friend)
