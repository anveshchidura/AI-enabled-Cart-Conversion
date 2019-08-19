# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 10:51:45 2019

@author: heame
"""



import pickle
import pandas as pd
#from itertools import permutations
import copy
import itertools


def sorted_pro(prod):
    sum1=[]
    sum0=[]
    sum2=[]
    sum3=[]
    sum4=[]
    for i in list(prod):
        if sum(i)==0:
            sum0.append(i)
        if sum(i)==1:
            sum1.append(i)
        if sum(i)==2:
            sum2.append(i)
        if sum(i)==3:
            sum3.append(i)
        if sum(i)==4:
            sum4.append(i)

    sorted_prod=sum4+sum3+sum2+sum1+sum0
    return sorted_prod

model = pickle.load(open("model.sav", 'rb'))
test=pd.DataFrame([[100,100,1,0,1,1,1,0]],index=[0],columns=["visitorid","itemid","confusion","shipping_charges","betterprice_elsewhere","delivery_charges","few_payment_options","trust"])
result = model.predict(test)

if result==0:
    input_lst=list(test.iloc[0])
    one_ind=[]
    for i in range(len(input_lst)):
        if input_lst[i]==1:
            one_ind.append(i)
#    req_lst=[input_lst[2]]+input_lst[4:-1]
    prod=itertools.product([1,0],repeat=len(one_ind))
    perm=sorted_pro(prod)
    for i in list(perm):
        test2=copy.deepcopy(test)
        for j in range(len(one_ind)):
            test2[test2.columns[one_ind[j]]][0]=i[j]
        upd_res=model.predict(test2)
        if upd_res==1:
            break

#
#itertools.product()
#
#
#
#prod=itertools.product([1,0], repeat=4)
#sum1=[]
#sum0=[]
#sum2=[]
#sum3=[]
#sum4=[]
#for i in list(prod):
#    if sum(i)==0:
#        sum0.append(i)
#    if sum(i)==1:
#        sum1.append(i)
#    if sum(i)==2:
#        sum2.append(i)
#    if sum(i)==3:
#        sum3.append(i)
#    if sum(i)==4:
#        sum4.append(i)
#
#sorted_prod=sum4+sum3+sum2+sum1+sum0
#    
#
#for i in list(prod):
#    print (list(i)) 
#
#
