// const plus = document.querySelector(".plus");
// const minus = document.querySelector(".minus");
// const num = document.querySelector(".num");

//     let a = 1;

//     plus.addEventListener("click", ()=>{
//     a++;
//     a = (a < 10) ? "0" + a : a;
//     num.innerText = a;
//     });

//     minus.addEventListener("click", ()=>{
//     if(a > 1){
//         a--;
//         a = (a < 10) ? "0" + a : a;
//         num.innerText = a;
//     }
//     });
$('.quantity button').on('click', function () {
    var button = $(this);
    var oldValue = button.parent().parent().find('input').val();
    if (button.hasClass('btn-plus')) {
        var newVal = parseFloat(oldValue) + 1;
    } else {
        if (oldValue > 1) {
            var newVal = parseFloat(oldValue) - 1;
        } else {
            newVal = 1;
        }
    }
    button.parent().parent().find('input').val(newVal);
});