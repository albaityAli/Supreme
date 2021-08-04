from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.ext import commands
from selenium.webdriver.support.ui import Select


opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:1234")
driver = webdriver.Chrome(executable_path=r"C:\\Users\\aalba\\OneDrive\\Desktop\\chromedriver.exe",options=opt)
client = commands.Bot(command_prefix = "!")

def auto_fill():
    driver.find_element_by_xpath("//*[@id='order_billing_name']").send_keys(#full name)
    driver.find_element_by_xpath("//*[@id='order_email']").send_keys(#email)
    driver.find_element_by_xpath("//*[@id='order_tel']").send_keys(#phone number)
    driver.find_element_by_xpath("//*[@id='bo']").send_keys(#address line 1)
    driver.find_element_by_xpath("//*[@id='order_billing_city']").send_keys(#city)
    driver.find_element_by_xpath("//*[@id='order_billing_zip']").send_keys(#postcode)
    driver.find_element_by_xpath("//*[@id='cnb']").send_keys(#card number)
    month = Select(driver.find_element_by_xpath("//*[@id='credit_card_month']"))
    month.select_by_visible_text(#month of expiry)
    year = Select(driver.find_element_by_id("credit_card_year"))
    year.select_by_visible_text(#year of expiry)
    driver.find_element_by_xpath("//*[@id='vval']").send_keys(#security code)
    driver.find_element_by_xpath("//*[@id='cart-cc']/fieldset/p/label").click()

#copy and paste the following command for debugging version of chrome:
#cd C:\Program Files\Google\Chrome\Application
#chrome.exe --remote-debugging-port=1234 --user-data-dir="C:\Users\aalba\OneDrive\Desktop\Chrome Profile"




@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def autofill(ctx):
    auto_fill()

client.run(#discord api key)
