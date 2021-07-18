# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 14:54:03 2019

@author: Umar Miftah Fauzi
Code based on work from:
Samuel Chan - https://github.com/onlyphantom/pricemate
Laura Fedoruk - https://towardsdatascience.com/web-scraping-basics-selenium-and-beautiful-soup-applied-to-searching-for-campsite-availability-4a8de1decac9
"""

from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

video_ids =[]
driver = Chrome(ChromeDriverManager().install())
with driver:
    wait = WebDriverWait(driver,15)
    driver.get("https://www.youtube.com/channel/UCQxK-01l6hi0mZprya9USqg/videos")

    for item in range(200): 
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(15)

    for video_id in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
        video_ids.append(video_id.text)