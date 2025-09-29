from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time
import os
import re
import pytesseract
from PIL import Image

edge_options = webdriver.EdgeOptions()
edge_options.add_argument("--headless")
edge_options.add_argument("--disable-gpu")
edge_options.add_argument("--no-sandbox")

# Khởi tạo trình duyệt
try:
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)
except WebDriverException as e:
    print(f"Lỗi khi khởi tạo WebDriver: {e}")
    exit()

driver.execute_cdp_cmd('Network.clearBrowserCache', {})
driver.execute_cdp_cmd('Storage.clearDataForOrigin', {
    "origin": "*",
    "storageTypes": "all"
})