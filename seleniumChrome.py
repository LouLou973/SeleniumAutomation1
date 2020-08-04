from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Safari()
driver.maximize_window()
driver.get("https://www.youtube.com/")

driver.find_element_by_id("search-input").click()
driver.find_element_by_id("search-input").send_keys("VINTAGE RADIO (LIVE OLDIES 24/7!)")
time.sleep(2)
driver.find_element_by_id("search-icon-legacy").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[2]/div[1]/ytd-thumbnail/a/yt-img-shadow/img").click()
time.sleep(5)
driver.quit()