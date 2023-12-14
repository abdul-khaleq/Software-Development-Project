var numbers = [1, 5, 9, 12, 4, 20, 19, 3, 22]

console.log(numbers.sort(function(a,b){
    return a-b
}))

console.log(numbers.sort((a,b) => a-b
))