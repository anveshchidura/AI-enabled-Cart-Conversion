from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render_to_response
from dell.models import Proddesc
# Create your views here.
ids=[]
def home(request):
	return render(request,"Website/boot/index.html")

# def midpage(request):
# 	 return render(request,"test.html")	


# def display(request):
#   return render_to_response('template.tmpl', {'obj': Proddesc.objects.all()})

def bumbum(request):
	for i in request.POST:
	 	ids.append(i)
	 	while "csrfmiddlewaretoken" in ids: ids.remove("csrfmiddlewaretoken")  
	# 	#print(len(ids))
	print (ids)
	# h=Proddesc.objects.filter(productId=112)	
	# print("harsha")
	# print(h)
	# temp_list = []
	# for each_id in ids:
	# 	each_data = list(Proddesc.objects.filter(productId=each_id))
	# 	temp_list.append(each_data)
	#print(temp_list)
	lst=func()	

	if lst==[1]:
		return render_to_response('Website/boot/product_summary.html' )

	if lst==[2]:
		return render_to_response('Website/boot/product_summary1p.html' )

	if lst==[1,2]:
		return render_to_response('Website/boot/product_summaryboth.html')
	
	return render_to_response('Website/boot/product_summarynone.html')
	# else:	
	# 	return render(request,"table.html")

# print(ids)
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

def sol(colname):
	if(colname=="betterprice_elsewhere"):
		return 1
	if(colname=="deliveryTime"):
		return 2

	


def func():
	h=Proddesc.objects.filter(productId=int(ids[0]))
	pid=h[0].productId
	p1=h[0].site1
	p2=h[0].site2
	p3=h[0].site3
	p=h[0].price
	pricelist=[p1,p2,p3]
	print(pricelist)
	bp=0
	for i in pricelist:
		if (p>i):
			bp=1
	time=h[0].deliveryTime
	if(time>3):
		dt=1
	else:
		dt=0			
	model = pickle.load(open("C:\\Users\\lkvre\\Desktop\\dell\\hackath\\dell\\model.sav", 'rb'))
	lst=[100,pid,0,0,bp,dt,0,0]
	test=pd.DataFrame([lst],index=[0],columns=["visitorid","itemid","confusion","shipping_charges","betterprice_elsewhere","delivery_charges","few_payment_options","trust"])
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
	    print(i)
	    sollst=[]
	    for i in one_ind:
		    
		    if(test2[test2.columns[i]][0]==0):
		    	sollst.append(sol(test2.columns[i]))
	
	
	
	else:
		return []

	print(sollst)
	return sollst	
	# t=Proddesc.objects.filter(productId=pid)
	# t.            

