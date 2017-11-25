/// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!


///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop

// While Loop
var times = 5
while(times > 0){
  console.log("Hello while " + times)
  times = times - 1
}

// For Loop
for(i=0; i<5; i++){
  console.log("Hello For " + i)
}



/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// METHOD ONE
// While Loop
var num = 1;
while (num < 26) {
  if(num%2 === 1){
    console.log("while odd: " + num)
  }
  num++
}

// METHOD TWO
// For Loop
for(i=1; i<26; i++){
  if(i%2 !== 0){
    console.log("for odd: " + i)
  }
}
