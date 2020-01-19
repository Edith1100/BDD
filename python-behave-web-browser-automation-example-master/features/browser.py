from selenium import webdriver


class Browser(object):

    driver = webdriver.Chrome('C:/Users/User/Anaconda3/chromedriver')
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(context):
        context.driver.close()

    def find_title(context):
        return context.driver.find_element_by_class_name("homepage-banner__title")
