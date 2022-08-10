#!/usr/bin/env python
# coding: utf-8

# # Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You
# have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10
# jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.naukri.com/
# 2. Enter “Data Analyst” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the
# location” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.

# In[1]:


get_ipython().system('pip install selenium')


# In[1]:


import selenium
import pandas as pd
from selenium import webdriver


# In[3]:


driver = webdriver.Chrome(r"C:\Users\Win7\Desktop\Datascience\chromedriver_win32\chromedriver.exe")


# In[ ]:


url = "https://www.naukri.com"
driver.get(url)


# In[3]:


search_job = driver.find_element_by_xpath("//input[@class='sugInp']")
search_job


# In[ ]:


search_job.send_keys('Data Analyst')


# In[ ]:


search_loc=driver.find_element_by_id('qsb-location-sugg')
search_loc.send_keys("Bangalore")


# In[5]:


search_btn= driver .find_element_by_xpath("//button[@class='btn']")
search_btn


# In[ ]:


search_btn=driver.find_element_by_xpath("//button[@class='btn']")
search_btn.click()


# In[6]:


search_btn=driver.find_element_by_xpath("//button[@class='btn']")
search_btn.click()


# In[7]:


title_tags=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
title_tags


# In[ ]:


job_titles=[]
for i in title_tags:
    if i.text is None:
        job_titles.append('Not')
    else:
        job_titles.append(i.text)
job_titles[:10]        


# In[4]:


company_tags=driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
company_tags


# In[ ]:


companies_names=[]

for i in company_tags:
    companies_names.append(i.text)
companies_names[:10]    


# In[5]:


experience_tags=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience'] //span")
experience_tags


# In[ ]:


experience_list=[]
for i in experience_tags:
    experience_list.append(i.text)
experience_list[:10]   


# In[6]:


locations_tags=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span")
locations_tags


# In[ ]:


locations_list=[]
for i in locations_tags:
    locations_list.append(i.text)
locations_list[:10]   


# In[7]:


print(len(job_titles[:10])),print(len(companies_names[:10])),print(len(experience_list[:10])),print(len(locations_list[:10]))


# In[ ]:


jobs=pd.DataFrame({})
jobs['title']=job_titles[:10]
jobs['company']=companies_names[:10]
jobs['experience_required']=experience_list[:10]
jobs['location']=locations_list[:10]


# In[8]:


jobs


# In[ ]:


driver.close()


# In[ ]:


from selenium.common.exceptions import NoSuchElementException


# In[ ]:





# # Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You
# have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.naukri.com/
# 2. Enter “Data Scientist” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the
# location” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.

# In[9]:


driver = webdriver.Chrome(r"C:\Users\Win7\Desktop\Datascience\chromedriver_win32\chromedriver.exe")


# In[ ]:


url = "https://www.naukri.com"
driver.get(url)


# In[ ]:


search_job = driver.find_element_by_xpath("//input[@class='sugInp']")
search_job


# In[ ]:


search_job.send_keys('Data Scientist')


# In[ ]:


search_loc=driver.find_element_by_id('qsb-location-sugg')
search_loc.send_keys("Bangalore")


# In[ ]:


search_btn= driver .find_element_by_xpath("//button[@class='btn']")
search_btn


# In[ ]:


search_btn=driver.find_element_by_class_name('btn')
search_btn.click()


# In[ ]:


title_tag=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
title_tag


# In[ ]:


job1_titles=[]
for i in title_tag:
    if i.text is None:
        job1_titles.append('Not')
    else:
        job1_titles.append(i.text)
job1_titles[:10] 


# In[ ]:


company_tag=driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
company_tag


# In[ ]:


companies1_names=[]

for i in company_tag:
    companies1_names.append(i.text)
companies1_names[:10]   


# In[ ]:


locations_tag=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span")
locations_tag


# In[ ]:


locations1_list=[]
for i in locations_tag:
    locations1_list.append(i.text)
locations1_list[:10]    


# In[ ]:


print(len(job1_titles[:10])),print(len(companies1_names[:10])),print(len(locations1_list[:10]))


# In[ ]:


driver=webdriver.Chrome(r"C:\Users\Neha\Downloads\chromedriver_win32\chromedriver.exe")
driver.get('https://www.naukri.com/data-scientist-jobs-in-banglore-bagaluru')


