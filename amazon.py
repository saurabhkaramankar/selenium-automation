from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
web=webdriver.Chrome("C:\\browserdrivers\\chromedriver")
web.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
time.sleep(1)
login=web.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]")
login.send_keys("1234567890");
Submit=web.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input")
Submit.click()
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
web=webdriver.Chrome("C:\\browserdrivers\\chromedriver")
web.get("https://www.amazon.com")
searchbox=web.find_element_by_id("twotabsearchtextbox")
searchbox.send_keys("invicta watches for men")
time.sleep(1)
Find=web.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
Find.click()
time.sleep(1)
from selenium import webdriver
web=webdriver.Chrome("C:\\browserdrivers\\chromedriver")
Producturl="https://www.amazon.com/Invicta-Quartz-Stainless-SiliconeCasual/dp/B01G5DHJ8G?ref_=Oct_DLandingS_D_e3d0119e_60&smid=ATVPDKIKX0DER"
web.get(Producturl)
sleep(3)
web.find_element_by_id('add-to-cart-button').click()
web.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/form/div/div/div/div/div[9]/div[1]/span/span/span/input").click()
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest, time, re
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class Amazon(unittest.TestCase):
 @classmethod
 def setUp(cls):
 # Call Firefox browser
 cls.driver = webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver")
 cls.driver.implicitly_wait(30)
 #Load amazon.in site
 cls.driver.get("https://www.amazon.in/")
 cls.driver.maximize_window()
def test_amazon(self):
 # In the search box, enter ' data catalog' and search'
 self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("data catalog")
 self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").submit()
 self.driver.implicitly_wait(5) 
 print("done")
 
 first_book_title = "The Condensed Chemical Dictionary; A Reference Volume for All Requiring Quick Access to a Large Amount of Essential Data Regarding Chemicals, and ... Used in Manufacturing and Laboratory Work"
 #check for title
 title = 
self.driver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[1]/a/h2').text.strip
()
self.assertEqual(first_book_title,title)
 # check for author
 author = 
self.driver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[2]/span[2]').text
 self.assertEqual(author,"Inc Chemical Catalog Company")
 # check for paperback price 
 paperback = 
self.driver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[2]/div[2]/div[1]/div[2]/a/span').
text.strip()
 self.assertEqual(paperback,"1,499")
 # check for hardcover price
 hardcover = 
self.driver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[2]/div[2]/div[1]/div[7]/a/span').
text.strip()
 self.assertEqual(hardcover,"3,115.91")
 print("Title = ", title)
 print("Author = ", author)
 print("Paperback Price = " , paperback)
 print("Hard Cover Price = " , hardcover)
 
 @classmethod 
 def tearDown(cls):
 #Close the browser
 cls.driver.quit()
if __name__ == "__main__":
 unittest.main()
