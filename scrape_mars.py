from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def init_browser():
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find('div', class_='list_text')
    news_title = articles.find('a').text
    news_p = articles.find('div', class_='article_teaser_body').text

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    picture = soup.find('a', class_='button fancybox')
    featured_image_url = 'https://www.jpl.nasa.gov' + picture['data-fancybox-href']

    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
    [s.extract() for s in text('a')]
    mars_weather = text.text

    url = 'https://space-facts.com/mars/'
    browser.visit(url)
    table = pd.read_html(url)
    table = table[0]
    table = table.rename(columns = {0:'description', 1:'value'})
    table.set_index('description', inplace=True)
    html_table = table.to_html()

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find_all('div', class_='description')
    hemisphere_image_urls = []
    for article in articles:        
        title = article.a.text
        target_url = 'https://astrogeology.usgs.gov' + article.a['href']        
        browser.visit(target_url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        img_url = soup.find('a', target="_blank")['href']
        temp_dic = {
            "title": title,
            "img_url": img_url
        }        
        hemisphere_image_urls.append(temp_dic) 

    my_dict = {
        "news_title":news_title,
        "news_p":news_p,
        "featured_image_url":featured_image_url,
        "mars_weather":mars_weather,
        "html_table":html_table,
        "hemisphere_image_urls":hemisphere_image_urls
    }

    browser.quit()
    
    return my_dict