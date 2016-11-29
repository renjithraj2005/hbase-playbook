import happybase

#First, make sure the thrift server is running:hbase thrift start

connection = happybase.Connection('hadoop-master')
print(connection.tables())
table = connection.table('emp')

table.put('1',{'personal': 'Renjith'},{'professional': 'Renjith'})
print(table.row('1')) # {'f1:': 'hello'}