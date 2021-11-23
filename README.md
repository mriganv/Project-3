# Project 4: US Job Market Analysis
Website: http://project3-us-job-market-analysis.azurewebsites.net/
## Project Description
* Web Scraped job listings from [Indeed.com](https://www.indeed.com/) & [USAjob.gov](https://www.usajobs.gov/) using Python libraries Splinter and BeautifulSoup
* In addition to web scraped data, took Job Satisfaction Survey of Data Professionals from [Kaggle.com](https://www.kaggle.com/phuchuynguyen/datarelated-developers-survey-by-stack-overflow)
* Analysis on recent US job market split by Government and Non-Government
* Comparison analysis on government jobs vs private/public sector jobs 
   * Map: clustered markers & customized markers via Leaflet
   * Bar: animated and distributed by job categories related to Data Professionals via [CanvasJS](https://canvasjs.com/javascript-charts/animated-chart/)
* Analysis of job descriptions across the two datasets - Government and Non-Government
   * Bar: taken key words (skills and tools) from Job Descriptions and analyzing what skills companies are looking for when they hire Data Professionals
   * Pie: Analysis of Job Satisfaction survey (taken by Data Professionals)
<!-- * Analysis on salary by industry and occupation (2020)
   * Bar: animated and distributed by industry and occupation via Plotly
* Statistical analysis on Occupations by state (2020)
   * Map: choropleth layers sorted by occupation via Leaflet -->

### Data Resources:

* [Indeed Jobs](https://us-job-market-mw.s3.us-west-2.amazonaws.com/mw_job_listings_scraped.csv)
* [USA Government Jobs](https://us-job-market-mw.s3.us-west-2.amazonaws.com/mw_govjob_listings_scraped.csv)
* [Job Satisfaction Survey (Data Professionals)](https://www.kaggle.com/phuchuynguyen/datarelated-developers-survey-by-stack-overflow)
* [Other](https://github.com/mriganv/Project-3-Project-4/tree/main/static/resources)

### Technologies used:

* Python: Pandas, Matplotlib, Splinter, BeautifulSoup, [Nominatim and geopy](https://medium.com/analytics-vidhya/how-to-generate-lat-and-long-coordinates-of-city-without-using-apis-25ebabcaf1d5)(for geolocation)
* Javascript: Plotly, D3, Leaflet, [CanvasJS](https://canvasjs.com/javascript-charts/animated-chart/)
* HTML & CSS: Bootstrap
* Amazon S3
* Amazon RDS Aurora, PostgreSQL
* Tableau
* JSON & GEOJSON
* Excel



## Our Team

* [Marta Woodkowski](https://github.com/MartaWoodkowski)
* [Chithra Priya Janardhana](https://github.com/mriganv)
* [Shan Jiang](https://github.com/FrankJiang1208)
* [Maryam Hejripour](https://github.com/mforoohi)
* [Andrew Su](https://github.com/isoju)

