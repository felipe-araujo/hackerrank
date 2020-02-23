handleDigitClick = event => {
    let res = document.getElementById('res');
    res.innerText = res.innerHTML + event.target.innerText;
}

clearDigits = event => {
    let res = document.getElementById('res');
    res.innerText = "";
};

performCalculation = event => {
    let res = document.getElementById('res');
    let expr = res.innerText;
    let f = null;
    let args = null;
    
    if(expr.indexOf('+') > 0){
        f = (x, y) =>  x+y;
        args = expr.split('+');
    }else if(expr.indexOf('-') > 0){
        f = (x, y) =>  x-y;
        args = expr.split('-');
    }else if(expr.indexOf('*') > 0){
        f = (x, y) =>  x*y;
        args = expr.split('*');
    }else if (expr.indexOf('/') > 0){
        f = (x, y) =>  Math.floor(x/y);
        args = expr.split('/');
    }

    args = args.map(n => parseInt(n, 2));
    ans = args.reduce(f, 0);
    res.innerText = ans.toString(2);
}


document.getElementById('btn0').onclick = handleDigitClick;
document.getElementById('btn1').onclick = handleDigitClick;
document.getElementById('btnSum').onclick = handleDigitClick;
document.getElementById('btnSub').onclick = handleDigitClick;
document.getElementById('btnMul').onclick = handleDigitClick;
document.getElementById('btnDiv').onclick = handleDigitClick;

document.getElementById('btnClr').onclick = clearDigits;

document.getElementById('btnEql').onclick = performCalculation;
