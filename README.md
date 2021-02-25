# Mission To Mars

## Objective

Use Beautiful Soup and Splinter to web scrape data from:  
* [NASA Mars News Site](https://mars.nasa.gov/news/)  
* [JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)  
* [Mars Space Facts](https://space-facts.com/mars)  
* [USGS Astrogeology Site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)  

Then use MongoDB and Flask to showcase results on a webpage.  

The scrape will pull the following information about the planet 
Mars:  

* NASA: Latest News title and teaser  
* JPL: Featured Mars Image  
* Space-Facts: Table of facts containing diameter, mass, moons, orbit, temperature, etc.  
* USGS: Full size image of Mars' four hemispheres  

## Code

Developed code in Jupyter Notebook in order to test code.  Imported dependencies and connected to Chromedriver to allow browser to access webpages in order to scrape.  

I scraped [NASA Mars News Site](https://mars.nasa.gov/news/) first for the latest news title and teaser text using BeautifulSoup to parse through HTML for correct elements and classes with relevant information.  
Next, the Jet Propulsion Laboratory [image page of Mars](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) was scraped. In order to pull the correct image, I had to find the correct href and combine it with the JPL URL.  
I then visited the [Mars Space Facts website](https://space-facts.com/mars) and used pd.read_html() to scrape the table data on the page. I took the first table [0] and renamed the columns. The dataframe was then converted into an HTML table.  
Finally, visted the [USGS Astrogeology Site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to scrape the images of Mars' four hemispheres. The page shows 4 thumbnails of Mars' hemisphere, not full images.  Generated loop to run each thumbnail page URL inorder for scrape to access correct page with full image.  It then used Beautiful Soup to parse through HTML where it found the "wide-image" class.  It then combined the USGS URL and the found wide-image source in order to populate the full image.  It also pulled the image titles of each hemisphere and appended Title and Image to a list.  

After the code worked in Jupyter Notebook, it was transfered to Visual Studio Code as a python file.  All the scraped data was then compiled into a dictionary to be returned at the end of the function.  

## Website

In another Python file, Flask, PyMongo and scrape_mars was imported as dependencies.  PyMongo was used to connect with the MongoDB server while Flask was used to activate the scrape function. This app.py would prompt scrape and update MongoDB with this information which the results are then visualized through the index.html.  
![1-Web](https://github.com/bourbonracer/Mars-Mission-Scrape/blob/master/Mission_to_Mars/Mission_to_Mars.JPG?raw=true)  
![2-Hemispheres](https://github.com/bourbonracer/Mars-Mission-Scrape/blob/master/Mission_to_Mars/Mars_Hemisphere_Grid.JPG?raw=true)


