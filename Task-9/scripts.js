var createtask=document.querySelectorAll('#createtask');
 
function displaycreatetaskpanel(event){
    var bctarget=event.target;
    var createtaskpanel=bctarget.parentNode.querySelector(".create-task-menu");
    createtaskpanel.classList.add("make-visible");
}
for(var i=0;i<createtask.length;i++){
    var anchor=createtask[i];
    anchor.addEventListener("click",displaycreatetaskpanel);  
        
}

var titleinput=document.querySelector("#title-input").value;
var descinput=document.querySelector("#desc-input").value;
var timeinput=document.querySelector("#time-input").value;
var dateinput=document.querySelector("#date-input").value;


document.querySelector("#add-task").onclick=function(){
    document.querySelector("#tasks").innerHTML=`
    <div class="taskonebyone">
    <div class ="titletask"> ${document.querySelector("#title-input").value}</div>
    <button id="more">More About this Task</button>
    <div class="noob">
    <span>${document.querySelector("#desc-input").value}
    ${document.querySelector("#time-input").value}
    ${document.querySelector("#date-input").value}
</span>
    </div>    `;
    
}

const targetdiv=document.querySelectorAll(".noob");
const btn=document.getElementById("more");
btn.onclick = function(){
    if(targetdiv.style.display=="none"){
        targetdiv.style.display="block";
    }
};