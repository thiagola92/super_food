import os
import time

from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

cwd = os.getcwd() + '/chromedriver'

super_zip_code = '91105'
super_email = 'thiagola92@gmail.com'
super_password= 'password'

amazon_login = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
amazon_prime_now = "https://primenow.amazon.com/home"
amazon_whole_food = "https://primenow.amazon.com/home?ref_=pn_gw_nav_sbs_1_A256W4XWLHBSNZ&requestedBrandId=V2hvbGUgRm9vZHMgTWFya2V0"

def login():
  driver.get(amazon_login)

  wait.until(lambda d: d.find_element_by_id('ap_email'))
  driver.find_element_by_id('ap_email').send_keys(super_email + '\n')

  wait.until(lambda d: d.find_element_by_id('ap_password'))
  driver.find_element_by_id('ap_password').send_keys(super_password + '\n')

def enter_zip_code():
  driver.get(amazon_prime_now)

  try:
    wait.until(lambda d: d.find_element_by_id('lsPostalCode'))
    driver.find_element_by_id('lsPostalCode').send_keys(super_zip_code + '\n')
  except Exception as e:
    # Probably already knows your zip code
    pass

def check_whole_food():
  driver.get(amazon_whole_food)
  wait.until(lambda d: d.find_element_by_id('nawMessageBox'))
  text = driver.find_element_by_id('nawMessageBox').text

  if "temporarily sold out" not in text:
    print('\x1b[42m\x1b[97m AVAILABLE \x1b[99m\x1b[49m')
    return True

  print('\x1b[41m\x1b[97m NOT AVAILABLE \x1b[99m\x1b[49m')
  return False

with Chrome(executable_path=cwd, options=options) as driver:
  wait = WebDriverWait(driver, 10)

  login()
  enter_zip_code()

  available = False
  while True:
    available = check_whole_food()
    time.sleep(60)