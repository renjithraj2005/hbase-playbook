import happybase

#First, make sure the thrift server is running:hbase thrift start

connection = happybase.Connection('hadoop-master')
print(connection.tables())
table = connection.table('user')

table.put('1',{'first_name': 'Renjith','last_name': 'Raj'})
print(table.row('1')) # {'f1:': 'hello'}