from pickle import FALSE
import urllib, json
import sys
import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
start = time.time()

# User Information 
first_name='first';
family_name='last';
email='email';
address='address';
country='USA';
city='city';
postcode='11111';
state='state';
mobile='15555555555';
CCNumber1="1111"
CCNumber2="1111"
CCNumber3="1111"
CCNumber4="1111"
CCName="ccname"
CCExpiry1="11"
CCExpiry2="11"
CCVerification="111"

# Site information
domain = "https://store.ui.com"
handle = "uvc-g4-doorbell"
#handle = 'g4-doorbell-pro-poe-adapter'
url = domain + "/products/" + handle + ".json"

# Product information
quantity = "1"

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
#options.add_argument("--headless") # Comment that line to see script running in Chrome.
driver = webdriver.Chrome(options=options)

response = urllib.request.urlopen(url)
data = json.loads(response.read())
username = 'email'
password = 'password'

checkoutDetails = 'checkout[shipping_address][first_name]='+ first_name +'&checkout[shipping_address][last_name]='+ family_name +'&checkout[email]='+ email +'&checkout[shipping_address][address1]='+ address +'&checkout[shipping_address][city]='+ city +'&checkout[shipping_address][zip]='+ postcode +'&checkout[shipping_address][country_code]='+ country +'&&checkout[shipping_address][province_code]='+ state +'&checkout[shipping_address][phone]='+ mobile;

for i in data['product']['variants']: 
    if (i['inventory_empty'] == 'false'):
        link = domain + '/cart/'+ str(i['id']) +':'+ quantity +'?'+ checkoutDetails;
        
        # Add to Cart
        driver.get(link)
        print('1. Added to the cart...');

        # Log in
        driver.find_element(By.CLASS_NAME,'loginLink').click()
        time.sleep(2)
        driver.find_element(By.NAME,'username').send_keys(username);
        driver.find_element(By.NAME,'password').send_keys(password);
        driver.find_element(By.CSS_SELECTOR,'button').click()
        print('2. Logged in...');
        
        # Choose residential and click continue to shipping
        time.sleep(2)
        driver.find_element(By.ID,'ct__radio-btn-residential').click()
        driver.find_element(By.ID,'continue_button').click()
        print('3. Selecting Shipping...');
        
        # Click continue to Payment
        time.sleep(3)
        driver.find_element(By.ID,'continue_button').click()
        print('4. Filling out Payment...');
        
        # Same as shipping address
        time.sleep(3)

        # Find CC details
        driver.find_element(By.ID,'checkout_different_billing_address_false').click() # Same as shipping address
        driver.find_element(By.XPATH,"//*[contains(@id, 'checkout_payment_gateway_')]").click(); # Click by Credit Card

        # Enter CC Number
        driver.switch_to.frame(driver.find_element(By.XPATH,"//*[contains(@id, 'card-fields-number-')]"))
        driver.find_element(By.ID,"number").send_keys(CCNumber1);
        driver.find_element(By.ID,"number").send_keys(CCNumber2);
        driver.find_element(By.ID,"number").send_keys(CCNumber3);
        driver.find_element(By.ID,"number").send_keys(CCNumber4);
    
        driver.switch_to.parent_frame();

        #Enter name
        driver.switch_to.frame(driver.find_element(By.XPATH,"//*[contains(@id, 'card-fields-name-')]"))
        driver.find_element(By.ID,"name").send_keys(first_name + " " + family_name);

        driver.switch_to.parent_frame();

        #Enter expiration date
        driver.switch_to.frame(driver.find_element(By.XPATH,"//*[contains(@id, 'card-fields-expiry-')]"))
        driver.find_element(By.ID,"expiry").send_keys(CCExpiry1);
        driver.find_element(By.ID,"expiry").send_keys(CCExpiry2);

        driver.switch_to.parent_frame();

        #Enter CC Verification
        driver.switch_to.frame(driver.find_element(By.XPATH,"//*[contains(@id, 'card-fields-verification_value-')]"))
        driver.find_element(By.ID,"verification_value").send_keys(CCVerification);

        print('5. Credit Card details entered...');
        driver.switch_to.parent_frame();

        # try to process payment.
        driver.find_element(By.ID,'continue_button').click()
        print('6. Processing payment...');
        time.sleep(3)
        
        # Pray to work ;) 
        order = driver.find_element(By.XPATH,"//span[@class='os-order-number']").get_attribute('innerHTML');
        print(order);
        print('Checkout total: ', time.time()-start, 'seconds.')
