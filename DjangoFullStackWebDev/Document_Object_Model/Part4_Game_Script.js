var restart = document.querySelector("#b")

var squares = document.querySelectorAll('td')

function clearBoard(){
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent = ''
  }
}
restart.addEventListener('click', clearBoard)


// Create a function that will check the square marker
function changeMarker(){
    if(this.textContent === ''){
      this.textContent = 'X';
      // console.log(marker)
    }else if (this.textContent === 'X') {
      this.textContent = 'O';
    }else {
      this.textContent = '';
    }
};

// Use a for loop to add Event listeners to all the squares
for (var i = 0; i < squares.length; i++) {
    squares[i].addEventListener('click', changeMarker);
}


// var cel_11 = document.querySelector('#cel_11')
//
// cel_11.addEventListener("click", function() {
//   if (cel_11.innerHTML == '') {
//     cel_11.textContent = 'X'
//   }
//   else if (cel_11.innerHTML == 'X') {
//     cel_11.textContent = 'O'
//   }
//   else if (cel_11.innerHTML == 'O'){
//     cel_11.textContent = ''
//   }
//
// })
