import pandas as pd

df1=pd.read_csv('C:/Users/Salvinanto7/Downloads/reg_csv.csv')
dict1=df1.to_dict()
df2=pd.read_csv('C:/Users/Salvinanto7/Downloads/feedback_csv.csv')
dict2=df2.to_dict()
dict3={}
dict1_val_list=list(map(lambda x:x.upper(),dict1['Name'].values()))

for key,val in dict2['Name'].items():
    if val.upper() in dict1_val_list:
        k=dict1_val_list.index(val.upper())
        if val not in dict3.keys():
            dict3[val.title()]=dict1['College'][k].title()
        else:
            dict3[val.title()+'_1']=dict1['College'][k].title()

#print(dict3)
#print(len(dict3))
df3=pd.DataFrame(data=dict3,index=[0])
df3=(df3.T)
df3.to_excel(r'C:/Users/Salvinanto7/Downloads/cert_details.xlsx')
