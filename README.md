# We Can Have Nice Things

Repository for CAPP 30122 Winter 2018 Project

  * Alexander Tyan (AlexanderTyan)
  * Kevin Sun (Sun-Kev)
  * Tyler Amos (tamos)
  
# Set up

### 1. Install PostgreSQL

Follow the instructions on django-girls for PostgreSQL install (NOTE: For creating the database user and the database, follow step 2 in this README):

https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation/


### 2. Now create a PostgrSQL user nice_things. In PostgreSQL:
  
  CREATE USER nice_things LOGIN password '';

You may need to specify a password. If that happens, go to nice_things_django_project/settings.py and change the following line:

  'PASSWORD': ''
  
  To:
  
  'PASSWORD': 'uccs'
  
 And then try:
 
  CREATE USER nice_things LOGIN password 'uccs';
  
  CREATE DATABASE nice_things_db OWNER nice_things;
  
### 3. Install dependencies:

cd to your local clone of the repository nice_things and run:

pip3 install -r requirements.txt

Or if you are on the UChicago Student Ubuntu VM:

sudo -H pip3 install -r requirements.txt
  
### 3. Leave PostgresSQL running and now, in a new terminal:
  
  python3 manage.py makemigrations
  
  python3 manage.py migrate
  
### 4. Open the Django manage.py shell:
  
  python3 manage.py shell
  
### 5. Run the following commands:
  
  import update_db
  
  update_db.update_database()
  
### 6. Exit to terminal, and:
  
  python3 manage.py runserver
  
### 7. Enjoy your nice things. 

# Code Attribution

Due to the design of the project, all areas of code were worked on by all members. 

# References

* Python documentation (python.org)
* W3Schools (w3schools.com)
* Leaflet (leafletjs.com)
* For each package or API used, our code draws from examples and tutorials provided in the documentation.
* When external resources, e.g., StackOverflow were consulted, they are cited in the code. 

# Data Sources
 
 #### Bureau of Labor Wage and Hour Compliance Data: https://enforcedata.dol.gov/views/data_summary.php
 
"The dataset contains all concluded WHD compliance actions since FY 2005. The dataset includes whether any violations were found and the back wage amount, number of employees due back wages, and civil money penalties assessed. " (Ibid)
 
 #### City of Chicago Data Portal: https://data.cityofchicago.org
 
 1. Environmental Records Lookup: https://data.cityofchicago.org/Environment-Sustainable-Development/CDPH-Environmental-Records-Lookup-Table/a9u4-3dwb
 
 "This dataset serves as a lookup table to determine if environmental records exist in a Chicago Department of Public Health (CDPH) environmental dataset for a given address." (Ibid)
 
 From this dataset, we use: 
 
 "COMPLAINTS: A ‘Y’ indicates that one or more records exist in the CDPH Environmental Complaints dataset." and "ENFORCEMENT: A ‘Y’ indicates that one or more records exist in the CDPH Environmental Enforcement dataset. " (Ibid)
 
 2. Food Inspections: https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5
 
"This information is derived from inspections of restaurants and other food establishments in Chicago from January 1, 2010 to the present. Inspections are performed by staff from the Chicago Department of Public Health’s Food Protection Program using a standardized procedure. The results of the inspection are inputted into a database, then reviewed and approved by a State of Illinois Licensed Environmental Health Practitioner (LEHP). For descriptions of the data elements included in this set, go to http://bit.ly/tS9IE8 "  (Ibid) 

3. Divvy Bike Share Locations: https://www.divvybikes.com/system-data (Q3/4 2017)

Q3 and Q4 data for 2017 was used to identify the locations of Divvy stations. The data was provided with the trips dataset which can be downloaded above. The data used in this repository was downloaded on March 5, 2018.
 
# Python Modules and Tools Used:

 * yelpapi: https://github.com/gfairchild/yelpapi
    * This package was updated by the group and submitted as a pull request. See https://github.com/gfairchild/yelpapi/pull/8
 
 * pandas: https://pandas.pydata.org
 
 * requests: http://docs.python-requests.org/en/master/
 
 * dominate: https://github.com/Knio/dominate
 
  * django-geojson: https://django-geojson.readthedocs.io/en/latest/installation.html

 * leaflet: http://leafletjs.com

 * django-leaflet: https://django-leaflet.readthedocs.io

 * record_linkage: http://recordlinkage.readthedocs.io
 
 
 
 # All API keys are provided in the Gitlab repository (tylera). The main APIs used are:

Google Maps: https://developers.google.com/maps/documentation/geocoding/intro

Mapbox (for vector tile layers): https://www.mapbox.com

Chicago Data Portal: https://data.cityofchicago.org

Yelp: https://www.yelp.com/developers
  
 
 
