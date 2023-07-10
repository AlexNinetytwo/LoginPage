let seconds = 0;
let timer = setInterval(updateTimer, 1000);
let screenSaver = document.getElementById("screenSaver");
let screenSaverBox = document.getElementById("screenSaverBox");


function redrawTimeplan(id) {
  saveBlind_id(id);
  resetAddButton();
  rebuildTableHeader(tableRows);
  getTimeEntries(id)
    .then(displayEntries)
    .catch(error => {
      console.log(error);
    });
}


function resetAddButton() {
  addButton.removeEventListener("click", saveNewAction);
  addButton.innerHTML = `Neu`;
  addButton.addEventListener("click", addAction);
}



function getCurrentTime() {
  // let currentTime = new 
}

function updateTimer() {
  seconds++;
  if (seconds > 60) {
    showScreenSaver()
    seconds = 0;
  }
}

function resetTimer() {
  clearInterval(timer);
  screenSaver.style.display = "none";
  timer = setInterval(updateTimer, 1000);
}

function showScreenSaver() {
  clearInterval(timer);
  screenSaver.style.display = "flex";
  timer = setInterval(moveScreenSaver, 2000);
}

let directionX = 10
let directionY = 10
let bodyWidth = document.getElementById("body").getBoundingClientRect().width;
let bodyHeight = document.getElementById("body").getBoundingClientRect().height;


function moveScreenSaver() {
  let xPos = screenSaverBox.offsetLeft;
  let yPos = screenSaverBox.offsetTop;
  let screenSaverWidth = screenSaverBox.getBoundingClientRect().width;
  let screenSaverHeight = screenSaverBox.getBoundingClientRect().height;
  screenSaverBox.style.left = String(xPos + directionX) + "px";
  screenSaverBox.style.top = String(yPos + directionY) + "px";
  if (xPos < 0)  {
    directionX = 10
  } else if (xPos+screenSaverWidth > bodyWidth) {
    directionX = -10
  }
  if (yPos < 0)  {
    directionY = 10
  } else if (yPos+screenSaverHeight > bodyHeight-screenSaverHeight) {
    directionY = -10
  }
  
}