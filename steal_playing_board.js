
// used to get string representation of a playing board from https://www.puzzle-binairo.com
// paste following code to explorer console and run it
// then save generated string into a file and use it as an input


dots = document.querySelector(".board-back").children
size = Math.floor(Math.sqrt(dots.length))

let i = 0

let result = ""

for (let d of dots) {
  if (i >= size * size) break;
  if (i++ % size === 0) result += "\n";
  if (d.classList.contains("cell-0")) {
    result += "O"
    continue
  }

  if (d.classList.contains("cell-1")) {
    result += "X"
    continue
  }

  result += "_"
}
console.log(result)