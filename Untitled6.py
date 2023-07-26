#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# SELENIUM ASSIGNMENT


get_ipython().system('pip install selenium')

# Let's import all required libraries

import selenium                                  #library that is used to work with selenium

from selenium import webdriver                   #importing webdriver module from selenium to open automated chrome window

import pandas as pd                              #to create DataFrame

from selenium.webdriver.common.by import By      #importing inbuilt class By 

import warnings                                  #to ignore any sort of warning

warnings.filterwarnings("ignore")

import time                                      #use to stop search engine for few seconds


# In[ ]:


#Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data.


# In[25]:


driver = webdriver.Chrome()


# In[26]:


driver.get("https://www.naukri.com/")


# In[30]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Analyst')


# In[31]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Banglore')


# In[32]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[33]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[34]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
    
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    experience=i.text
    experience_required.append(experience)


# In[35]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[36]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company_name':company_name,'Experience':experience_required})
df


# In[ ]:





# In[ ]:


#Q2:Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.


# In[14]:


driver = webdriver.Chrome()


# In[38]:


driver.get("https://www.naukri.com/")


# In[39]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Scientist')


# In[40]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Banglore')


# In[41]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[42]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[43]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
    
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    


# In[48]:


print(len(job_title),len(job_location),len(company_name))


# In[57]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company_name':company_name})
df


# In[ ]:





# In[ ]:





# In[ ]:


#Q3: In this question you have to scrape data using the filters available on the webpage as shown below:
#You have to use the location and salary filter.
#You have to scrape data for “Data Scientist” designation for first 10 job results.
#You have to scrape the job-title, job-location, company name, experience required. 
#The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs


# In[59]:


driver = webdriver.Chrome()


# In[60]:


driver.get("https://www.naukri.com/")


# In[61]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Scientist')


# In[62]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[64]:


location_checkbox = driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[5]/div[2]/div[2]/label/p/span[1]")
location_checkbox.click()


# In[65]:


salary_checkbox = driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[6]/div[2]/div[2]/label/p/span[1]")
salary_checkbox.click()


# In[67]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[68]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
    
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    experience=i.text
    experience_required.append(experience)


# In[69]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[70]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company_name':company_name,'experience':experience_required})
df


# In[ ]:





# #Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 1. Brand
# 2. ProductDescription
# 3. Price

# In[51]:


driver = webdriver.Chrome()


# In[52]:


driver.get("https://www.flipkart.com/")


# In[58]:


PRODUCT = driver.find_element(By.CLASS_NAME,"_3704LK")
PRODUCT.send_keys("Sunglasses")


# In[ ]:


search=driver.find_element(By.CLASS_NAME,'L0Z3Pu')
search.click()


# In[24]:


brand_tags=[]
product_description=[]
price=[]


# In[25]:


start=0
end=3
for page in range(start,end):
    brand=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand:
        brand_tags.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)
                               


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link: 
#https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART


# In[120]:


driver=webdriver.Chrome()


# In[121]:


driver.get('https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART')


# In[97]:


rating=[]
review_summary=[]
full_review=[]


# In[98]:


start = 0
end = 10
for page in range(start, end):
    # Find rating elements using the given XPath
    rating_tags = driver.find_elements(By.XPATH, '//div[@class="_3LWZlK _1BLPMq"]')
    for i in rating_tags[0:10]:
        rating = i.text
        ratings.append(rating)

    # Click the next button
    next_button = driver.find_element(By.XPATH, '//a[@class="_1LKTO3"]')
    next_button.click()

    # Add a time delay to let the page load before proceeding to the next iteration
    time.sleep(4)

# After the loop, close the driver
driver.quit()

# Print the collected ratings
print(ratings)


# In[111]:


start=0
end=10
for page in range(start,end):
    review_summary_tags=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
    for i in review_summary_tags:
        review_summary.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(5)


# In[122]:


start=0
end=10
for page in range(start,end):
    full_review_tags=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
    for i in full_review_tags:
        full_review.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(5)
    


# In[127]:


print(len(ratings[0:100]),len(review_summary),len(full_review))


# In[125]:


import pandas as pd
df=pd.DataFrame({"Rating":ratings[0:100],'Review_Summary':review_summary,'Full_Review':full_review[0:100]})
df


# In[ ]:





# In[ ]:





# #Q6: Scrape data forfirst 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the search field.
# You have to scrape 3 attributes of each sneaker:
# 1. Brand
# 2. ProductDescription
# 3. Price
# As shown in the below image, you have to scrape the above attributes

# In[15]:


driver=webdriver.Chrome()


# In[16]:


driver.get("https://www.flipkart.com/")


# In[19]:


product=driver.find_element(By.CLASS_NAME,'Pke_EE')
product.send_keys('sneakers')


# In[23]:


search=driver.find_element(By.CLASS_NAME,'_2iLD__')
search.click()


# In[50]:


brand=[]
product_description=[]
price=[]


# In[57]:


start=0
end=3
for page in range(start,end):
    brands=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brands:
        brand.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(5)
print(brand)


# In[58]:


len(brand)


# In[67]:


start=0
end=3
for page in range( start,end):
    product_description_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in product_description_tags:
        product_description.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(5)


# In[68]:


len(product_description)


# In[59]:


start=0
end=3
for page in range(start,end):
    price_list=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in price_list:
        price.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(5)


# In[61]:


len(price)


# In[69]:


print(len(brand),len(product_description),len(price))


# In[70]:


import pandas as pd 
df=pd.DataFrame({'Brand':brand[0:100],'Product_Description':product_description[0:100],'Price':price[0:100]})
df


# In[ ]:





# In[ ]:


#Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then set CPU Type filter to “Intel Core i7” as shown in the below image:


# In[46]:


driver=webdriver.Chrome()


# In[47]:


driver.get('https://www.amazon.in/')


# In[49]:


laptops=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]')
laptops.send_keys('Laptops')


# In[ ]:





# In[ ]:


#Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.


# In[74]:


driver=webdriver.Chrome()


# In[75]:


driver.get("http://www.azquotes.com/")


# In[76]:


top=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a')
top.click()


# In[77]:


quote=[]


# In[79]:


start=0
end=10
for page in range(start,end):
    quotes=driver.find_elements(By.XPATH,'//a[@class="title"]')
    for i in quotes:
        quote.append(i.text)
    next_button=driver.find_element(By.XPATH,'//li[@class="next"]')
    next_button.click()
    time.sleep(10)
    


# In[ ]:





# In[ ]:





# In[ ]:


#Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e. car name and Price) from https://www.motor1.com/


# In[41]:


driver=webdriver.Chrome()


# In[42]:


driver.get('https://www.motor1.com/')


# In[43]:


car=driver.find_element(By.CLASS_NAME,'search-bar__submit')
car.send_keys('50 most expensive cars')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




