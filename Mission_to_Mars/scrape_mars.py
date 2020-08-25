import os
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import time

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    # ------------------------------- NASA Mars News -------------------------------
    mars_news_url = 'https://mars.nasa.gov/news/'
    browser.visit(mars_news_url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    html = browser.html
    mars_news_soup = bs(html, 'html.parser')

    news_title = mars_news_soup.find('div', class_="content_title").get_text()
    news_teaser = mars_news_soup.find('div', class_='article_teaser_body').get_text()

    # ------------------------------- JPL Mars Space Images - Featured Images -------------------------------
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=mars&category=Mars#submit'
    jpl = 'https://www.jpl.nasa.gov'
    browser.visit(jpl_url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    html = browser.html
    jpl_soup = bs(html, 'html.parser')

    featured_img_path = jpl_soup.find_all('a', class_="button fancybox")[0].get('data-fancybox-href').strip()
    img_url = jpl  + featured_img_path

    # ------------------------------- Mars Facts -------------------------------
    facts_url = 'https://space-facts.com/mars/'

    tables = pd.read_html(facts_url)

    facts_df = tables[0]
    facts_df.columns=["Mars", "Measurements"]

    facts_html = facts_df.to_html()

    facts_html.replace("\n","")

    # ------------------------------- Mars Hemispheres -------------------------------
    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    usgs = "https://astrogeology.usgs.gov"
    browser.visit(usgs_url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    html = browser.html
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