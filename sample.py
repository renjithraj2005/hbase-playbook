# -*- coding: utf-8 -*-

import happybase

#First, make sure the thrift server is running:hbase thrift start


connection = happybase.Connection('hadoop-master')

connection.create_table(
    'sayone_test',
    {
     'o': dict(),  # use defaults
    }
)