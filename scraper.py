from bs4 import BeautifulSoup as bs
import pandas as pd
import requests as req

link = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

headers = ["name", "distance", "mass", "radius"]

webpage = req.get(link, verify=False)

soup = bs(webpage.text, "html.parser")

data = []
