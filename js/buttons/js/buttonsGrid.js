function rotate(){
    idx = [2, 3, 6, 9, 8, 7, 4, 1];
    let prev = document.getElementById('btn1').innerText;
    let temp = '';
    for(let i in idx){
        let id = 'btn' + idx[i]
        console.log(id);
        temp = document.getElementById(id).innerText;
        document.getElementById(id).innerText = prev;
        prev = temp;
    }
}

document.getElementById('btn5').onclick = rotate;

