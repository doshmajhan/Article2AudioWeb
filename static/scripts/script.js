var imageID=0;
function changeImage(every_seconds){
    //change the image
    if(imageID==0){
        document.body.style.backgroundImage = "url('static/mountain1.jpg')";
        imageID++;
    }
    else{if(imageID==1){
        document.body.style.backgroundImage = "url('static/mountainv2.jpg')";
        imageID++;
    }
    else{if(imageID==2){
        document.body.style.backgroundImage = "url('static/mountain3.jpg')";
        imageID++;
    }
    else{if(imageID==3){
        document.body.style.backgroundImage = "url('static/mountain4.jpg')";
        imageID=0;
    }}}}
    //call same function again for x of seconds
    setTimeout("changeImage("+every_seconds+")",((every_seconds)*1000));
}