import glassdoor_scrapper as gs
import pandas as pd

path = "C:/Users/salar.ahmad/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 25, False, path, 10)

df.to_csv("Data.csv", index=False)