from selenium import webdriver
from time import sleep
from pandas import DataFrame
from pandas import ExcelWriter
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()

hostname = "http://127.0.0.1"
port = "24001"

#options.add_argument('--proxy-server=%s' % hostname + ":" + port)
options.add_argument('--disable-extensions')
options.add_argument('--profile-directory=Default')
options.add_argument("--disable-plugins-discovery");
options.add_argument("--start-maximized")

sheet = ExcelWriter('review_sheet.xlsx')
driver = webdriver.Chrome(options=options)
lis = []
links = ['https://www.walmart.com/ip/Masterbuilt-Gravity-Series-560-Digital-Charcoal-Grill-Smoker/811864559',]
'''
for link in open('in.csv', 'r'):
    links.append(link)
'''
    

for link in links:
    while True:
        try:
            driver.get(link)
            break
        except:
            pass
    
    while True:
        try:
            
            xpath = driver.find_element_by_xpath
            
            #xpath('//button[@class="button Reviews-seeAllButton button--primary"]').click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "See all reviews")]'))).click()
            
            xpaths = driver.find_elements_by_xpath
            #xpath('//h1[@data-automation-id="product-review-title"]')
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//h1[@data-automation-id="product-review-title"]')))
            page_url = driver.current_url
            break
        except:
            pass
    '''
    try:
        pages = xpaths('//ul[@class="paginator-list"]/li')[-1].text
    except:
        pages = 3
    
    for pag in range(1,int(pages)):
        while True:
            try:
                if int(pages)==3:
                    pass
                else:
                    page_link = page_url+'?page='+str(pag)
                    driver.get(page_link)
                break
            except:
                pass
    '''
    while True:
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="Grid ReviewList-content"]')))

            for container in xpaths('//div[@class="Grid ReviewList-content"]'):
                subx = container.find_element_by_xpath
                subxs = container.find_elements_by_xpath
                
                link = link
                try:
                    review_title = subx('.//h3[@itemprop="name"]').text
                except:
                    review_title = ''
                    
                try:
                    review_text = subx('.//div[@class="collapsable-content-container"]').text
                except:
                    review_text = ''
                    
                try:
                    datetime = subx('.//span[@itemprop="datePublished"]').text
                except:
                    datetime = ''
                try:                
                    location = ''
                except:
                    location = ''
                try:
                    
                    name = subx('.//span[@itemprop="author"]').text
                    rat = subxs('.//span[@class="elc-icon star star-small star-rated elc-icon-star-rating"]')
                    rating = str(len(rat))
                    print(name)
                    li = (link, review_title, review_text, datetime, location, name, rating)
                    lis.append(li)

                except:
                    pass
        except:
            pass
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="paginator-btn paginator-btn-next"]'))).click()
            sleep(2)
        except:
            break
df = DataFrame(lis)
df.to_excel(sheet, sheet_name='sheet')
sheet.save()
driver.close()
