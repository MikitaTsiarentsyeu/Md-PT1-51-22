function CheckData() {
  var data = new Array();
  data["name"] = document.getElementsByName("name")[0].value;
  data["surname"] = document.getElementsByName("surname")[0].value;
  data["lastname"] = document.getElementsByName("lastname")[0].value;
  data["date"] = document.getElementsByName("date")[0].value;
  data["pass"] = document.getElementsByName("pass")[0].value;
  data["card"] = document.getElementsByName("card")[0].value;
  data["r1"] = document.getElementsByName("r1")[0].value;
  data["r1"] = document.getElementsByName("r1")[0].value;
  data["r2"] = document.getElementsByName("r2")[0].value;
  
 
 if (data["name"]== "" ) {
  alert("нет имени");
  throw new FatalError("stop");
}
}


function fun1() {
  var rng=document.getElementById('r1'); 
  var p=document.getElementById('one'); 
  p.innerHTML= 'Сумма кредита: '+  rng.value + ' рублей' ;
  document.getElementById("one").style.fontSize = "16px";
  var p=document.getElementById('two'); 
  p.innerHTML='Сумма погашения кредита: '+ rng.value* 1.25 +' рублей';
  document.getElementById("two").style.fontSize = "16px";
}

function fun2() {
  var rng1=document.getElementById('r2'); 
  var p=document.getElementById('three'); 
  p.innerHTML= 'Срок кредита: '+ rng1.value ;
  document.getElementById("three").style.fontSize = "16px"; 
}

function fun3() {
  var p=document.getElementById('three');
  var a=document.getElementById('one');
  var b=document.getElementById('two');
  p.innerHTML = '';
  a.innerHTML = '';
  b.innerHTML = '';
  }
 
function fun4() {
  var p=document.getElementById('four'); 
  var a=document.getElementById('four_2'); 
  p.innerHTML= 'Расскажите, с какими проблемами вы столкнулись?';
  a.innerHTML= 'Чем подробнее вы их опишете, тем быстрее мы улучшим страницу. ';
  document.getElementById("four").style.fontSize = "18px";
  document.getElementById("four").style.fontWeight = "500";
  document.getElementById("four").style.marginTop= "14px";
  document.getElementById("four_2").style.fontSize = "18px";
  document.getElementById("four_2").style.fontWeight = "500";
  document.getElementById("four_2").style.marginTop= "-15px";
}
  function fun5() {

    var p=document.getElementById('four'); 
    var a=document.getElementById('four_2'); 
    p.innerHTML= 'Подскажите, как мы можем улучшить страницу?' ;
    a.innerHTML= 'На какой вопрос вы не нашли ответ?';
    document.getElementById("four").style.fontSize = "18px";
    document.getElementById("four").style.fontWeight = "500";
    document.getElementById("four").style.marginTop= "14px";
    document.getElementById("four_2").style.fontSize = "18px";
    document.getElementById("four_2").style.fontWeight = "500";
    document.getElementById("four_2").style.marginTop= "-15px";
    
  }
  function fun6() {
    document.getElementById("ask").remove();
    var pc = document.getElementById("pic_cntr");
    pc.innerHTML="<img src='thanks.png'>";
    pc.style.marginLeft = '360px';
  }

  function fun7() {
    document.getElementById("zzz").remove();
    var pc = document.getElementById("txt");
    pc.innerHTML="Ваш вопрос отправлен. Ожидайте ответ в ближайшее время!";
    pc.style.marginLeft = '240px';
    pc.style.marginTop = '16px';
    pc.style.color= 'red';
    pc.style.fontSize = '25px';
  }
  
  
  $(document).ready(function(){
    $('[data-toggle="popover_right"]').popover({
      placement : 'right'
    });
    $('[data-toggle="popover_left"]').popover({
        placement : 'left'
      });
  });
