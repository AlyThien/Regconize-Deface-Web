import os
import csv

# Từ khóa nhận biết deface
defaced_keywords = [
    "hacked by", "defaced by", "owned by", "0wn3d", 
    "security breached", "greetz to", "greetings to"
]

# Thư mục đầu vào chứa file TEXT (HTML thô)
input_folder = "C:/Users/tulym/IE105/html_pages"

# Thư mục xuất kết quả
defaced_folder = "C:/Users/tulym/IE105/filtered/defaced"
not_defaced_folder = "C:/Users/tulym/IE105/filtered/not_defaced"
os.makedirs(defaced_folder, exist_ok=True)
os.makedirs(not_defaced_folder, exist_ok=True)

# File CSV ghi nhãn
csv_output = "C:/Users/tulym/IE105/deface_labels.csv"

# Hàm kiểm tra HTML có bị deface hay không
def is_defaced(content):
    content_lower = content.lower()
    return any(keyword in content_lower for keyword in defaced_keywords)

# Kiểm tra thư mục đầu vào
if not os.path.exists(input_folder):
    raise FileNotFoundError(f"Thư mục '{input_folder}' không tồn tại. Vui lòng tạo thư mục và thêm file.")

# Kiểm tra nội dung thư mục
files = os.listdir(input_folder)
target_files = [f for f in files if f.endswith((".html", ".text"))]
if not target_files:
    print(f"❌ Không tìm thấy file .html, hoặc .text trong '{input_folder}'. Nội dung thư mục: {files}")
    exit()

# Mở CSV để ghi nhãn
with open(csv_output, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["filename", "label"])  # Header

    file_count = 0
    # Lặp qua từng file .html, .txt, .text
    for filename in target_files:
        filepath = os.path.join(input_folder, filename)

        try:
            # Đọc nội dung file
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Kiểm tra defaced
            if is_defaced(content):
                label = "defaced"
                out_path = os.path.join(defaced_folder, filename)
            else:
                label = "not_defaced"
                out_path = os.path.join(not_defaced_folder, filename)

            # Ghi ra thư mục
            with open(out_path, 'w', encoding='utf-8') as f_out:
                f_out.write(content)

            # Ghi nhãn vào CSV
            writer.writerow([filename, label])
            file_count += 1
            print(f"Đã xử lý: {filename} -> {label}")

        except Exception as e:
            print(f"❌ Lỗi khi xử lý file: {filename} -> {e}")

print(f"Hoàn tất phân loại {file_count} file. File CSV: {csv_output}")