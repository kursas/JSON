import json
import sqlite3
from datetime import datetime

db = sqlite3.connect('mydb.sqlite')
with open('myJSON.json', encoding='utf-8-sig') as json_file:
    json_data = json.loads(json_file.read())

    # Aim of this block is to get the list of the columns in the JSON file.
    columns = []
    column = []
    for data in json_data:
        column = list(data.keys())
        for col in column:
            if col not in columns:
                columns.append(col)

    # Here we get values of the columns in the JSON file in the right order.
    value = []
    values = []
    for data in json_data:
        for i in columns:
            value.append(str(dict(data).get(i)))
        values.append(list(value))
        value.clear()

    # Time to generate the create and insert queries and apply it to the sqlite3 database
    create_query = "create table if not exists myTable ({0})".format(" text,".join(columns))
    insert_query = "insert into myTable ({0}) values(?{1})".format(", ".join(columns), ",?" * (len(columns)-1))
    print("insert has started at " + str(datetime.now()))
c = db.cursor()
c.execute(create_query)
c.executemany(insert_query, values)
values.clear()
db.commit()
c.close()
print("insert has completed at " + str(datetime.now()))

#output
insert has started at 2023-01-15 18:02:15.318610
insert has completed at 2023-01-15 18:02:15.338693

Process finished with exit code 0
