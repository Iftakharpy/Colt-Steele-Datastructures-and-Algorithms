/*
Write a recursive function that takes a number.
This function should return factorial of the number.
If the number is negative this function should return None

Example:
1. factorial(1) #1
2. factorial(2) #2
3. factorial(3) #6
4. factorial(4) #24
5. factorial(0) #1
6. factorial(-1) #None
7. factorial(-100) #None
*/

//O(n)
function factorial(number){
    if (number<=-1){
        return NaN;
    }
    else if(number<=1){
        return 1
    }
    else{
        return number * factorial(number-1)
    }
}


console.log(-9)
console.log(0)
console.log(1)
console.log(2)
console.log(5)
console.log(6)