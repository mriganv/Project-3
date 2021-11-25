# Project 4: US Job Market for Data Professionals
Website: http://project3-us-job-market-analysis.azurewebsites.net/
## Project Description
* Acquire data through Web Scraping job listings from [Indeed.com](https://www.indeed.com/) & [USAjob.gov](https://www.usajobs.gov/) using Python libraries Splinter and BeautifulSoup
* In addition to web scraped data, took Job Satisfaction Survey of Data Professionals from [Kaggle.com](https://www.kaggle.com/)
* Analysis on recent US job market split by Government and Non-Government
* Comparison analysis on government jobs vs private/public sector jobs 
   * [Map](http://project3-us-job-market-analysis.azurewebsites.net/job_market): clustered markers & customized markers via Leaflet
   * [Bar](http://project3-us-job-market-analysis.azurewebsites.net/job_cat): animated and distributed by job categories related to Data Professionals via D3 and CanvasJS
* Analysis of job descriptions across the two datasets - Government and Non-Government
   * [Bar](https://public.tableau.com/app/profile/marta.woodkowski/viz/SkillscompanieslookforwhenhireDataProfessionals/SkillscompanieslookforwhenhireDataProfessionals): taken key words (skills and tools) from Job Descriptions and analyzing what skills companies are looking for when they hire Data Professionals
   * [Pie](https://public.tableau.com/app/profile/marta.woodkowski/viz/JobSatisfactionofDataProfessionals/JobSatisfactionDataProfessionals): Analysis of Job Satisfaction survey (taken by Data Professionals)
* Analysis of Average Salary of Job Categories by Location using Indeed Dataset
   * Bar: interactive chart displaying by City and Company via Tableau
   * Bubble: interactive chart displaying by State via Tableau
* Analysis of Number of Job Openings by Location and Job Category
   * Map: interactive maps depicting number of Job Openings by City and and State via Tableau
   * Bubble: organized Job Titles into categories and analyzed number of Job Openings by category
* Analysis of Salary by Job Category, Location, Tools and Skills using USAjobs Dataset
   * Bar: interactive charts displaying data on Salary by Job Category, State, Tools and Skills via Tableau
   * Boxplot: interactive Box plot displaying a five-number summary of average salary for each Job Category
   * Bubble: interactive chart displaying the count of Jobs based on each Tool
   * Map: interactive map depicting Number of Job Openings and Salary by State
* Machine Learning - Salary Prediction: Loaded onto RDS and exported as csv files from [pgadmin](https://github.com/mriganv/Project-3-Project-4/blob/main/static/notebooks/Loading_ML_Model_Data.ipynb)
   * Model 1: Random Forest Classifier
      * Feature Type: all numeric using get_dummies
      * Features: Job Titles, Salary, Skills
      * Model Accuracy: 86% with 1 bin variance error
   * Model 2: Random Forest Classifier
      * Feature Type: part text, part numeric, combined using featureunion
      * Features: 'Job Title', 'Job Description', 'Size', 'Industry', 'Salary', 'State', 'Age', Skills
      * Model Accuracy: 79% with 1 bin variance error

### Data Resources:

* [Indeed Jobs](https://us-job-market-mw.s3.us-west-2.amazonaws.com/mw_job_listings_scraped.csv) 
* [USA Government Jobs](https://us-job-market-mw.s3.us-west-2.amazonaws.com/mw_govjob_listings_scraped.csv)
* [Job Satisfaction Survey (Data Professionals)](https://www.kaggle.com/phuchuynguyen/datarelated-developers-survey-by-stack-overflow) 
* [Github resources folder](https://github.com/mriganv/Project-3-Project-4/tree/main/static/resources)

### Technologies used:

* Python: Pandas, Matplotlib, Splinter, BeautifulSoup, [Nominatim and geopy](https://medium.com/analytics-vidhya/how-to-generate-lat-and-long-coordinates-of-city-without-using-apis-25ebabcaf1d5)(for geolocation)
* Javascript: Plotly, D3, Leaflet, [CanvasJS](https://canvasjs.com/javascript-charts/animated-chart/)
* HTML & CSS: Bootstrap
* Amazon S3
* Amazon RDS Aurora, PostgreSQL
* Tableau
* Azure
* Flask
* JSON & GeoJSON
* Excel



## Our Team

* [Marta Woodkowski](https://github.com/MartaWoodkowski)
* [Chithra Priya Janardhana](https://github.com/mriganv)
* [Shan Jiang](https://github.com/FrankJiang1208)
* [Maryam Hejripour](https://github.com/mforoohi)
* [Andrew Su](https://github.com/isoju)

