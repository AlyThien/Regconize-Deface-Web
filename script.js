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

function showFile(file){
    let fileType = file.type;
    let validExtensions = ['image/jpeg', 'image/jpg', 'image/png'];
    if (validExtensions.includes(fileType)){
        let fileReader = new FileReader();
        fileReader.onload = () => {
            let fileURL = fileReader.result;
            let imgTag = `<img src="${fileURL}" alt="">`;
            dropArea.innerHTML = imgTag;
        }
        fileReader.readAsDataURL(file);
    } else {
        alert('This is not an Image File!');
        dragText.textContent = "Drag & Release to Upload File";
    }
}