

from selenium import webdriver
import time
def get_drvier():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_button_basic")
  return driver

def main():
  driver = get_drvier()
  # time.sleep(2)
  element = driver.find_element(by="xpath", value="/html/body/div[4]/div[3]/div/div/div/div[6]/div[1]/div/div/div/div[5]/pre[6]/span/span[4]")
  return element.text

print(main())