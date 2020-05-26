let html = `<div class="row my-3">`;
for(let i=1;i<27;i++){
    if(i==16 || i==17 || i==25){
    html += `<div class="col-sm-8 col-md-3 my-4 mx-auto"><a href="/img/${i}.png"target="_blank"><img src="img/${i}.png" style="height:200px;" class="img-thumbnail"></a></div>`;
    }
    else{
    html += `<div class="col-sm-8 col-md-3 my-4 mx-auto"><a href="/img/${i}.jpg"target="_blank"><img src="img/${i}.jpg" style="height:200px;" class="img-thumbnail"></a></div>`;
    }
    if(i%3==0 && i!=26){
        html+= `</div><div class="row my-3">`;
    }
    if(i==26){
        html+= `</div>`;
    }
}
html += `</div>`;
document.getElementById('imageset').innerHTML = html;