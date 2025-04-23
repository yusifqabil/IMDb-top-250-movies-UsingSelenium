from selenium import webdriver 
from selenium.webdriver.common.by import By
import pandas as pd
driver = webdriver.Chrome()
result = []
driver.get("https://www.imdb.com/chart/top/")
allMovies = driver.find_elements(By.CLASS_NAME,"ipc-metadata-list-summary-item")
for movie in allMovies : 
    name = movie.find_element(By.TAG_NAME,"h3").text
    rating = movie.find_element(By.CLASS_NAME,"ipc-rating-star--rating").text 
    allSpans = movie.find_elements(By.TAG_NAME,"span")
    year = allSpans[1].text
    duration = allSpans[2].text
    result.append((name,year,duration,rating))
df = pd.DataFrame(result,columns=["name","year","duration","rating"])
with open("output.csv","w") as out : 
    df.to_csv(out,index=False)
driver.quit()