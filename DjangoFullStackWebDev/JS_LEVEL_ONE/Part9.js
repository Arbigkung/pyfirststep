var name = prompt("Enter name:")
var surname = prompt("Enter last name:")
var age = prompt("Enter age:")
var tall = prompt("Enter tall:")
var petName = prompt("Enter your pet name:")

if (name[0] === surname[0] && age > 20 && age < 30 && tall > 170 && petName.slice(-1) === 'y') {
  console.log("Welcome Spy")
}
else {
  alert("Hello normal guy")
}
