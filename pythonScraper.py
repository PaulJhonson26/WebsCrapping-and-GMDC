from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import math
import time

def loadArticles(driver, times):
    load_more = driver.find_element_by_xpath("//button[@class='options__load-more']")
    for i in range(times):
        time.sleep(0.5)
        load_more.click()

def getArticleList(driver):
    articleListDiv = driver.find_element_by_id("infinitescroll")
    allArticles = articleListDiv.find_elements_by_class_name("item-info")
    return allArticles
def parseArticle(driver):
    time.sleep(0.5)
    try:
        divP = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "storytext"))
        )
    except:
        driver.quit()
    divP = driver.find_element_by_id("storytext")
    P = driver.find_elements_by_tag_name('p')
    finalStringArticle = ""
    for i in range(len(P)):
        if(len(P[i].text) > 50): #if it's not authors etc.
            finalStringArticle = finalStringArticle + P[i].text


    print("Paragraphs: ",finalStringArticle)
    return finalStringArticle


def main():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.npr.org/sections/politics/")
    DRIVERCONST = driver.title
    time.sleep(0.5)
    loadArticles(driver, 10)
    allArticles = getArticleList(driver)
    finalArticleArray = []

    for i in range(len(allArticles)):
        print("article: ", i)
        time.sleep(0.5)
        allArticles[i].click()
        time.sleep(0.5)
        if (DRIVERCONST == driver.title):
            allArticles = getArticleList(driver)
            print("couldn't click article ", i)
        else:
            finalArticleArray.append(parseArticle(driver))
            time.sleep(0.5)
            driver.back()
            time.sleep(0.5)
            loadArticles(driver, math.ceil((i+1)/23)+1) #1 load more click loads 20 ish articles so only click every 20 articles
            allArticles = getArticleList(driver)

if __name__ == "__main__":
    main()