# In[ ]:


urls=[]


# In[ ]:


job_description=[]


# In[ ]:


for i in driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']"):
    urls.append(i.get_attribute("href"))
        


# In[ ]:


for url in urls[:10]:
    
    
    try:
        driver.get(url)
        description=driver.find_element_by_xpath("//section[@class='job-desc']").text
        job_description.append(description)
        
    except NoSuchElementException:
        job_description.append("Not Available")


# In[ ]:


job_description


# In[ ]:


print(len(job_description))


# In[ ]:


job1=pd.DataFrame({})
job1['title']=job1_titles[:10]
job1['company_name']=companies1_names[:10]
job1['location']=locations1_list[:10]
job1['job_desc']=job_description


# In[ ]:


job1


# In[ ]:


driver.close()


# In[ ]:





# # In this question you have to scrape data using the filters available on the webpage as shown below:
# You have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results.
# You have to scrape the job-title, job-location, company name, experience required.
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
# The task will be done as shown in the below steps:
# 1. first get the webpage https://www.naukri.com/
# 2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
# 3. Then click the search button.
# 4. Then apply the location filter and salary filter by checking the respective boxes
# 5. Then scrape the data for the first 10 jobs results you get.
# 6. Finally create a dataframe of the scraped data.

# In[ ]:


driver = webdriver.Chrome(r"C:\Users\Neha\Downloads\chromedriver_win32\chromedriver.exe")


# In[ ]:


url = "https://www.naukri.com"
driver.get(url)


# In[ ]:


search_job = driver.find_element_by_xpath("//input[@class='sugInp']")
search_job


# In[ ]:


search_job.send_keys('Data Scientist')


# In[ ]:


search_btn= driver .find_element_by_xpath("//button[@class='btn']")
search_btn


# In[ ]:


search_btn=driver.find_element_by_class_name('btn')
search_btn.click()


# In[ ]:


title_t1=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
title_t1


# In[ ]:


job_titles=[]
for i in title_t1:
    if i.text is None:
        job_titles.append('Not')
    else:
        job_titles.append(i.text)
job_titles[:10]        


# In[ ]:


company_t1=driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
company_t1


# In[ ]:


companies_names=[]

for i in company_t1:
    companies_names.append(i.text)
companies_names[:10]    


# In[ ]:


experience_t1=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience'] //span")
experience_t1


# In[ ]:


experience_list=[]
for i in experience_t1:
    experience_list.append(i.text)
experience_list[:10]   


# In[ ]:


locations_t1=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span")
locations_t1


# In[ ]:


locations_list=[]
for i in locations_t1:
    locations_list.append(i.text)
locations_list[:10]    


# In[ ]:


print(len(job_titles[:10])),print(len(companies_names[:10])),print(len(experience_list[:10])),print(len(locations_list[:10]))


# In[ ]:


jobs2=pd.DataFrame({})
jobs2['title']=job_titles[:10]
jobs2['company']=companies_names[:10]
jobs2['experience_required']=experience_list[:10]
jobs2['location']=locations_list[:10]


# In[ ]:


jobs2


# In[ ]:


driver.close()


# In[ ]:





# # Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 1. Brand
# 2. Product Description
# 3. Price
# The attributes which you have to scrape is ticked marked in the below image.

# In[ ]:


driver = webdriver.Chrome(r"C:\Users\Neha\Downloads\chromedriver_win32\chromedriver.exe")


# In[ ]:


url="https://www.flipkart.com/"
driver.get(url)


# In[ ]:


search_g= driver.find_element_by_xpath("//input[@type='text']")
search_g


# In[ ]:


search_g.send_keys('sunglasses')


# In[ ]:


search_btn=driver.find_element_by_xpath("//button[@class='L0Z3Pu']")
search_btn


# In[ ]:


search_btn=driver.find_element_by_class_name('L0Z3Pu')
search_btn.click()


# In[ ]:


B_name=[]
Price=[]
P_desc=[]
Discount=[]


# In[ ]:


