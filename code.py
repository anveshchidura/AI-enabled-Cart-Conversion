import pandas as pd
import random
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

data=pd.read_csv("data.csv")



data2=data.loc[(data["event"] == "transaction") | (data["event"] == "addtocart")]
data2.reset_index(inplace=True)
data2.drop(columns = ["index"],axis = 1,inplace=True)
data3=data2.sort_values(['visitorid', 'itemid','transactionid'])
data3.reset_index(inplace=True)
data3.drop(columns = ["index"],axis = 1,inplace=True)



data4=data3.loc[data3["event"]=="transaction"]
trans_ind_list=list(data4.index)
count=0
for i in trans_ind_list:
    if data3.iloc[i-count+1, 3]!=data3.iloc[i-count, 3]:
        data3=data3.drop(i-count,axis=0)
        data3.reset_index(inplace=True)
        data3.drop(columns=["index"],axis=1,inplace=True)
        count=count+1
transaction=[0 for i in list(data3.index)]
for i in list(data3.index):
    if data3["event"][i]=="transaction":
        transaction[i+1]=1

data3["revenue_generated"]=transaction



data5=data3.loc[data3["event"]=="addtocart"]
data5.reset_index(inplace=True)
data5.drop(columns=["transactionid","index","timestamp"],axis=1,inplace=True)





addtocart = list((data5[data5["revenue_generated"]==0]).index)
len(addtocart)

atoc = random.sample(addtocart,k=25125)

justbrowsing = [0]*69332
for i in atoc:
   justbrowsing[i] = 1

data5["justbrowsing"] = justbrowsing

atoc2 = random.sample(addtocart,k=10050)
atoc3 = random.sample(addtocart,k=4522)
atoc4 = random.sample(addtocart,k=4020)
atoc5 = random.sample(addtocart,k=2512)
atoc6 = random.sample(addtocart,k=11557)

high_shipping_price = [0]*69332
better_price_elsewhere = [0]*69332
delivery_time = [0]*69332
payment_options = [0]*69332
other_reasons = [0]*69332

for i in atoc2:
    high_shipping_price[i] = 1
for i in atoc3:
    better_price_elsewhere[i] = 1
for i in atoc4:
    delivery_time[i] = 1
for i in atoc5:
    payment_options[i] = 1
for i in atoc6:
    other_reasons[i] = 1

data5["high_shipping_price"] = high_shipping_price
data5["better_price_elsewhere"] = better_price_elsewhere
data5["delivery_time"] = delivery_time
data5["payment_options"] = payment_options
data5["other_reasons"] = other_reasons


data5 = data5.drop("event",axis =1)

data5 = data5.rename(columns = {"transaction":"revenue_generated"})

transaction = list((data5[data5["revenue_generated"]==1]).index)

trans1 = random.sample(transaction,k=1908)
trans2 = random.sample(transaction,k=3816)
trans3 = random.sample(transaction,k=7632)
trans4 = random.sample(transaction,k=5724)
trans5 = random.sample(transaction,k=9541)
trans6 = random.sample(transaction,k=5724)

justbrowsing1 = [0]*69332
high_shipping_price1 = [0]*69332
better_price_elsewhere1 = [0]*69332
delivery_time1 = [0]*69332
payment_options1 = [0]*69332
other_reasons1 = [0]*69332

for i in trans1:
    justbrowsing1[i] = 1
for i in trans2:
    high_shipping_price1[i] = 1
for i in trans3:
    better_price_elsewhere1[i] = 1
for i in trans4:
    delivery_time1[i] = 1
for i in trans5:
    payment_options1[i] = 1
for i in trans6:
    other_reasons1[i] = 1

data5["justbrowsing1"] = justbrowsing1

data5["high_shipping_price1"] = high_shipping_price1
data5["better_price_elsewhere1"] = better_price_elsewhere1
data5["delivery_time1"] = delivery_time1
data5["payment_options1"] = payment_options1
data5["other_reasons1"] = other_reasons1

data5["just_browsing"] = data5["justbrowsing"] + data5["justbrowsing1"]
data5["shipping_charges"] = data5["high_shipping_price1"] + data5["high_shipping_price"]
data5["betterprice_elsewhere"] = data5["better_price_elsewhere1"] + data5["better_price_elsewhere"]
data5["delivery_charges"]= data5["delivery_time1"] + data5["delivery_time"]
data5["few_payment_options"]=data5["payment_options1"] + data5["payment_options"]
data5["otherreasons"] = data5["other_reasons1"]+data5["other_reasons"]

data5 = data5.drop(columns = {"justbrowsing","justbrowsing1","high_shipping_price1","high_shipping_price","better_price_elsewhere1","better_price_elsewhere","delivery_time1","delivery_time","payment_options","payment_options1","other_reasons","other_reasons1"},axis=1)

for i in data5.index:
    row=list(data5.iloc[i])[3:]
    if 1 not in row:
        data5["revenue_generated"][i]=1
    elif 0 not in row:
        data5["revenue_generated"][i]=0

revenue = list(data5["revenue_generated"])
y = pd.DataFrame({"revenue_generated" :revenue})
x = data5.drop("revenue_generated",axis=1)





x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 42, shuffle = True,train_size = 0.8)
# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(x_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(x_test)


print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

