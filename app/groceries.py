
# READ INVENTORY OF PRODUCTS
import os

#products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
#products_df = read_csv(products_filepath)
#products = products_df.to_dict("records")

#from folder_name.file_name import function
#in order to grab and use a funciton from another file (locally import)
from app.utils import to_usd

# checks to see if a products.csv file exists. If not, it uses the default

#I tried using the commented out variables above, but I can not define them if the file does not exist
#Additionally, I tried creating a function with the ability to substitute the syntax and make the file name 
#dynamic but this method kept being identified as a tuple not a string  
if os.path.isfile(os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")) == True:
    print("USING CUSTOM PRODUCTS CSV FILE...")
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
else:
    print("USING DEFAULT PRODUCTS CSV FILE...")
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "default_products.csv")

from pandas import read_csv

#reads the csv file into products variable
products = read_csv(csv_filepath)
#pandas transforms the data into a list of dictionaries
products = products.to_dict('records')


# PRINTED INVENTORY REPORT

print("---------")
print("THERE ARE", len(products), "PRODUCTS:")
print("---------")

all_prices = []
for p in products:
    print("..." + p["name"] + "   " + to_usd(p["price"]))
    all_prices.append(float(p["price"]))

import statistics
avg_price = statistics.mean(all_prices)

print("---------")
print("AVERAGE PRICE:", to_usd(avg_price))


# EMAIL INVENTORY REPORT
