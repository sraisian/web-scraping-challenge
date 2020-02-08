from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd
import csv
import os
import numpy as np
import pymongo



#Pyfile 1 - hold scrape functions here that app.py will call
#Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.


def init_browser():
    executable_path = {"executable_path": "/Users/sarah/Desktop/chromedriver"}
    return Browser("chrome", **executable_path, headless=True)

#have the scrapping code from jupyter file in scrape function#
def scrape():
    #NASA NEWS Website
    #Url to scrap#
    url = 'https://mars.nasa.gov/news/'
    # Retrieve page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse with 'html.parser' or maybe 'lxml'
    soup = bs(response.text, 'html.parser')
    # Examine the results, then determine element that contains sought info
    #print(soup.prettify())
    #have a variable to store title and paragraph texts
    news_title = soup.title.text
    news_p = soup.p.text

    ###JPL Mars Space Images - Featured Image
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    response = requests.get(jpl_url)
    soup = bs(response.text, 'html.parser')
    #print(soup.prettify())
    #find image url for the current Featured Mars Image and assign the url string 
    #to a variable called featured_image_url
    # pull images from website
    img = soup.find_all('a', class_="button fancybox")
    # pull image link
    picurl = image['data-fancybox-href']
    #combine with base site url
    feat_img_url = 'https://www.jpl.nasa.gov' + picurl
    #append to a list
    jpl_pic = []
    jpl_pic.append(feat_img_url)

    #Mars Weather - Twitter
    twitter_url = 'https://twitter.com/marswxreport?lang=en'
    # Retrieve page with the requests module
    response = requests.get(twitter_url)
    # Create BeautifulSoup object; parse with 'html.parser' or maybe 'lxml'
    soup = bs(response.text, 'html.parser')
    # Examine the results, then determine element that contains sought info
   # print(soup3.prettify())
    #scrape the latest Mars weather tweet from the page. 
    #Save the tweet text for the weather report as a variable called mars_weather.
    # results are returned as an iterable list
    results = soup.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    mars_weather = results[0].text
    #mars_weather

    #Mars Facts Website#
    facts_url = 'https://space-facts.com/mars/' 
    # Retrieve page with the requests module
    response = requests.get(facts_url)
    # Create BeautifulSoup object; parse with 'html.parser' or maybe 'lxml'
    soup = bs(response.text, 'html.parser')
    # Examine the results, then determine element that contains sought info
    #print(soup.prettify())
    #use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    #<tbody>
    table = pd.read_html(facts_url)
    #table[0]
    facts_df = table[0]
    facts_df.columns = ["Facts", "Value"]
    facts_df.set_index(["Facts"], inplace =True)
    #facts_df
    #Use Pandas to convert the data to a HTML table string.
    facts_html = facts_df.to_html()
    facts_html = facts_html.replace("\n","")
    #facts_html


    #Save both the image url string for the full resolution hemisphere image, 
    #and the Hemisphere title containing the hemisphere name. 
    #Use a Python dictionary to store the data using the keys img_url and title.

    #Cerberus Hemisphere
    urlhemi1 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    # Retrieve page with the requests module
    response = requests.get(urlhemi1)
    # Create BeautifulSoup object; parse with 'html.parser' or maybe 'lxml'
    soup = bs(response.text, 'html.parser')
    # Examine the results, then determine element that contains sought info
    #print(soup.prettify())
    #extract title 
    hemi1 = soup.find_all('li')
    title1 = soup.find_all('h2', class_ = 'title')
    hemi1title = title1[0].text
    #extract url for original
    hemi1 = hemi1[0]
    hemi1url = hemi1.find('a')['href']
    #print(hemi1title, hemi1url)
    #append dictionary
    hemi1_dict = {"Title": hemi1title, "url": hemi1url}
    #print(hemi1_dict)

    #Schiaperelli Hemishphere
    urlhemi2 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    # Retrieve page with the requests module
    response = requests.get(urlhemi2)
    # Create BeautifulSoup object; parse with 'html.parser' or maybe 'lxml'
    soup = bs(response.text, 'html.parser')
    # Examine the results, then determine element that contains sought info
    #print(soup.prettify())
    #extract title 
    hemi2 = soup.find_all('li')
    title2 = soup.find_all('h2', class_ = 'title')
    hemi2title = title2[0].text
    #extract url for original
    hemi2 = hemi2[0]
    hemi2url = hemi2.find('a')['href']
    #print(hemi2title, hemi2url)
    #append dictionary
    hemi2_dict = {"Title": hemi2title, "url": hemi2url}
    #print(hemi2_dict)

    #Syrtis Hemishphere
    urlhemi3 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    # Retrieve page with the requests module
    response = requests.get(urlhemi3)
    # Create BeautifulSoup object; parse with 'html.parser' or maybe 'lxml'
    soup = bs(response.text, 'html.parser')
    # Examine the results, then determine element that contains sought info
    #print(soup.prettify())
    #extract title 
    hemi3 = soup.find_all('li')
    title3 = soup.find_all('h2', class_ = 'title')
    hemi3title = title3[0].text
    #extract url for original
    hemi3 = hemi3[0]
    hemi3url = hemi3.find('a')['href']
    #print(hemi3title, hemi3url)
    #append dictionary
    hemi3_dict = {"Title": hemi3title, "url": hemi3url}
    #print(hemi3_dict)

    #Valles Hemisphere
    urlhemi4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    # Retrieve page with the requests module
    response = requests.get(urlhemi4)
    # Create BeautifulSoup object; parse with 'html.parser' or maybe 'lxml'
    soup = bs(response.text, 'html.parser')
    # Examine the results, then determine element that contains sought info
    #print(soup.prettify())
    #extract title 
    hemi4 = soup.find_all('li')
    title4 = soup.find_all('h2', class_ = 'title')
    hemi4title = title4[0].text
    #extract url for original
    hemi4 = hemi4[0]
    hemi4url = hemi4.find('a')['href']
    #print(hemi4title, hemi4url)
    #append dictionary
    hemi4_dict = {"Title": hemi4title, "url": hemi4url}
    #print(hemi4_dict)
    #Append the dictionary with the image url string and the hemisphere title to a list. 
    #This list will contain one dictionary for each hemisphere.
    hemisphere_img_url = [hemi1_dict, hemi2_dict, hemi3_dict, hemi4_dict]
    #print(hemisphere_img_url)
    
    #return one Python dictionary containing all scraped data

    mars_data = {
     "Nasa_News_Title": news_title,
     "Nasa_News_Text": news_p,
     "Most_Recent_Mars_Image": jpl_pic,
     "Mars_Weather": mars_weather,
     "Mars Facts":facts_html,
     "Hemispheres": hemisphere_img_url
     }
    
    return mars_data
