
const containers = Array.from(document.getElementsByClassName("col"));
const modalImg = document.getElementById("img01");
const modal = document.getElementById("myModal");
// tại sao chỉ khi thêm id riêng cho mỗi ảnh thì mới chạy được ???
containers.forEach(container => {
    container.onclick = (e) => {
        
        modal.style.display = "block";
        modalImg.src = e.target.src;
    };
});
  

const span = document.getElementsByClassName("close")[0];


span.onclick = (e) => { 
  modal.style.display = "none";
  
}

modal.onclick = (e) => {
    if(e.target == modalImg){
        return;
    }
    modal.style.display = 'none'
}