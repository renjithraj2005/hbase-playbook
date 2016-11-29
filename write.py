import happybase
connection = happybase.Connection('hadoop-master')
table = connection.table('sayone_test')
table.put('row-key', {'o:qual1': 'Renjith', 'o:qual2': 'Raj'})
table.put('row-key-2', {'o:qual1': 'Sayone', 'o:qual2': 'Test'})
for k, data in table.scan():
  print k, data