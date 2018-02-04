
var CELL_SIZE = 40;

function Labyrinth() {
    this.map = [
        [0, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0]];
}

function printConsole(){
  for (var y = 0; y< this.map.length;y++){
    var str = "";
    for (var x = 0; x<this.map[y].length;x++){
      str+=(this.map[y][x]==1) ? "*" : " ";
    }
    console.log(str);
  }
}

function printDisplay(id){
  var mapDiv = document.getElementById(id);
  mapDiv.style.width = CELL_SIZE * this.map[0].length + "px";
  mapDiv.style.height = CELL_SIZE* this.map.length + "px";
  mapDiv.style.border = "1px solid black";
  mapDiv.style.position = "absolute";
  mapDiv.style.overflow = "true";
  for (var y = 0; y< this.map.length;y++){
    for (var x = 0; x<this.map[y].length;x++){
      addCell(mapDiv, x, y);
    }
  }
}

function addCell(map, x, y){
  var cell = document.createElement("div");
  cell.style.position= "absolute";

  cell.style.left=CELL_SIZE *x+ "px";
  cell.style.top= CELL_SIZE *y+ "px";
  cell.style.height=CELL_SIZE + "px";
  cell.style.width=CELL_SIZE + "px";
  cell.style.backgroundColor = (this.map[y][x]==1) ? "gray" : "white";
  map.appendChild(cell);
}
