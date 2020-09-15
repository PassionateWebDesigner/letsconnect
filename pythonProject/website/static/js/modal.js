var modal = document.getElementById('simplemodal');
var modalbtn =  document.getElementById('modalbtn');
var closebtn = document.getElementsByClassName('closeBtn')[0];

//listen for click
modalbtn.addEventListener('click',openModal);
        
//Listen for close click
closebtn.addEventListener('click',closeModal);
        
//Listen for outside click
window.addEventListener('click',clickOutside);

function openModal(){
    modal.style.display = 'block';
}
function closeModal(){
    modal.style.display='none';
}
function clickOutside(e){
    if(e.target == modal){
        modal.style.display='none';
    }
}
