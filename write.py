import happybase
connection = happybase.Connection('hadoop-master')
table = connection.table('sayone_test')
table.put('row-key', {'o:qual1': 'Renjith', 'o:qual2': 'Raj'})
for k, data in table.scan():
  print k, data