for i in range(3):
    b_name=driver.find_elements_by_xpath("//div[@class='_2WkVRV']")
    p_desc=driver.find_elements_by_xpath("//a[@class='IRpwTa']")
    price =driver.find_elements_by_xpath("//div[@class='_25b18c']")
    discount=driver.find_elements_by_xpath("//div[@class='_3Ay6Sb']")
    
    for j  in b_name:
        B_name.append(j.text)
    B_name[:100]    
    
    
    
    for k in p_desc:
        P_desc.append(k.text)
    P_desc[:100] 
    
    
    for l in price:
        Price.append(l.text)
    Price[:100] 
    
    
    for t in discount:
        Discount.append(t.text)
    Discount[:100]


# In[ ]:


B_name[:100]
    


# In[ ]:


print(len(B_name[:100])),print(len(Price[:100])),print(len(P_desc[:100])),print(len(Discount[:100]))


# In[ ]:


sun_gl=pd.DataFrame({})
sun_gl['Brand_name']=B_name[:100]
sun_gl['P_price']=Price[:100]
sun_gl['Pr_desc']=P_desc[:100]
sun_gl['P_discount']=Discount[:100]


# In[ ]:


sun_gl


# In[ ]:


driver.close()


# In[ ]:





# # Scrape data for first 100 sneakers you find when you visit flipkart.com and
# search for “sneakers” in the search field.
# 
# You have to scrape 4 attributes of each sneaker :
# 
# Brand
# 
# Product Description
# 
# Price
# 
# discount %

# In[ ]:


driver = webdriver.Chrome(r"C:\Users\Neha\Downloads\chromedriver_win32\chromedriver.exe")


# In[ ]:


url="https://www.flipkart.com/"
driver.get(url)


# In[ ]:


search_g= driver.find_element_by_xpath("//input[@type='text']")
search_g


# In[ ]:


search_g.send_keys('sneakers')


# In[ ]:


search_btn=driver.find_element_by_xpath("//button[@class='L0Z3Pu']")
search_btn


# In[ ]:


search_btn=driver.find_element_by_class_name('L0Z3Pu')
search_btn.click()


# In[ ]:


B_name=[]
Price=[]
P_desc=[]
Discount=[]


# In[ ]:


for i in range(3):
    b_name=driver.find_elements_by_xpath("//div[@class='_2WkVRV']")
    p_desc=driver.find_elements_by_xpath("//a[@class='IRpwTa']")
    price =driver.find_elements_by_xpath("//div[@class='_25b18c']")
    discount=driver.find_elements_by_xpath("//div[@class='_3Ay6Sb']")
    
    for j  in b_name:
        B_name.append(j.text)
    B_name[:100]    
    
    
    
    for k in p_desc:
        P_desc.append(k.text)
    P_desc[:100] 
    
    
    for l in price:
        Price.append(l.text)
    Price[:100] 
    
    
    for t in discount:
        Discount.append(t.text)
    Discount[:100]


# In[ ]:


print(len(B_name[:100])),print(len(Price[:100])),print(len(P_desc[:100])),print(len(Discount[:100]))


# In[ ]:


sun_gl=pd.DataFrame({})
sun_gl['Brand_name']=B_name[:100]
sun_gl['P_price']=Price[:100]
sun_gl['Pr_desc']=P_desc[:100]
sun_gl['P_discount']=Discount[:100]


# In[ ]:


sun_gl


# In[ ]:


driver.close()


# In[ ]:





# # Go to the link - https://www.myntra.com/shoes
# Set second Price filter and Color filter to “Black”, as shown in the below image.
# And then scrape First 100 shoes data you get. The data should include “Brand” of the shoes , Short Shoe
# description, price of the shoe as shown in the below image.

# In[ ]:


driver = webdriver.Chrome(r"C:\Users\Neha\Downloads\chromedriver_win32\chromedriver.exe")


# In[ ]:


url="https://www.myntra.com/shoes"
driver.get(url)


# In[ ]:


filter_button=driver.find_elements_by_xpath("//label[@class='common-customerCheckbox vertical-filters-label']")
for i in filter_button:
    if i.text=="Rs. 6649 to Rs. 13099":
        i.click()
        break


# In[ ]:


filter_button=driver.find_elements_by_xpath("//li[@class='colour-listItem']")
for i in filter_button:
    if i.text=="Black":
        i.click()
        break


# In[ ]:


B_name=[]
Price=[]
P_desc=[]


# # for i in range(2):
#     b_name=driver.find_elements_by_xpath("//h1[@class='pdp-title']")
#     p_desc=driver.find_elements_by_xpath("//h1[@class='name']")
#     price =driver.find_elements_by_xpath("//div[@class='product-price']")
#  
#     for j  in b_name:
#         B_name.append(j.text)
#     B_name[:100]    
#     
#     
#     
#     for k in p_desc:
#         P_desc.append(k.text)
#     P_desc[:100] 
#     
#     
#     for l in price:
#         Price.append(l.text)
#     Price[:100] 
#     

# In[ ]:


print(len(B_name[:100])),print(len(Price[:100])),print(len(P_desc[:100]))


# In[ ]:


driver.close()


# In[ ]:





# # Go to webpage https://www.amazon.in/
# Enter “Laptop” in the search field and then click the search icon.
# Then set CPU Type filter to “Intel Core i7” as shown in the below image:
# After setting the filters scrape first 10 laptops data. You have to scrape 3 attributesfor each laptop:
# 1. Title
# 2. Ratings
# 3. Price

# In[ ]:


driver = webdriver.Chrome(r"C:\Users\Neha\Downloads\chromedriver_win32\chromedriver.exe")


# In[ ]:


url=" https://www.amazon.in "
driver.get(url)


# In[ ]:


search_g= driver.find_element_by_xpath("//input[@type='text']")
search_g


# In[ ]:


search_g.send_keys('Laptop')


# In[ ]:


search_btn=driver.find_element_by_xpath("//input[@id='nav-search-submit-button']")
search_btn


# In[ ]:


search_btn=driver.find_element_by_xpath("//input[@id='nav-search-submit-button']")
search_btn.click()


# In[ ]:


Title=[]
Price=[]
Rating=[]


# In[ ]:


for i in range(3):
    b_name=driver.find_elements_by_xpath("//div[@class='_2WkVRV']")
    p_desc=driver.find_elements_by_xpath("//a[@class='IRpwTa']")
    price =driver.find_elements_by_xpath("//div[@class='_25b18c']")
    
    
    for j  in b_name:
        Title.append(j.text)
    Title[:100]    
    
    
    
    for k in p_desc:
        P_desc.append(k.text)
    P_desc[:100] 
    
    
    for l in price:
        Price.append(l.text)
    Price[:100] 


# In[ ]:


print(len(B_name[:100])),print(len(Price[:100])),print(len(P_desc[:100]))


# In[ ]:


driver.close()


# In[ ]:





# # Scrape 100 reviews data from flipkart.com for iphone11 phone.
# This task will be done in following steps:
# 1. First get the webpage https://www.flipkart.com/
# 2. Enter “iphone 11” in “Search” field .
# 3. Then click the search button.

# In[ ]:





# In[ ]:





# # Write a python program to scrape the salary data for Data Scientist designation.
# You have to scrape Company name, Number of salaries, Average salary, Minsalary, Max Salary.
# The above task will be, done as shown in the below steps:
# 1. First get the webpage https://www.ambitionbox.com/
# 2. Click on the salaries option as shown in the image.
# After reaching to the following webpage, In place of “Search Job Profile” enters “Data Scientist” and
# then click on “Data Scientist”.You have to scrape the data ticked in the above image.
# 4. Scrape the data for the first 10 companies. Scrape the company name, total salary record, average
# salary, minimum salary, maximum salary, experience required.
# 5. Store the data in a dataframe.

# In[ ]:





# # Write a python program to scrape data for first 10 job results for Data Scientist Designation in Noida
# location. You have to scrape company name, No. of days ago when job was posted, Rating of the company.
# This task will be done in following steps:
# 1. First get the webpage https://www.ambitionbox.com/
# 2. Click on the Job option as shown in the image
# 3. After reaching to the next webpage, In place of “Search by Designations, Companies, Skills” enter
# “Data Scientist” and click on search button.
# 4. You will reach to the following web page click on location and in place of “Search location” enter
# “Noida” and select location “Noida”.
# 5. Then scrape the data for the first 10 jobs results you get on the above shown page.
# 6. Finally create a dataframe of the scraped data.

# In[ ]:





# In[ ]:




