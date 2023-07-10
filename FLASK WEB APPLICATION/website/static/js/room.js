let isTouchDevice = 'ontouchstart' in window || navigator.maxTouchPoints > 0 || navigator.msMaxTouchPoints > 0;
let blind_id;
let plan = document.getElementById("timeplan");
let tableRows = document.getElementById("timeTable");
let tableFrame = document.getElementById("tableFrame");
let addButton = document.getElementById("addButton");

let modulesActions = [];
let allDriveButtons = document.querySelectorAll("controlButton");

let newTime = "06:00";
let newAction = "0";

function saveBlind_id(id) {
  blind_id = id;
}

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


function driveButton(id) {
  let portActionSplit = id.split("/");
  let port = portButtonSplit[1];
  let action = portButtonSplit[0];
  saveDriveButtonStates(port, action);
}

function saveDriveButtonStates(port, state) {
  $.ajax({
    url: "/updateButtonStates/" + port,
    type: 'POST',
    data: {'state': state},
    success: function (response) {
      console.log(response);
    },
    error: function (error) {
      console.log(error);
    }
  });
}

function redrawDriveButtons() {
  console.log("Redrawing drive buttons now.")
}

function switchButtonClass(id) {
  button = document.getElementById(id);
  if (button.classList.contains("automaticButtonTrue")) {
    button.classList.remove("automaticButtonTrue");
    button.classList.add("automaticButtonFalse");
  } else {
    button.classList.remove("automaticButtonFalse");
    button.classList.add("automaticButtonTrue");
  }
}

function switchLightState(id, port) {
  let lightBulb = document.getElementById(id);
  let button = document.getElementById("lightButton/"+id);
  if (lightBulb.classList.contains("lightBulbOn")) {
    lightBulb.classList.remove("lightBulbOn");
    button.innerHTML = `ON`;
    lightOn(port);
  } else {
    lightBulb.classList.add("lightBulbOn");
    button.innerHTML = `OFF`;
    lightOff(port);
  }
  
}

function lightOn(port) {
  $.ajax({
    url: "/turnLightOn/" + port,
    type: 'POST',
    success: function (response) {
      console.log(response);
    },
    error: function (error) {
      console.log(error);
    }
  });
}

function lightOff(port) {
  $.ajax({
    url: "/turnLightOff/" + port,
    type: 'POST',
    success: function (response) {
      console.log(response);
    },
    error: function (error) {
      console.log(error);
    }
  });
}

function longPress(button) {
  let opposite = getOpposite(button);
  button.classList.remove("buttonLocked");
}

function releaseButton(button) {
  button.classList.add("controlButton");  
}

function shortPress(button) {
  let opposite = getOpposite(button);
  unlockEachDriveButtonIfThe_ALLinterface_IsUsed(button);
  opposite.classList.remove("buttonLocked");
  if (button.classList.contains("buttonLocked")) {
    button.classList.remove("buttonLocked");
    button.value = "0";
  } else {
    button.classList.add("buttonLocked");
    button.value = "1";
  }
  
}

function getOpposite(button) {
  let action = button.id.split("/")[0];
  let port = button.id.split("/")[1];
  let opposite = document.getElementById("driveDown/"+port);
  if (action == "driveDown") {
    opposite = document.getElementById("driveUp/"+port);
  }
  return opposite;
}

function unlockEachDriveButtonIfThe_ALLinterface_IsUsed(button) {
  let port = button.id.split("/")[1];
  if (port == "00") {
    let buttons = document.querySelectorAll(".buttonLocked");
    for (let i = 0; i < buttons.length; i++) {
      if (buttons[i] != button) {
        buttons[i].classList.remove("buttonLocked");
        buttons[i].value = "0";
      }
    }
  } else {
      try {
        allUp.classList.remove("buttonLocked");
        allDown.classList.remove("buttonLocked");
      }
      catch {}
      finally {
        allUp.value = "0";
        allDown.value = "1";
      }
  }
}

function updateCurrentActions(buttons) {
  $.ajax({
    url: "/updateCurrentActions/",
    type: 'POST',
    data: {'buttons': buttons},
    success: function (response) {
      console.log(response);
    },
    error: function (error) {
      console.log(error);
    }
  });
}

function setEventListener(button) {

  if (isTouchDevice) {
    setTouchListener(button);
  } else {
    setClickListener(button);
  }

}

function setClickListener(button) {
  button.addEventListener("mousedown", function () {

    let long = false;

    pressTimer = setTimeout(function () {
      // long press
      longPress(button);
      long = true;
    }, 500);

    // short press
    shortPress(button);
    updateCurrentActions(allDriveButtons);
  });

  button.addEventListener("mouseup", function () {
    clearTimeout(pressTimer);
    if (long) {
      button.value = "0";
      updateCurrentActions(allDriveButtons);
    }
    
  });
}

function setTouchListener(button) {
  button.addEventListener("touchstart",  function () {

    pressTimer = setTimeout(function () {
      // long press
      longPress(button);
    }, 500);

    // short press
    shortPress(button);
    updateCurrentActions(allDriveButtons);
  });

  button.addEventListener("touchend", function () {
    clearTimeout(pressTimer);
  });
}

function clearEventListener(id) {
  button = document.getElementById(id);
  button.removeEventListener("touchstart", function () { });
  button.removeEventListener("touchend", function () { });
}


