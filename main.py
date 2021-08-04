from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
import concurrent.futures
import data_analysis_supreme
from anticaptchaofficial.recaptchav2proxyon import *


start = time.time()

proxy_file = open("proxies.txt")
proxies = proxy_file.readlines()


def cop(row, proxy_line):
    
    def http_proxy(i):
        prox = i.rsplit(":")
        return prox


    http = http_proxy(proxy_line)
    # proxy setup
    server = {
        'proxy': {
            'http': f"http://{http[2]}:{http[3]}@{http[0]}:{http[1]}".replace("\n", ""),
            'https': f"https://{http[2]}:{http[3]}@{http[0]}:{http[1]}".replace("\n", ""),
            'no_proxy': 'localhost,127.0.0.1',
        }
    }

    capabilities = DesiredCapabilities().CHROME
    capabilities["pageLoadStrategy"] = "none"

    #solver = recaptchaV2Proxyon()
    #solver.set_verbose(1)
    #solver.set_key(#insert api key here)
    #solver.set_website_url("http://supremenewyork.com/checkout")
    #solver.set_website_key("6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-")
    #solver.set_proxy_address(http[0])
    #solver.set_proxy_port(http[1])
    #solver.set_proxy_login(http[2])
    #solver.set_proxy_password(http[3])
    #solver.set_user_agent("Mozilla/5.0")
    #solver.set_cookies("test=true")
    #g_response = solver.solve_and_return_solution()

    print(time.time()-start)
    
    driver = webdriver.Chrome(desired_capabilities=capabilities, executable_path=r"C:\Users\aalba\OneDrive\Desktop\chromedriver.exe", seleniumwire_options=server)

    driver.get("http://www.supremenewyork.com/shop/all/t-shirts")

    item = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.LINK_TEXT, #productname)))
    item.click()

    driver.implicitly_wait(20)

    try:
        driver.find_element_by_xpath('//a[contains(@data-style-name, "#colour")]').click()
    except:
        try:
            driver.find_element_by_xpath('//a[contains(@data-style-name, "#colour")]').click()
        except:
            pass

    addToB = None
    while addToB == None:
        try:
            try:
                Select(driver.find_element_by_xpath('//*[@id = "size"]')).select_by_visible_text(#size)
                addToB = driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input')
                addToB.click()
            except:
                try:
                    Select(driver.find_element_by_xpath('//*[@id = "size"]')).select_by_visible_text(#size)
                    addToB = driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input')
                    addToB.click()
                except:
                    addToB = driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input')
                    addToB.click()
        except:
            time.sleep(1)
            driver.refresh()

    checkout = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cart"]/a[2]')))
    checkout.click()
    driver.find_element_by_xpath("//*[@id='order_billing_name']").send_keys(data_analysis.df.loc[row].Name)
    driver.find_element_by_xpath("//*[@id='order_email']").send_keys(data_analysis.df.loc[row].Email)
    driver.find_element_by_xpath("//*[@id='order_tel']").send_keys(data_analysis.df.loc[row].Phone)
    driver.find_element_by_xpath("//*[@id='bo']").send_keys(data_analysis.df.loc[row].Address)
    driver.find_element_by_xpath("//*[@id='order_billing_city']").send_keys(data_analysis.df.loc[row].City)
    driver.find_element_by_xpath("//*[@id='order_billing_zip']").send_keys(data_analysis.df.loc[row].Postcode)


    driver.find_element_by_xpath("//*[@id='cnb']").send_keys(data_analysis.df.loc[row].CardNumber)
    Select(driver.find_element_by_xpath("//*[@id='credit_card_month']")).select_by_visible_text(data_analysis.df.loc[row].ExpiryM)
    Select(driver.find_element_by_id("credit_card_year")).select_by_visible_text(data_analysis.df.loc[row].ExpiryY)
    driver.find_element_by_xpath("//*[@id='vval']").send_keys(data_analysis.df.loc[row].Security)
    driver.find_element_by_xpath("//*[@id='cart-cc']/fieldset/p/label").click()

    driver.execute_script('document.getElementById("g-recaptcha-response").innerHTML = "{}";'.format(g_response))

    #driver.find_element_by_xpath('//*[@id="pay"]/input').click()
    
    print(proxy_line)


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(cop, data_analysis.rows, proxies)
    executor.shutdown(wait=True)



print(time.time() - start)


end = input("SCRIPT ENDED")
