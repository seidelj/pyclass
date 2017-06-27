from selenium import webdriver
import os

phantomjs_path = "/Users/joseph/bin/phantomjs"

# explicitly state where phantomjs executable is
# and indicate no log file should be created
browser = webdriver.PhantomJS(executable_path=phantomjs_path,service_log_path=os.path.devnull)

browser.get("https://www.python.org")

print browser.title