function rebuildTableHeader(tag) {
  tag.innerHTML = `
    <tr>
      <th>Uhrzeit</th>
      <th>Aktion</th>
      <th class="lastColumn">Entf</th>
    </tr>
  `;
}


function getTimeEntries(blind_id) {
  return new Promise((resolve, reject) => {
    $.ajax({
      url: "/getTimeEntries/" + blind_id,
      type: 'GET',
      success: function (response) {
        let actionTimes = response.data;
        resolve(actionTimes);
      },
      error: function (error) {
        reject(error);
      }
    });
  });
}

function displayEntries(entries) {
  let time;
  let state;
  let action_id;
  entries.forEach(entry => {
    time = entry['time_value'];
    state = entry['closedInPercent'];
    action_id = entry['id'];
    tableRows.innerHTML += `
      <tr>
        <td>${time}</td>
        <td>${state}</td>
        <td><button onclick="deleteAction(${action_id})" id="${action_id}" class="deleteButton">X</button></td>
      </tr>
    `;
  });
  
  // Show plan
  plan.style.display = "flex";
}

function addAction() {
  drawInputRow();
  changeAddButton();
}

function drawInputRow() {
  tableRows.innerHTML += `
  <tr>
    <td id="timeColumn"><div class="newTimeCont"><div class="timeCont">${newTime}</div><div><button onclick="justifyTime(0)" class="timeChooseButton">&#60;</button><button onclick="justifyTime(1)" class="timeChooseButton">&#62;</button></div></div></td>
    <td id="actionColumn"><div class="newTimeCont">${newAction}<div><button onclick="justifyAction(0)" class="timeChooseButton">&#60;</button><button onclick="justifyAction(1)" class="timeChooseButton">&#62;</button></div></div></td>
    <td><button onclick="interrupt()" class="deleteButton">X</button></td>
  </tr>
  `;
  tableFrame.scrollTop = tableFrame.scrollHeight;
}

function changeAddButton() {
  addButton.innerHTML = `Hinzufügen`;
  addButton.onclick = null;
  addButton.removeEventListener("click", addAction);
  addButton.addEventListener("click", saveNewAction);
}

function justifyTime(direction) {
  setTime(direction);
  let timeColumn = document.getElementById("timeColumn");
  timeColumn.innerHTML = `
    <div class="newTimeCont"><div class="timeCont">${newTime}</div><div><button onclick="justifyTime(0)" class="timeChooseButton">&#60;</button><button onclick="justifyTime(1)" class="timeChooseButton">&#62;</button></div></div>
  `;
}

function justifyAction(direction) {
  setAction(direction);
  let actionColumn = document.getElementById("actionColumn");
  actionColumn.innerHTML = `
    <div class="newTimeCont">${newAction}<div><button onclick="justifyAction(0)" class="timeChooseButton">&#60;</button><button onclick="justifyAction(1)" class="timeChooseButton">&#62;</button></div></div>
  `;
}

function setTime(direction) {
  let timePart = newTime.split(":");
  let hours = parseInt(timePart[0]);
  let minutes = parseInt(timePart[1]);
  let allMinutes = hours * 60 + minutes;

  if (direction) {
    allMinutes += 30;
  } else {
    allMinutes -= 30;
  }
  if (allMinutes >= 24 * 60) {
  allMinutes -= 24 * 60;
  } else if (allMinutes < 0) {
    allMinutes += 24 * 60;
  }

  let expandHours = Math.floor(allMinutes / 60);
  let expandMinutes = allMinutes % 60;
  let expandHoursString = expandHours.toString().padStart(2, "0");
  let expandMinutesString = expandMinutes.toString().padStart(2, "0");
  // Rückgabe der erweiterten Zeit im Format "hh:mm"
  newTime = expandHoursString + ":" + expandMinutesString;
}

function setAction(direction) {
  if (direction && parseInt(newAction) < 100) {
    newAction = String(parseInt(newAction)+10);
  } else if (!direction && parseInt(newAction) > 0) {
    newAction = String(parseInt(newAction)-10);
  }
}

function interrupt() {
  redrawTimeplan(blind_id);
}

function resetAddButton() {
  // addButton.removeEventListener("click", saveNewAction);
  addButton.innerHTML = `Neu`;
  addButton.addEventListener("click", addAction);
}

function saveNewAction() {
  $.ajax({
    url: "/saveNewAction/" + blind_id,
    type: 'POST',
    data: {'time':newTime, 'action':newAction},
    success: function (response) {
      console.log(response);
      redrawTimeplan(blind_id);
    },
    error: function (error) {
      console.log(error);
    }
  });
}

function deleteAction(action_id) {
  $.ajax({
    url: "/deleteAction/" + action_id,
    type: 'POST',
    success: function (response) {
      console.log(response);
      redrawTimeplan(blind_id)
    },
    error: function (error) {
      console.log(error);
    }
  });
}

function closePlan() {
  plan.style.display="none";
}

function automatic(port) {
  $.ajax({
      url: "/switchAutomatic/" + port,
      type: 'POST',
      success: function (response) {
          console.log(response);
      },
      error: function(error) {
        console.error(error);
      }
  })
}

function envAutomatic(moduleType, enviroment, env_id) {
  console.log(env_id);
  $.ajax({
      url: "/switchEnvAutomatic/" + env_id,
      type: 'POST',
      data: {'moduleType':moduleType, 'enviroment':enviroment},
      success: function (response) {
          console.log(response);
      },
      error: function(error) {
        console.error(error);
      }
  })
}