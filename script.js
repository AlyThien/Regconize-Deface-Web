const dropArea = document.querySelector('.drag-area');
const dragText = dropArea.querySelector('header');
const button = dropArea.querySelector('button');
const input = document.querySelector('#fileInput');
const resultElement = document.querySelector('#result');

button.addEventListener('click', () => {
    input.click();
});

input.addEventListener('change', function () {
    const file = this.files[0];
    showFile(file);
});

dropArea.addEventListener('dragover', (event) => {
    event.preventDefault();
    dragText.textContent = "Release to Upload File";
});

dropArea.addEventListener('dragleave', (event) => {
    event.preventDefault();
    dragText.textContent = "Drag & Drop to Upload File";
});

dropArea.addEventListener('drop', (event) => {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    showFile(file);
});

async function showFile(file) {
    const fileType = file.type;
    const validExtensions = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp', 'image/avif'];
    
    if (!validExtensions.includes(fileType)) {
        alert('This is not a valid image file! Please use JPG, PNG, WebP, or AVIF.');
        dragText.textContent = "Drag & Drop to Upload File";
        return;
    }

    const fileReader = new FileReader();
    fileReader.onload = async () => {
        const fileURL = fileReader.result;
        const imgTag = `<img src="${fileURL}" alt="Uploaded Image" class="max-w-full max-h-64 object-contain">`;
        dropArea.innerHTML = imgTag + `<p id="result" class="mt-4 text-base font-medium"></p>`;
        
        resultElement.textContent = "Đang xử lý...";
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch('http://localhost:8000/predict', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            resultElement.textContent = `Ảnh ${data.filename}: ${data.result}`;
        } catch (error) {
            resultElement.textContent = `Lỗi: ${error.message}`;
            console.error('Error:', error);
        }
    };
    fileReader.readAsDataURL(file);
}