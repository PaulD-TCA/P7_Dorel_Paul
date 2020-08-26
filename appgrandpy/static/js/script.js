$(document).ready(function(){
    $("#myForm").submit(function(event){
        event.preventDefault();
        let form = $("#userInput").val();
        $.ajax({
            url: "/api/info/",
            type: "POST",
            contentType : "application/json; charset=UTF-8",
            dataType : "json",
            data: JSON.stringify(form),
            success: function(newAnswer) {
                createUserConversation(form);
                let grandPyAnswer = newAnswer[1];
                let adress = newAnswer[2][0];
                createGrandPyConversation(grandPyAnswer);
                countMap++;
                let mapNumber = "map"+ countMap
                let mapLat = newAnswer[2][1]["lat"];
                let mapLng = newAnswer[2][1]["lng"];
                let mapCoord = {"lat": mapLat, "lng": mapLng};
                createGrandPyMap(mapNumber);
                initMap(mapNumber, mapCoord);
            let contentHtml = '<div class="form-group mt-3">'+
              '<input id="userInput" type="text" name="userText" size="50" class="text-center" placeholder="Pose ta question ici à GrandPy."/>'+
              '<button class="btn btn-primary" type="submit" >Demander</button>'+
            '</div>';
            console.log(contentHtml)
            $("#myForm").html(contentHtml);
            }
        })
    })
})

let countMap = 0;

function createUserConversation(form){
  let conversation = document.getElementById("convDisplay");

  let newRowUser = document.createElement("div");
  newRowUser.classList.add("row");
  conversation.prepend(newRowUser);

  let newColUser = document.createElement("div");
  newColUser.classList.add("col-8", "offset-md-2", "alert", "alert-success");
  newRowUser.appendChild(newColUser);

  let newPUser = document.createElement("p");
  newPUser.classList.add("text");
  newColUser.appendChild(newPUser);
  newPUser.innerHTML = form;
};

function createGrandPyConversation(grandPyAnswer){
  let conversation = document.getElementById("convDisplay");

  let newRowGPy = document.createElement("div");
  newRowGPy.classList.add("row");
  conversation.prepend(newRowGPy);

  let newColGPy = document.createElement("div");
  newColGPy.classList.add("col-8", "alert", "alert-secondary");
  newRowGPy.appendChild(newColGPy);

  let newPGPy = document.createElement("p");
  newPGPy.classList.add("text");
  newColGPy.appendChild(newPGPy);
  newPGPy.innerHTML = grandPyAnswer;
};

function createGrandPyMap(mapNumber){
  let conversation = document.getElementById("convDisplay");

  let newRowMap = document.createElement("div");
  newRowMap.classList.add("row");
  conversation.prepend(newRowMap);

  let newColMap = document.createElement("div");
  newColMap.classList.add("col");
  newRowMap.appendChild(newColMap);
  newColMap.innerHTML = '<div id="'+mapNumber+'"></div><br>'
};

function initMap(mapNumber, mapCoord) {
  let map = new google.maps.Map(
      document.getElementById(mapNumber), {zoom: 12, center: mapCoord});
  let marker = new google.maps.Marker({position: mapCoord, map: map});
};
