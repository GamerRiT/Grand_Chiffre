async function cod(){
    let place =document.getElementById('cod').value;

    let res= await eel.code(place)();

    document.getElementById('decode').innerHTML=res;
}
jQuery('#show').on('click',function(){
    cod();
});