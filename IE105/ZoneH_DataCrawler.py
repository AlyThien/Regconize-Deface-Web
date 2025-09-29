import requests
import re
import sys
import os
import platform
from colorama import Fore, Style, init

# Khởi tạo colorama cho màu sắc
init(autoreset=True)

# Xóa màn hình
os.system('cls' if platform.system() == 'Windows' else 'clear')

# Nhập cookies
zhe_cookie = input('\nEnter ZHE cookie: ').strip()
phpsessid_cookie = input('Enter PHPSESSID cookie: ').strip()

cookie = {
    "ZHE": zhe_cookie,
    "PHPSESSID": phpsessid_cookie
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"
}

def grab_by_notifier(notifier):
    for i in range(1, 51):
        url = f"http://www.zone-h.org/archive/notifier={notifier}/page={i}"
        res = requests.get(url, cookies=cookie, headers=headers)
        html = res.content

        print(f'\n📄 Đang lấy từ: {url}')

        if b'captcha' in html:
            print(Fore.YELLOW + "⚠️ CAPTCHA detected. Hãy xác minh thủ công trên trình duyệt.")
            sys.exit()

        if b'/mirror/id/' not in html:
            print(Fore.GREEN + "✅ Đã hoàn thành.")
            break

        # Lấy domain trong bảng
        matches = re.findall(b'<td>([^<\n]+)\n\s+</td>', html)
        with open(f"{notifier}.txt", 'a') as f:
            for m in matches:
                domain = m.split(b'/')[0].decode().strip()
                print(f"[+] {domain}")
                f.write(f"http://{domain}\n")

def grab_onhold_sites():
    for i in range(1, 51):
        url = f"http://www.zone-h.org/archive/published=0/page={i}"
        res = requests.get(url, cookies=cookie, headers=headers)
        html = res.content

        print(f'\n📄 Đang lấy từ: {url}')

        if b'captcha' in html:
            print(Fore.YELLOW + "⚠️ CAPTCHA detected. Hãy xác minh thủ công trên trình duyệt.")
            sys.exit()

        matches = re.findall(b'<td>([^<\n]+)\n\s+</td>', html)
        with open("onhold_zone.txt", 'a') as f:
            for m in matches:
                domain = m.split(b'/')[0].decode().strip()
                print(f"[+] {domain}")
                f.write(f"http://{domain}\n")

def main():
    print("\nChọn chế độ:")
    print("1 - Lấy site theo Notifier")
    print("2 - Lấy site OnHold (chưa được kiểm duyệt)")
    choice = input("Nhập lựa chọn (1-2): ").strip()

    if choice == "1":
        notifier = input("Nhập tên notifier: ").strip()
        grab_by_notifier(notifier)
    elif choice == "2":
        grab_onhold_sites()
    else:
        print("❌ Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
