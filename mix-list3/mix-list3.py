#!/usr/bin/env python3
list1 = ['cisco_nxos', 'arista_eos', 'cisco_ios']
print(list1)
#Let’s add an item to our list.
list1.extend(['juniper'])
print(list1)
#Let’s add a list within our list.
list1.append(['10.1.0.1', '10.2.0.1', '10.3.0.1'])
print(list1)
#Return the value of item 5 in list1.
print(list1[4]) 
#Let’s try printing the first IP address.
print(list1[4][0])