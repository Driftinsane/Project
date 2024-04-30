#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


Loan_data=pd.read_csv('D:/Python Projects/Python Proj 2/Loan_data_analysis_project/Loan_dataset.csv')


# In[3]:


Loan_data


# In[10]:


#1.What is the average current loan amount from each loan status?
Loan_data.groupby(by='Loan Status')['Current Loan Amount'].mean()


# In[15]:


#2.How does the credit score vary with the annual income?
sns.scatterplot(data=Loan_data,x='Credit Score',y='Annual Income',hue='Credit Score')


# In[16]:


#3.Is there a correlation between the number of open accounts and the current credit balance?
Loan_data[['Number of Open Accounts','Current Credit Balance']].corr()['Number of Open Accounts']


# In[19]:


#4.What is the distribution of credit scores across different home ownership types?
Loan_data.groupby(by='Home Ownership')['Credit Score'].max().plot(kind='bar')


# In[20]:


#5.How does the annual income differ for different purposes of loans?
Loan_data.groupby('Purpose')['Annual Income'].max().plot(kind='bar')


# In[21]:


#6.What is the average monthly debt for each term (short-term vs. long-term)?
Loan_data.groupby(by='Term')['Monthly Debt'].mean()


# In[22]:


#7.Is there a correlation between years of credit history and the current credit balance?
Loan_data[['Years of Credit History','Current Credit Balance']].corr()['Years of Credit History']


# In[25]:


#8.How does the credit score vary with the years in the current job?
sns.scatterplot(data=Loan_data,y='Years in current job',x='Credit Score',hue='Credit Score')


# In[29]:


#9.What is the relationship between the number of credit problems and the number of open accounts?
sns.scatterplot(data=Loan_data,x='Number of Credit Problems',y='Number of Open Accounts',hue='Number of Open Accounts')


# In[30]:


#10.What is the distribution of annual income across different loan statuses?
Loan_data.groupby(by='Loan Status')['Annual Income'].max()


# In[32]:


#11.Is there a correlation between the current loan amount and the number of open accounts?
Loan_data[['Current Loan Amount','Number of Open Accounts']].corr()['Number of Open Accounts']


# In[35]:


#12.How does the monthly debt vary with the years of credit history?
sns.scatterplot(data=Loan_data,x='Monthly Debt',y='Years of Credit History',hue='Years of Credit History')


# In[38]:


#13.What is the average annual income for each purpose of loan?
Loan_data.groupby(by='Purpose')['Annual Income'].mean().plot(kind='bar')


# In[40]:


#14.How does the credit score vary with the number of credit problems?
sns.scatterplot(data=Loan_data,y='Credit Score',x='Number of Credit Problems')


# In[41]:


#15.Is there a correlation between the number of credit problems and the current credit balance?
Loan_data[['Number of Credit Problems','Current Credit Balance']].corr()['Number of Credit Problems']


# In[44]:


#16.What is the distribution of current loan amounts across different home ownership types?
Loan_data.groupby(by='Home Ownership')['Current Loan Amount'].max()


# In[45]:


#17.How does the annual income vary with the years in the current job?
sns.scatterplot(data=Loan_data,x='Annual Income',y='Years in current job')


# In[46]:


#18.Is there a correlation between the current loan amount and the monthly debt?
Loan_data[['Current Loan Amount','Monthly Debt']].corr()['Current Loan Amount']


# In[47]:


#19.What is the average monthly debt for each home ownership type?
Loan_data.groupby(by='Home Ownership')['Monthly Debt'].mean()


# In[48]:


#20.How does the credit score vary with the number of open accounts?
sns.scatterplot(data=Loan_data,x='Credit Score',y='Number of Open Accounts')


# In[50]:


#21.What is the distribution of credit scores across different loan statuses?
Loan_data.groupby(by='Loan Status')['Credit Score'].max().plot(kind='bar')


# In[51]:


#22.Is there a correlation between the current loan amount and the years of credit history?
Loan_data[['Current Loan Amount','Years of Credit History']].corr()['Current Loan Amount']


# In[52]:


#23.How does the monthly debt vary with the number of credit problems?
sns.scatterplot(data=Loan_data,x='Monthly Debt',y='Number of Credit Problems')


# In[54]:


#24.What is the average current loan amount for each purpose of loan?
Loan_data.groupby(by='Purpose')['Current Loan Amount'].mean().plot(kind='bar')


# In[55]:


#25.How does the credit score vary with the current credit balance?
sns.scatterplot(data=Loan_data,x='Credit Score',y='Current Credit Balance')


# In[57]:


#26.Is there a correlation between the annual income and the current credit balance?
Loan_data[['Annual Income','Current Credit Balance']].corr()['Annual Income']


# In[58]:


#27.What is the distribution of annual income across different terms (short-term vs. long-term)?
Loan_data.groupby(by='Term')['Annual Income'].max().plot(kind='bar')


# In[59]:


#28.How does the credit score vary with the number of credit problems?
sns.scatterplot(data=Loan_data,x='Credit Score',y='Number of Credit Problems')


# In[60]:


#29.Is there a correlation between the current loan amount and the number of credit problems?
Loan_data[['Current Loan Amount','Number of Credit Problems']].corr()['Current Loan Amount']


# In[61]:


#30.What is the relationship between the number of open accounts and the years of credit history?
sns.scatterplot(data=Loan_data,x='Number of Open Accounts',y='Years of Credit History')


# In[7]:


Loan_data.columns


# In[ ]:




