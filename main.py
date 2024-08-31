from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

website = "https://www.thesun.co.uk/sport/football"

driver = webdriver.Chrome()
driver.get(website)

time.sleep(5)

containers = driver.find_elements(By.XPATH, '//div[@class="teaser__copy-container"]/a')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(By.XPATH, './span').text
    subtitle = container.find_element(By.XPATH, './h3').text
    link = container.get_attribute('href')

    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {
    "Titles": titles,
    "Subtitles": subtitles,
    "Links": links,
}

df_headlines = pd.DataFrame(my_dict)
df_headlines.to_excel('headlines.xlsx', index=False)
driver.quit()
