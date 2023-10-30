#!/usr/bin/env python
# coding: utf-8

# # Predicting House Prices
# 
# You are working for a real estate company, and your goal is to build a predictive model to estimate house prices based on various features. You have a dataset containing information about houses, such as square footage, number of bedrooms, number of bathrooms, and other relevant attributes. You are tasked with the following:
# 
# Dataset: You can choose / download the dataset from Kaggle/ UCI Repository or any other medium.
# 
# 1. Data Preparation:
# 
# a. Load the dataset using pandas. 
# 
# b. Explore and clean the data. Handle missing values and outliers.
# 
# c. Split the dataset into training and testing sets.
# 
# 2. Implement Simple Linear Regression:
# 
# a. Choose a feature (e.g., square footage) as the independent variable (X) and house prices as the dependent variable (y).
# 
# b. Implement a simple linear regression model using sklearn to predict house prices based on the selected feature.
# 
# c. Visualize the data and the regression line.
# 
# 3. Evaluate the Simple Linear Regression Model:
#     
# a. Use scikit-learn to calculate the R-squared value to assess the goodness of fit.
# 
# b. Interpret the R-squared value and discuss the model's performance.
# 
# 4. Implement Multiple Linear Regression:
# 
# a. Select multiple features (e.g., square footage, number of bedrooms, number of bathrooms) as independent variables (X) and house prices as the dependent variable (y).
# 
# b. Implement a multiple linear regression model using scikit-learn to predict house prices based on the selected features.
# 
# 5. Evaluate the Multiple Linear Regression Model:
# 
# a. Calculate the Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE) to assess the model's accuracy.
# 
# b. Discuss the advantages of using multiple features in regression analysis.
# 
# 6. Model Comparison:
# 
# a. Compare the results of the simple linear regression and multiple linear regression models.
# 
# b. Discuss the advantages and limitations of each model.
# 
# 7. Model Improvement:
# 
# a. Explore potential model improvements, such as feature selection, feature engineering, or hyperparameter tuning, and describe how they could enhance the model's performance.
# 
# 8. Conclusion:
# 
# a. Summarize the findings and provide insights into how this predictive model can be used to assist the real estate company in estimating house prices.
# 
# 9. Presentation:
# 
# a. Prepare a presentation or report summarizing your analysis, results, and recommendations.
# 
# In this case study, you are required to demonstrate your ability to preprocess data, implement both simple and multiple linear regression models, evaluate their performance, and make recommendations for improving the models. This case study should assess your knowledge of using Python libraries like NumPy, pandas, and scikit-learn for linear regression tasks and your understanding of model evaluation techniques.

# In[7]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


#Load the dataset
data=pd.read_csv("Housing.csv")
data


# In[23]:


data.hist()


# In[24]:


#b. Explore and clean the data. Handle missing values and outliers.
data.isna().sum()


# In[25]:


data.head(1)


# In[26]:


x=data.iloc[:,1:2]
x
#x.head(2)


# In[29]:


y=data.iloc[:,:1]
#y.head(2)
y


# In[30]:


type(x)


# In[31]:


type(y)


# In[32]:


#c. Split the dataset into training and testing sets.
import sklearn
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=2)


# In[46]:


data.shape


# In[48]:


#a. Choose a feature (e.g., square footage) as the independent variable (X) and house prices as the dependent variable (y).
#b. Implement a simple linear regression model using sklearn to predict house prices based on the selected feature.
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
#train the data
print('Training Started.......\n')
print()
lin_reg.fit(xtrain, ytrain)
print()
print('Training Completed.....')
print()
#test the data

print('Testing invoked......\n')
ypred=lin_reg.predict(xtest)

print('Predicted Total Price \n',ypred)

print('\n Testing is also completed....\n')


# In[50]:


#c. Visualize the data and the regression line.
plt.scatter(xtrain,ytrain,color='yellow')
plt.plot(xtrain,lin_reg.predict(xtrain),color='blue')
plt.title("Housing Prices")
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()


# In[51]:


plt.scatter(xtest,ytest,color='yellow')
plt.plot(xtest,lin_reg.predict(xtest),color='blue')
plt.title("Housing Prices")
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()


# In[52]:


#a. Use scikit-learn to calculate the R-squared value to assess the goodness of fit.
#b. Interpret the R-squared value and discuss the model's performance.
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score
print("Mean Squared Error: \t",mean_squared_error(ytest,ypred))
print()
print("RMSE: \t",np.sqrt(mean_squared_error(ytest,ypred)))
print()
print("Variance Score: \t",explained_variance_score(ytest,ypred))
print()
print("R-Square: \t",r2_score(ytest,ypred))


# In[9]:


#Multiple Linear Regression 
#a. Select multiple features (e.g., square footage, number of bedrooms, number of bathrooms) as independent variables (X) and house prices as the dependent variable (y).

#b. Implement a multiple linear regression model using scikit-learn to predict house prices based on the selected features.
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:


data1=pd.read_csv("Housing.csv")
data1.head()


# In[11]:


data1.isna().sum()


# In[12]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data1["mainroad"]=le.fit_transform(data1["mainroad"])
data1["guestroom"]=le.fit_transform(data1["guestroom"])
data1["basement"]=le.fit_transform(data1["basement"])
data1["hotwaterheating"]=le.fit_transform(data1["hotwaterheating"])
data1["airconditioning"]=le.fit_transform(data1["airconditioning"])
data1["prefarea"]=le.fit_transform(data1["prefarea"])
data1["furnishingstatus"]=le.fit_transform(data1["furnishingstatus"])
data1.head()


# In[59]:


sns.pairplot(data1)


# In[63]:


sns.boxplot(x=data1["prefarea"],y=data1["area"])


# In[64]:


sns.barplot(x=data1["prefarea"],y=data1["area"])


# In[13]:


x=data1.iloc[:,1:]
x.head()


# In[73]:


y=data1.iloc[:,:1]
y.head()


# In[74]:


from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=1)


# In[75]:


from sklearn.linear_model import LinearRegression
mul_reg=LinearRegression()
#train the data
print('Training Started.......\n')
print()
mul_reg.fit(xtrain, ytrain)
print()
print('Training Completed.....')
print()
#test the data

print('Testing invoked......\n')
ypred=mul_reg.predict(xtest)

print('Predicted Total Price \n',ypred)

print('\n Testing is also completed....\n')


# In[77]:


from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_absolute_error
print("Mean Absolute Error: \t",mean_absolute_error(ytest,ypred))
print()
print("Mean Squared Error: \t",mean_squared_error(ytest,ypred))
print()
print("RMSE: \t",np.sqrt(mean_squared_error(ytest,ypred)))
print()
print("Variance Score: \t",explained_variance_score(ytest,ypred))
print()
print("R-Square: \t",r2_score(ytest,ypred))


# In[79]:


plt.figure(figsize=(10,6))
sns.heatmap(data1.corr(),annot=True,vmin=-1,vmax=1)


# In[ ]:




