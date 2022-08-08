#!/usr/bin/env python
# coding: utf-8

# # Write a python program to display all the header tags from wikipedia.org.

# In[1]:


get_ipython().system('pip install pywhatkit')


# In[3]:


import pywhatkit as pwt
pwt.info("python programimg")


# In[6]:


import pywhatkit as pwt
pwt.info("python programimg",100)


# # Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
# and make data frame.

# In[5]:


pip install beautifulsoup4


# In[9]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
 
 
# Downloading imdb top 250 movie's data
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value')
        for b in soup.select('td.posterColumn span[name=ir]')]
 
 
 
 
# create a empty list for storing
# movie information
list = []
 
# Iterating over movies to extract
# each movie's details
for index in range(0, len(movies)):
     
    # Separating movie into: 'place',
    # 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"place": place,
            "movie_title": movie_title,
            "rating": ratings[index],
            "year": year,
            "star_cast": crew[index],
            }
    list.append(data)
 
# printing movie details with its rating.
for movie in list:
    print(movie['place'], '-', movie['movie_title'], '('+movie['year'] +
        ') -', 'Starring:', movie['star_cast'], movie['rating'])
 
 
##.......##
df = pd.DataFrame(list)
df.to_csv('imdb_top_250_movies.csv',index=False)


# In[ ]:





# # Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of
# release) and make data frame.

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[7]:


url ="https://www.imdb.com/india/top-rated-indian-movies/"
response=requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup)

movies_data = soup.findAll('div',attrs= {'class': 'lister-item mode-advanced'})
# In[8]:


movies_data=soup.findAll('div',attrs={'class':'lister-list'})


# In[11]:


movies_data


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Write s python program to display list of respected former presidents of India(i.e. Name , Term of office)
# from https://presidentofindia.nic.in/former-presidents.htm

# In[ ]:





# In[ ]:





# In[9]:


from bs4 import BeautifulSoup
import requests
import re

# Download IMDB's Top 100 Indian movies data
url = 'https://www.imdb.com/india/top-rated-indian-movies/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

imdb = []

# Store each item into dictionary (data), then put those into a list (imdb)
for index in range(0, len(movies)):
    # Seperate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"movie_title": movie_title,
            "year": year,
            "place": place,
            "star_cast": crew[index],
            "rating": ratings[index],
            "vote": votes[index],
            "link": links[index]}


# In[ ]:





# In[ ]:





# In[1]:


get_ipython().system('pip install requests --upgrade')


# In[2]:


import requests


# In[3]:


headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}


# In[6]:


url ='https://scholar.google.com/citations?view_op=top_venues&hl=en'


# In[4]:


response=requests.get(url,headers=headers)


# In[7]:


response.status_code


# In[ ]:





# In[ ]:





# # Write s python program to display list of respected former presidents of India(i.e. Name , Term of office)
# from https://presidentofindia.nic.in/former-presidents.htm

# # from bs4 import BeautifulSoup
# import requests
# import re
# 
# url = 'https://presidentofindia.nic.in/former-presidents.htm'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
# 
# name = soup.select('contentPlaceHolder1_mainbody')
# print(name)
# 
# links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
# duration = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]
# for index in range(0, len(name)):
#     # Seperate movie into: 'place', 'title', 'year'
#     name_string = name[index].get_text()
#     name = (' '.join(name_string.split()).replace('.', ''))
#     name_title = name[len(str(index))+1:-7]
#     year = re.search('\((.*?)\)', name_string).group(1)
#     duration = name[:len(str(index))-(len(name))]
#     data = {"name_title": name_title,
#             "year": year,
#             "place": place,

# # Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# b) Top 10 ODI Batsmen along with the records of their team and rating.
# c) Top 10 ODI bowlers along with the records of their team and rating.

# In[20]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }

urls =[ 
"https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting",
"https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling",
]

final_result_file_name = "All Ranking List.csv"
final_column_names = ["Ranking Type", "Position", "Player Name", "Team Name", "Rating", "Career Best Rating", "Crawl URL"]
pd.DataFrame(columns=final_column_names).to_csv(final_result_file_name, sep="\t", index=False, encoding="utf-8")

for url in urls:
    request_object = requests.get(url, headers=headers)
    html_content = request_object.text
    print(request_object.status_code, "->", url)
    soup_object = BeautifulSoup(html_content, "lxml")
    for element in soup_object.select('[class="ranking-pos up"], [class="ranking-pos down"]'):
        element.replace_with(BeautifulSoup("<" + element.name + "></" + element.name + ">", "html.parser"))

    ranking_type = soup_object.select_one(".rankings-block__title-container > h4").text

    result_file_name = ranking_type + ".csv"
    column_names = ["Position", "Player Name", "Team Name", "Rating", "Career Best Rating", "Crawl URL"]
    pd.DataFrame(columns=column_names).to_csv(result_file_name, sep="\t", index=False, encoding="utf-8")

    for element in soup_object.select('table[class="table rankings-table"] tr'):
        if(element.find("th")):
            continue
        data_dict = dict()
        data_dict["Crawl URL"] = url
        data_dict["Ranking Type"] = ranking_type
        if(element.select_one('[class*="position"]')):
            data_dict["Position"] = element.select_one('[class*="position"]').text
        for player_name in (element.select('a[href*="/player-rankings"]')):
            if(player_name.text.strip()):
                data_dict["Player Name"] = player_name.text
        if(element.select_one('[class^="flag-15"]')):
            data_dict["Team Name"] = element.select_one('[class^="flag-15"]')["class"][-1]
        if(element.select_one('[class$="rating"]')):
            data_dict["Rating"] = element.select_one('[class$="rating"]').text
        if(element.select_one('td.u-hide-phablet')):
            data_dict["Career Best Rating"] = element.select_one('td.u-hide-phablet').text
        for key in data_dict.keys():
            data_dict[key] = re.sub(r"\s+", " ", data_dict[key])
            data_dict[key] = data_dict[key].strip()
        pd.DataFrame([data_dict], columns=column_names).to_csv(result_file_name, sep="\t", index=False, header=False, encoding="utf-8", mode="a")
        pd.DataFrame([data_dict], columns=final_column_names).to_csv(final_result_file_name, sep="\t", index=False, header=False, encoding="utf-8", mode="a")


# # Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# b) Top 10 women’s ODI Batting players along with the records of their team and rating.
# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[21]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }

urls = [
"https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting",
"https://www.icc-cricket.com/rankings/womens/player-rankings/odi/bowling",
]

final_result_file_name = "All Ranking List.csv"
final_column_names = ["Ranking Type", "Position", "Player Name", "Team Name", "Rating", "Career Best Rating", "Crawl URL"]
pd.DataFrame(columns=final_column_names).to_csv(final_result_file_name, sep="\t", index=False, encoding="utf-8")

for url in urls:
    request_object = requests.get(url, headers=headers)
    html_content = request_object.text
    print(request_object.status_code, "->", url)
    soup_object = BeautifulSoup(html_content, "lxml")
    for element in soup_object.select('[class="ranking-pos up"], [class="ranking-pos down"]'):
        element.replace_with(BeautifulSoup("<" + element.name + "></" + element.name + ">", "html.parser"))

    ranking_type = soup_object.select_one(".rankings-block__title-container > h4").text

    result_file_name = ranking_type + ".csv"
    column_names = ["Position", "Player Name", "Team Name", "Rating", "Career Best Rating", "Crawl URL"]
    pd.DataFrame(columns=column_names).to_csv(result_file_name, sep="\t", index=False, encoding="utf-8")

    for element in soup_object.select('table[class="table rankings-table"] tr'):
        if(element.find("th")):
            continue
        data_dict = dict()
        data_dict["Crawl URL"] = url
        data_dict["Ranking Type"] = ranking_type
        if(element.select_one('[class*="position"]')):
            data_dict["Position"] = element.select_one('[class*="position"]').text
        for player_name in (element.select('a[href*="/player-rankings"]')):
            if(player_name.text.strip()):
                data_dict["Player Name"] = player_name.text
        if(element.select_one('[class^="flag-15"]')):
            data_dict["Team Name"] = element.select_one('[class^="flag-15"]')["class"][-1]
        if(element.select_one('[class$="rating"]')):
            data_dict["Rating"] = element.select_one('[class$="rating"]').text
        if(element.select_one('td.u-hide-phablet')):
            data_dict["Career Best Rating"] = element.select_one('td.u-hide-phablet').text
        for key in data_dict.keys():
            data_dict[key] = re.sub(r"\s+", " ", data_dict[key])
            data_dict[key] = data_dict[key].strip()
        pd.DataFrame([data_dict], columns=column_names).to_csv(result_file_name, sep="\t", index=False, header=False, encoding="utf-8", mode="a")
        pd.DataFrame([data_dict], columns=final_column_names).to_csv(final_result_file_name, sep="\t", index=False, header=False, encoding="utf-8", mode="a")


# # Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :
# i) Headline
# ii) Time
# iii) News Link

# In[24]:


import requests
from bs4 import BeautifulSoup

url='https://www.cnbc.com/world/?region=world'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h3')
for x in headlines:
    print(x.text.strip())


# # Write a python program to scrape the details of most downloaded articles from AI in last 90 days.
# https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
# Scrape below mentioned details :
# i) Paper Title
# ii) Authors
# iii) Published Date
# iv) Paper URL

# In[28]:


get_ipython().system('pip install beautifulsoup4')
from bs4 import BeautifulSoup

# this function for the getting inforamtion of the web page
url='https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles'
response=requests.get(url,headers=headers)
# this function for the extracting information of the tags
def get_tags(url):
  paper_tag = doc.select('[data-lid]')
  cite_tag = doc.select('[title=Cite] + a')
  link_tag = doc.find_all('h3',{"class" : "gs_rt"})
  author_tag = doc.find_all("div", {"class": "gs_a"})

  return paper_tag,cite_tag,link_tag,author_tag

# check successful response
  if response.status_code != 200:
    print('Status code:', response.status_code)
    raise Exception('Failed to fetch web page ')

#parse using beautiful soup
  paper_doc = BeautifulSoup(response.text,'html.parser')

  return paper_doc
# it will return the title of the paper
def get_papertitle(paper_tag):
  
  paper_names = []
  
  for tag in paper_tag:
    paper_names.append(tag.select('h3')[0].get_text())

  return paper_names
# function for the getting autho , year and publication information
def get_author_year_publi_info(authors_tag):
  years = []
  publication = []
  authors = []
  for i in range(len(authors_tag)):
      authortag_text = (authors_tag[i].text).split()
      year = int(re.search(r'\d+', authors_tag[i].text).group())
      years.append(year)
      publication.append(authortag_text[-1])
      author = authortag_text[0] + ' ' + re.sub(',','', authortag_text[1])
      authors.append(author)
  
  return years , publication, authors


# # Write a python program to scrape the details of top publications from Google Scholar from
# https://scholar.google.com/citations?view_op=top_venues&hl=en
# i) Rank
# ii) Publication
# iii) h5-index
# iv) h5-median

# In[29]:


import requests, lxml
from bs4 import BeautifulSoup
import pandas as pd


def scrape_all_metrics_top_publications():

    params = {
        "view_op": "top_venues",  # top publications results
        "hl": "en"  # or other lang: pt, sp, de, ru, fr, ja, ko, pl, uk, id
        }

    # https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
    # whatismybrowser.com/detect/what-is-my-user-agent
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Safari/537.36"
        }

    html = requests.get("https://scholar.google.com/citations?view_op=top_venues&hl=en", params=params, headers=headers, timeout=30)
    soup = BeautifulSoup(html.text, "lxml").find("table")

    df = pd.DataFrame(pd.read_html(str(soup))[0])
    df.drop(df.columns[0], axis=1, inplace=True)
    df.insert(loc=2,
              column="h5-index link",
              value=[f'https://scholar.google.com/{link.a["href"]}' for link in soup.select(".gsc_mvt_t+ td")])

    df.to_csv("google_scholar_metrics_top_publications.csv", index=False)

    # save to csv for specific language
    # df.to_csv(f"google_scholar_metrics_top_publications_lang_{params['hl']}.csv", index=False)

scrape_all_metrics_top_publications()


# In[ ]:





# In[ ]:




