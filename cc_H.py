#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# import pathlib module
import pathlib
  


df=pd.read_excel(r'C:\\Users\\RTD SR_ 1\\Desktop\\NGCM_Data_T.S.58I03_1.xlsx')
def coef(data):
    matrix = np.zeros((data.shape[1], data.shape[1]))
    for i in range(data.shape[1]):
        for j in range(data.shape[1]):
            df01 = pd.DataFrame(zip(data.iloc[:,i], data.iloc[:,j]), columns=["x","y"])
            df01["yranks"] = df01["y"].rank()
            df01 = df01.sort_values("x")
            rank_series = df01["yranks"].reset_index(drop=True)
            #rank_series
            diff=[]
            for k in range(len(rank_series)-1):
                diff.append(abs(rank_series[k+1]-rank_series[k]))
            f=1-3*(sum(diff)/((df01.shape[0]**2)-1))
            matrix[i,j] = f
            
    return matrix
        
a = coef(df)
df02 = pd.DataFrame(a, columns=df.columns, index=df.columns).round(3)
df02


sns.clustermap(df02, method="complete", cmap='RdBu', annot=True, 
               annot_kws={"size": 9}, vmin=-1, vmax=1, figsize=(25,25));
plt.title('Chatterjee correlation Cofficent with Hierarchical cluster')
plt.savefig('CCCH.png', dpi=150, bbox_inches='tight')


plt.figure(figsize=(25,25))
correlations = df02

sns.heatmap(round(correlations,2), cmap='RdBu', annot=True, 
            annot_kws={"size": 9}, vmin=-1, vmax=1);
plt.title('Chatterjee correlation Cofficent')
plt.savefig('CCC.png', dpi=150, bbox_inches='tight')

# Pearsons correlation Cofficent

plt.figure(figsize=(25,25))
pcorrelations = df.corr()
sns.heatmap(round(pcorrelations,2), cmap='RdBu', annot=True, 
            annot_kws={"size": 9}, vmin=-1, vmax=1);
plt.title('Pearsons correlation Cofficent')
plt.savefig('PCC.png', dpi=150, bbox_inches='tight')


sns.clustermap(pcorrelations, method="complete", cmap='RdBu', annot=True, 
               annot_kws={"size": 9}, vmin=-1, vmax=1, figsize=(15,15));
plt.title('Pearsons correlation Cofficent with Hierarchical cluster')
plt.savefig('PCCH.png', dpi=150, bbox_inches='tight',transparent=True)

plt.show()


# In[ ]:





# In[ ]:




