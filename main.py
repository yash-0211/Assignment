from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv

# creating data.csv file
file= open('data.csv', 'w')
writer = csv.writer(file)
fields =["Est. Value Notes", "Description", "Closing Date"]
writer.writerow(fields)

print("Starting automation..")

# creating webdriver object to visit url 
options = Options()
options.add_argument('--ignore-certificate-errors')
browser = webdriver.Chrome(options=options)
link= "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"
browser.get(link)
time.sleep(3)

# clicking on the 1st posting 
print("Collecting data..")
element= browser.find_element(By.XPATH, f'//*[@id="table_id"]/tbody/tr[{1}]/td[2]/a')
browser.execute_script('arguments[0].click()', element)
time.sleep(5)

for i in range(1,6):
    # defining xpaths for the targeted fields 
    cd_xpath= '//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[1]/td[2]'
    evn_xpath= '//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[3]/td[2]'
    des_xpath= '//*[@id="current_project"]/div/div[3]/div/table/tbody/tr[3]/td[2]'

    # collecting from the HTML elements to csv file
    closing_date= browser.find_element(By.XPATH, cd_xpath).text
    est_value_notes= browser.find_element(By.XPATH, evn_xpath).text
    description= browser.find_element(By.XPATH, des_xpath).text
    row= [est_value_notes, description, closing_date]
    writer.writerow(row)

    # clicking the "next" button
    element= browser.find_element(By.XPATH, f'//*[@id="id_prevnext_next"]')
    browser.execute_script('arguments[0].click()', element)
    time.sleep(3)

browser.close()
file.close()
print("done.")