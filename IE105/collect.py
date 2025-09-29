import os
import shutil

# Đường dẫn đến các thư mục phân loại
base_folder_defaced = "d:/IE105/image/defaced"
base_folder_not_defaced = "d:/IE105/image/not_defaced"
base_folder_not_found = "d:/IE105/image/not_found"

# Đường dẫn đến các thư mục đích
output_folder_defaced = "d:/IE105/image_defaced"
output_folder_not_defaced = "d:/IE105/image_not_defaced"
output_folder_not_found = "d:/IE105/image_not_found"

# Tạo thư mục đích nếu chưa tồn tại
os.makedirs(output_folder_defaced, exist_ok=True)
os.makedirs(output_folder_not_defaced, exist_ok=True)
os.makedirs(output_folder_not_found, exist_ok=True)

def collect_images(source_folder, destination_folder):
    """Sao chép tất cả hình ảnh từ các folder con vào folder đích."""
    for folder_name in os.listdir(source_folder):
        folder_path = os.path.join(source_folder, folder_name)
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    source_file = os.path.join(folder_path, file_name)
                    destination_file = os.path.join(destination_folder, file_name)
                    shutil.copy2(source_file, destination_file)
                    print(f"Đã sao chép: {source_file} -> {destination_file}")

# Thu thập hình ảnh từ các thư mục phân loại
collect_images(base_folder_defaced, output_folder_defaced)
collect_images(base_folder_not_defaced, output_folder_not_defaced)
collect_images(base_folder_not_found, output_folder_not_found)

print("Hoàn thành việc thu thập hình ảnh.")