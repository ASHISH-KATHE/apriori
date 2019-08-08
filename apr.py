# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 07:54:15 2019

@author: Ashish
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 06:59:06 2019

@author: Ashish
"""

import pandas as pd
list_rule=[]
n_tran=6
flag=True
pair_c=1
i=0
dataset=pd.read_csv('store.csv')
for row in dataset['items']:
	list_rule.append([])
	temp=row.split(',')
	for word in temp:
		list_rule[i].append(word)
	i=i+1

dist_items=[]

item_count=[]

i=0
j=0
while i<len(list_rule):
	j=0
	while j<len(list_rule[i]):
		if list_rule[i][j] not in dist_items or (i==0):
			dist_items.append(list_rule[i][j])
			item_count.append(1)
		else:
			item_count[dist_items.index(list_rule[i][j])]+=1
		j+=1
	i+=1
    
i=0
while i<len(item_count):
	if item_count[i]<n_tran:
		item_count.remove(item_count[i])
		dist_items.remove(dist_items[i])
		continue
	i=i+1
pair_l=[]
l_ind=-1
i=0
j=0
rule_book=[]
item_count=[]
k=0
temp=False
while flag:
    i=0
    j=0
    maxx=len(dist_items)
    k=pair_c
    while i<len(dist_items):
        j=i+1
        while j<len(dist_items):
                pair_l.append([])
                l_ind+=1
                pair_l[l_ind].append(dist_items[i])
                k=j
                while k<j+pair_c:
                    if k>=maxx and dist_items[k-maxx] not in pair_l[l_ind]:
                        #pair_l[l_ind].append(dist_items[k-maxx])
                        k=k
                    elif  k<maxx and dist_items[k] not in pair_l[l_ind]:
                        pair_l[l_ind].append(dist_items[k])
                    k+=1
                j+=1
        i+=1
    i=0
    k=0
    j=0
    while i<len(pair_l):
        if len(pair_l[i])==pair_c:
            pair_l[i]=set(pair_l[i])
            while j<len(list_rule):
                if pair_l[i].intersection(list_rule[j]) in rule_book :
                    item_count[rule_book.index(pair_l[i].intersection(list_rule[j]))]+=1
                    #print(pair_l[i].intersection(list_rule[j]))
                elif len(pair_l[i].intersection(list_rule[j]))==pair_c:
                    rule_book.append(pair_l[i].intersection(list_rule[j]))
                    print(pair_l[i].intersection(list_rule[j]))
                    item_count.append(1)
                    k+=1
                j+=1
        i+=1
    if len(rule_book)>0 and len(item_count)>0:
        print(rule_book)
        print(item_count)
    rule_book.clear()
    item_count.clear()
    if k<2 and pair_c>3:
        break
    pair_l.clear()
    l_ind=-1
    pair_c+=1
    
