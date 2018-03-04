from pathlib import Path

# These are paths relative to "/nice_things_django_project" directory:
labor_stats = "/data/bls_chicago.csv"
labor_stats_geocoded = "/data/bls_chicago_geocoded.csv"
food_inspections = "/data/cdp_food_dump.csv"
data_dir = "/data"
helpers_dir = "/helpers"

# Citation: https://stackoverflow.com/questions/51520/
# how-to-get-an-absolute-file-path-in-python
# This gets absolute path of "/nice_things_django_project" directory:
nice_things_django_project_dir = str(Path(__file__).resolve())
