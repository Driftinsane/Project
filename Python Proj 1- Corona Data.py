#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[33]:


corona=pd.read_csv('D:/Python Projects/Python Proj 1/Corona_virus_analyst_project/covid_19_data.csv')


# In[34]:


corona


# In[36]:


#1.What is the total number of confirmed cases worldwide?
corona['Confirmed'].sum()


# In[37]:


#2.How many deaths have been reported globally?
corona['Deaths'].sum()


# In[38]:


#3.What is the total number of recovered cases worldwide?
corona['Recovered'].sum()


# In[39]:


#4.How many countries/regions are represented in the dataset?
corona['Country/Region'].count()


# In[40]:


#5.What is the trend of confirmed cases over time globally?
sns.histplot(data=corona,x='Confirmed',kde=True)


# In[96]:


corona[['Province/State','Confirmed']]


# In[108]:


#6.Which province/state has reported the highest number of confirmed cases?
corona['C_ascend']=corona['Confirmed'].sort_values(ascending=True)
corona[['C_ascend','Province/State']].tail().max()


# In[29]:


#7.Which country/region has the highest number of deaths?
corona[['Country/Region','Deaths']].max()


# In[24]:


#8.How does the number of confirmed cases vary across different provinces/states?
sns.boxplot(data=corona,x='Confirmed',y='Province/State')


# In[25]:


#9.What is the trend of deaths over time globally?
sns.histplot(data=corona,x='Deaths',kde=True)


# In[28]:


#10.Which country/region has the highest number of recovered cases?
corona[['Country/Region','Recovered']].max()


# In[46]:


#11.How does the number of recovered cases vary across different countries/regions?
sns.boxplot(data=corona,x='Recovered',y='Country/Region')


# In[49]:


#12.What is the distribution of confirmed cases by country/region?
corona.groupby(by='Country/Region')['Confirmed'].max().plot(kind='bar')


# In[51]:


#13.Is there a correlation between the number of confirmed cases and deaths?
corona[['Confirmed','Deaths']].corr()['Confirmed']


# In[52]:


#14.Is there a correlation between the number of confirmed cases and recovered cases?
corona[['Confirmed','Recovered']].corr()['Confirmed']


# In[75]:


#15.How does the mortality rate vary across different countries/regions?
corona.groupby(by='Country/Region')['Fatality rate'].max().plot(kind='bar')


# In[74]:


#16.How does the recovery rate vary across different countries/regions?
corona.groupby(by='Country/Region')['Recovery rate'].max().plot(kind='bar')


# In[72]:


#17.What is the trend of new confirmed cases over time globally?
sns.boxplot(data=corona,x='Confirmed',y='Last Update')


# In[71]:


#18.How does the fatality rate vary across different provinces/states?
corona['Fatality rate']=corona['Deaths']/corona['Confirmed']
corona.groupby(by='Province/State')['Fatality rate'].max().plot(kind='bar')


# In[73]:


#19.How does the recovery rate vary across different provinces/states?
corona['Recovery rate']=corona['Recovered']/corona['Confirmed']
corona.groupby(by='Province/State')['Recovery rate'].max().plot(kind='bar')


# In[69]:


#20.What is the trend of active cases over time globally?
corona['Active']=corona['Confirmed']-corona['Deaths']-corona['Recovered']
sns.histplot(data=corona,x='Active',kde=True)


# In[ ]:





# In[ ]:




