import os
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import time

# NASA Mars News
def init_browser():
    executable_path = {'executable_path': '../../../Chromedriver/chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    mars_news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(mars_news_url)

    html = browser.html
    time.sleep(7)
    mars_news_soup = bs(html, 'html.parser')

    news_result = mars_news_soup.find('div', class_="list_text")

    news_title = news_result.find('div', class_="content_title").find('a').text
    news_teaser = news_result.find('div', class_='article_teaser_body').text

    # print('--------------------------------------------------------------')
    # print(f'Latest News Title: {news_title}')
    # print('--------------------------------------------------------------')
    # print(f'Teaser Paragraph: {news_teaser}')
    # print('--------------------------------------------------------------')

    # JPL Mars Space Images - Featured Images
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    jpl = 'https://www.jpl.nasa.gov'
    browser.visit(jpl_url)

    html = browser.html
    time.sleep(7)
    jpl_soup = bs(html, 'html.parser')

    featured_img_path = jpl_soup.find_all('a', class_="button fancybox")[0].get('data-fancybox-href').strip()
    img_url = jpl  + featured_img_path
    # print(f'Featured Image: {img_url}')

    # Mars Facts
    facts_url = 'https://space-facts.com/mars/'

    tables = pd.read_html(facts_url)

    facts_df = tables[0]
    facts_df.columns=["Mars", "Measurements"]

    facts_html = facts_df.to_html()

    facts_html.replace("\n","")
    # print(facts_html)

    # Mars Hemispheres
    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    usgs = "https://astrogeology.usgs.gov"
    browser.visit(usgs_url)

    html = browser.html
    time.sleep(7)
    usgs_soup = bs(html, 'html.parser')

    usgs_results =  usgs_soup.find('div', class_="result-list")
    usgs_item = usgs_results.find_all('div', class_="item")

    hemisphere_data = []
    for x in usgs_item:
        img_title = x.find('h3').text
        page_url = x.find('a')['href']
        img_link = usgs + page_url
        browser.visit(img_link)
        mars_img_html = browser.html
        mars_img_soup = bs(mars_img_html, 'html.parser')
        mars_img = mars_img_soup.find('img', class_="wide-image")['src']
        full_img = usgs + mars_img
        hemisphere_data.append({"Title": img_title, "IMG": full_img})
    
    mars_data = {
        "latest_news_title": news_title,
        "news_teaser": news_teaser,
        "feat_img_url": img_url,
        "mars_facts_html": facts_html,
        "hemisphere": hemisphere_data
    }

    browser.quit()

    return mars_data