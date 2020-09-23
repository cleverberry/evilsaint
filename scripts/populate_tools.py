

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


SOURCE_FILE = 'github-tools.txt'
DEST_FILE = 'github-tools-template.txt'

source_file = open(SOURCE_FILE, 'r')
dest_file = open(DEST_FILE, 'w+', encoding="utf-8")

lines = source_file.readlines()

for line in lines:

    driver.get(line)
    about = 'No available description'
    try:
        elem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-repo-pjax-container"]/div[2]/div/div[2]/div[2]/div/div[1]/div/p')))
        about = elem.text
        print(about)
    except:
        print("Loading took too much time!")

    index = line.rfind('/')
    name = line[index+1:-1]
    org = line[:index]
    link = 'https://evilsaint.co.uk/tools/github/' + org + '-' + name
    template = '<li class="list-group-item"><a href="' + link + '" target="_blank" data-toggle="tooltip" data-placement="bottom" title="' + about + '">' + name + '</a></li>'
    dest_file.write(template + '\n')

dest_file.close()
source_file.close()
driver.close()