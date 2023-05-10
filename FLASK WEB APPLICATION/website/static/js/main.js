
let roomName;
let buttonID;


function redirectToPage(pageUrl) {
  window.location.href = pageUrl;
}

function changeClass(object, caseVar) {
    switch (caseVar) {
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