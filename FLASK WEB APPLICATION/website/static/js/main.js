
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
      case "Kinderzimmer":
        object.classList.add("nursery");
        break;
      case "Schlafzimmer":
        object.classList.add("bedRoom");
        break;
    }
  }

function goBack() {
    history.back();
}