
let roomName;
let buttonID;


function redirectToPage(pageUrl) {
  window.location.href = pageUrl;
}

function changeClass(object, caseVar) {
    switch (caseVar) {
      case "Erdgeschoss":
        object.classList.add("groundFloor");
        break;
      case "1.OG":
        object.classList.add("firstFloor");
        break;
      case "Wohnzimmer":
        object.classList.add("livingRoom");
        break;
      case "Esszimmer":
        object.classList.add("diningRoom");
        break;
      case "Küche":
        object.classList.add("kitchen");
        break;
      case "Büro1":
        object.classList.add("office");
        break;
      case "Büro2":
        object.classList.add("office");
        break;
      case "Herrenzimmer":
        object.classList.add("business");
        break;
    }
  }

function goBack() {
    history.back();
}