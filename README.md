# Scraping Mars

Here I build web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

I used Jupyter notebook file mission_to_mars.ipynb to work on each part of the code, tests and trials. When the full code was ready, I adjusted it and placed into scrape_mars.py and app.py used to create Flask and couple routs. 

Scraping process requires having chromedriver.exe file, which opens web sites and pulls data. Afterwards data and links to images saved into MongoDB. Last step is rendering my template and placing all that scraped data into it. Scraping process triggered by pressing a button on initial HTML page. 

Tools and libraries used here: Jupyter Notebook, BeautifulSoup, Pandas, chromedriver, MongoDB, Flask, flask_pymongo  and Requests/Splinter.

To run this project on your local computer download this repo, make sure you have MongoDB installed and Python v3 (with flask and flask_pymongo libraries). Run "python app.py" in command line in root repository and navigate to http://127.0.0.1:5000/. Click on "Scrape new data" button. 
