const dropArea = document.querySelector('.drag-area');
const dragText = dropArea.querySelector('header');
const button = dropArea.querySelector('button');
const input = dropArea.querySelector('input');

button.addEventListener('click',() => {
    input.click();
})

input.addEventListener('change', ()=>{
    const file = this.files[0];
    showFile(file);
})

dropArea.addEventListener('dragover', (event) => {
    event.preventDefault();
    dragText.textContent = "Release to Upload File";
})

dropArea.addEventListener('dragleave', (event) => {
    event.preventDefault();
    dragText.textContent = "Drag & Release to Upload File";
})

dropArea.addEventListener('drop', (event) => {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    showFile(file);
})

function showFile(file){
    const fileType = file.type;
    const validExtensions = ['image/jpeg', 'image/jpg', 'image/png'];
    if (validExtensions.includes(fileType)){
        const fileReader = new FileReader();
        fileReader.onload = () => {
            const fileURL = fileReader.result;
            const imgTag = `<img src="${fileURL}" alt="">`;
            dropArea.innerHTML = imgTag;
        }
        fileReader.readAsDataURL(file);
    } else {
        alert('This is not an Image File!');
        dragText.textContent = "Drag & Release to Upload File";
    }
}