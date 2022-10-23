#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[8]:


# Load the Excel data using pd.read_csv.
ott = pd.read_csv('ott_merge.csv')

# View the columns.
print(ott.columns)


# In[9]:


# Load the CSV data using pd.read_excel.
movies = pd.read_excel('movies_merge.xlsx')

print(movies.columns)


# In[5]:


# Data imported correctly?
print(movies.head())
print(movies.shape)
print(movies.dtypes)


# In[10]:


# Data imported correctly?
print(ott.head())
print(ott.dtypes)
print(ott.shape)


# In[11]:


# Merge the two DataFrames.
mov_ott = pd.merge(movies, ott, how='left', on = 'ID')

# View the DataFrame.
print(mov_ott.shape)
mov_ott.head()


# In[12]:


# Create a countplot based on number of movies streamed by Netflix per age group.
sns.countplot(x='Age',
              hue='Netflix',
              data=mov_ott)


# In[13]:


# Create a histogram based IMDb. 
sns.histplot(data=mov_ott,
             x='IMDb',
             binwidth=1)


# In[14]:


# Create scatterplot with two variables (IMDb and Rotten Tomatoes).
sns.scatterplot(x='IMDb',
                y='Rotten Tomatoes',
                data=mov_ott)


# In[15]:


# Create a simple lineplot.
sns.lineplot(x='Year',
             y='IMDb',
             data=mov_ott)


# In[16]:


# Create a simple lineplot.
sns.lineplot(x='Year',
             y='IMDb',
             data=mov_ott,
             ci=None)


# In[17]:


# Create lineplots with specification.
sns.lineplot(x = 'Year',
             y = 'IMDb',
             data=mov_ott[mov_ott['Age'].isin(['16+', '18+'])],
             hue ='Age')


# In[18]:


# Create lineplots with specification.
sns.lineplot(x = 'Year',
             y = 'IMDb',
             data=mov_ott[mov_ott['Age'].isin(['16+', '18+'])],
             hue ='Age',
             ci=None)


# In[19]:


mov_ott_2010 = mov_ott[mov_ott['Year'] >= 2010]

ax = sns.countplot(x='Year',
                   data=mov_ott_2010)

ax.set(ylabel='Percent')

total = len(mov_ott_2010['Year'])

for p in ax.patches:
    percentage = '{:.1f}%'.format(100 * p.get_height()/total)
    x = p.get_x()
    y = p.get_y() + p.get_height()
    ax.annotate(percentage, (x, y))

plt.xticks(rotation=90)
plt.show()


# In[20]:


ax = sns.displot(data=mov_ott,
                 x='IMDb',
                 bins=10,
                 kind='hist', 
                 palette='GnBu',
                 aspect=1.4,
                 kde=True)

plt.show()


# In[ ]:




