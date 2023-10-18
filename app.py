from flask import Flask
from selenium import webdriver
import time

app = Flask(__name__)


@app.route('/')
def run_selenium():
    print("Test Execution Started")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Remote(
        command_executor='http://standalone-chromium:4444/wd/hub',
        options=chrome_options,
    )

    driver.maximize_window()
    time.sleep(10)
    driver.get("https://www.youtube.com/")
    time.sleep(10)
    driver.close()
    driver.quit()
    print("Test Execution Successfully Completed!")

    return "Selenium test executed successfully!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8983)
