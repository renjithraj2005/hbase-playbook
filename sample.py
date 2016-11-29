import happybase

connection = happybase.Connection('hadoop-master')
table = connection.table('emp')

table.put('1',{'personal': 'Renjith'},{'professional': 'Renjith'})
print(table.row('1')) # {'f1:': 'hello'}