import requests
from bs4 import BeautifulSoup
import csv
import os

# 📥 Đọc danh sách URL từ file
with open("urls.txt", "r") as file:
    urls = [line.strip() for line in file.readlines() if line.strip()]

# 📁 Tạo thư mục lưu HTML
os.makedirs("html_pages", exist_ok=True)

# 📄 Ghi file CSV với chỉ 2 cột: URL và HTML_File_Name
with open("defaced_data_clean.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["URL", "HTML_File_Name"])  # 👉 Chỉ 2 trường

    for url in urls:
        try:
            response = requests.get(url, timeout=10)

            # ✅ Tạo tên file HTML
            html_filename = url.replace("http://", "").replace("https://", "").replace("/", "_") + ".html"
            html_path = os.path.join("html_pages", html_filename)

            # ✅ Lưu nội dung HTML vào file
            with open(html_path, "w", encoding="utf-8") as html_file:
                html_file.write(response.text)

            # ✅ Ghi vào CSV
            writer.writerow([url, html_filename])
            print(f"✔ Đã xử lý: {url}")

        except Exception as e:
            print(f"❌ Lỗi với {url}: {e}")
