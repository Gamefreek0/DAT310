function initGrid() {
    // collect colors in an array
    var colors = [];
    var range = ["00", "33", "66", "99", "cc", "ff"];

    for (var r = 0; r < range.length; r++) {
        for (var g = 0; g < range.length; g++) {
            for (var b = 0; b < range.length; b++) {
                colors.push("#" + range[r] + range[g] + range[b]);
            }
        }
    }

    var colDiv = document.getElementById('colors');
    for (var i=0; i<colors.length;i++){
      colDiv.innerHTML = colDiv.innerHTML + "<div class='choice' style=background-color:" + colors[i] + " onclick='colorClick(this)'></div>\n";
    }
}

function colorClick(colDiv){
  var color = colDiv.style.backgroundColor;
  var selectedDiv = document.getElementById("selected");
  selectedDiv.style.backgroundColor = color;
  selectedDiv.innerHTML = color;
}

window.onload = function () {
    initGrid();
}
