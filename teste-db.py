import mysql.connector

cnx = mysql.connector.connect(user='root', password='admin',
                              host='127.0.0.1',
                              database='voipmonitor')

cursor = cnx.cursor()

query = ("select   id,  duration,  calldate,  caller,  called,  a_lost,  b_lost, lastSIPresponseNum  "
         "from cdr where lastSIPresponseNum=%s")


input_str = "8"
cursor.execute(query, (input_str,))

for id,  duration,  calldate,  caller,  called,  a_lost,  b_lost, lastSIPresponseNum  in cursor:
  print(id)
  print(duration)
  print(calldate)
  print(caller)
  print(called)
  print(a_lost)
  print(b_lost)
  print(lastSIPresponseNum)

cursor.close()
cnx.close()