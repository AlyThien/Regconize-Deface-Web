import os
import shutil

# Đường dẫn đến thư mục chứa các folder hình ảnh và file text
base_folder = "d:/IE105/image/not_defaced"
output_folder_defaced = "d:/IE105/image/defaced"
output_folder_not_defaced = "d:/IE105/image/not_defaced"
output_folder_not_found = "d:/IE105/image/not_found"

# Tạo thư mục đích nếu chưa tồn tại
os.makedirs(output_folder_defaced, exist_ok=True)
os.makedirs(output_folder_not_defaced, exist_ok=True)
os.makedirs(output_folder_not_found, exist_ok=True)

# Từ khóa để xác định "bị defaced"
keywords = ["defaced", "hacked", "error", "compromised", "h4cked", "h4ck3d", "def4ced", "def4c3d", "defaced by", "hacked by", "defaced website", "hacked website", "H 4 C K 3 D", "pwn3d", "Owned"]

# Lặp qua các folder con trong thư mục gốc
for folder_name in os.listdir(base_folder):
    folder_path = os.path.join(base_folder, folder_name)
    if os.path.isdir(folder_path):
        # Tìm file text phân tích trong folder
        text_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
        if not text_files:
            print(f"Không tìm thấy file text trong folder: {folder_name}")
            continue

        # Đọc nội dung file text đầu tiên
        text_file_path = os.path.join(folder_path, text_files[0])
        with open(text_file_path, 'r', encoding='utf-8') as f:
            content = f.read().lower()

        # Kiểm tra nếu file txt chứa "404" hoặc "not found"
        if "404" in content or "not found" in content or "isn't working" in content or "Insufficient" in content or "Forbidden" in content or "not available" in content or "not accessible" in content or "not reachable" in content or "403" in content:
            shutil.move(folder_path, os.path.join(output_folder_not_found, folder_name))
            print(f"Folder '{folder_name}' được phân loại là 'not found'.")
            continue

        # Kiểm tra nội dung có chứa từ khóa không
        if any(keyword in content for keyword in keywords):
            shutil.move(folder_path, os.path.join(output_folder_defaced, folder_name))
            print(f"Folder '{folder_name}' được phân loại là 'bị defaced'.")
        else:
            shutil.move(folder_path, os.path.join(output_folder_not_defaced, folder_name))
            print(f"Folder '{folder_name}' được phân loại là 'không bị defaced'.")