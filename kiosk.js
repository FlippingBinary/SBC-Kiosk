function navTo(pg) {
  // trigger unload animation
  document.body.setAttribute('class','unloading');
  // set window to navigate in 0.5 seconds
  setTimeout(function(){window.location.href = pg;}, 500);
}

document.onkeydown = function(event) {
  var key = event.keyCode;
  switch (key) {
    case 49:
      navTo('screen1.htm');
      break;
    case 50:
      navTo('screen2.htm');
      break;
    default:
        var msgbox = document.getElementById("msgbox");
        if ( msgbox ) {
          msgbox.innerHTML = "KeyCode: " + key;
        }

  }
}
