console.log("is log")
const sbutton = document.getElementById('sbutton');

const notstart = document.getElementsByClassName('notstart');
console.log(notstart)

Array.from(notstart).forEach(function(e)
{
    console.log(e)
    e.addEventListener('click',()=>{
        console.log("is lo00g")
        alert("Login to attempt the quiz");
    })
})

