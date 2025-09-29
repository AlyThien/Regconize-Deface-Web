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
import tempfile


# Cấu hình đường dẫn Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Đọc các URL từ file zoneh_26-50.txt
file_path = "D:/IE105/onhold_zone.txt"
with open(file_path, "r") as file:
    urls = [line.strip() for line in file.readlines() if line.strip()]

# Cấu hình trình duyệt edge ở chế độ headless 
edge_options = webdriver.EdgeOptions()
edge_options.add_argument("--headless")
edge_options.add_argument("--disable-gpu")
edge_options.add_argument("--no-sandbox")

user_data_dir = tempfile.mkdtemp()
edge_options.add_argument(f"--user-data-dir={user_data_dir}")

# Khởi tạo trình duyệt
try:
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)
except WebDriverException as e:
    print(f"Lỗi khi khởi tạo WebDriver: {e}")
    exit()

# Lặp qua từng URL và xử lý
for index, url in enumerate(urls, start=1):
    try:
        print(f"\nĐang xử lý URL {index}/{len(urls)}: {url}")
        
        # Truy cập URL và chụp màn hình
        driver.get(url)
        folder_name = re.sub(r'[^\w\-]', '_', url)
        folder_path = os.path.join("d:/IE105/image", folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Lưu ảnh chụp màn hình
        screenshot_path = os.path.join(folder_path, f"screenshot_{index}.png")
        driver.save_screenshot(screenshot_path)
        print(f"Đã lưu ảnh tại: {os.path.abspath(screenshot_path)}")

        # Phân tích hình ảnh bằng OCR
        try:
            # Mở và xử lý ảnh
            image = Image.open(screenshot_path)
            
            # Chuyển đổi ảnh sang grayscale để tăng độ chính xác
            image = image.convert('L')
            
            # Trích xuất văn bản
            extracted_text = pytesseract.image_to_string(image, lang='eng+vie')  # Hỗ trợ cả tiếng Anh và Việt
            
            # Lưu kết quả ra file txt
            text_file_path = os.path.join(folder_path, f"text_analysis_{index}.txt")
            with open(text_file_path, 'w', encoding='utf-8') as f:
                f.write(extracted_text)
            
            print(f"Đã phân tích và lưu văn bản tại: {text_file_path}")
            print("Nội dung trích xuất:", extracted_text[:200] + "...")  # Hiển thị preview

        except Exception as ocr_error:
            print(f"Lỗi OCR: {ocr_error}")

    except Exception as main_error:
        print(f"Lỗi chính: {main_error}")

# Đóng trình duyệt
driver.quit()

