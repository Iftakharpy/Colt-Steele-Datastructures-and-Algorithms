/*
Write a recursive function that takes an array which contains number.
This function should return product of these numbers.

Example{
1. product([1,3,5]) // 15
2. product([1,3,5,0]) // 0
3. product([-1,3,5]) // -15
4. product([-1]) // -1
5. product([3]) // 3
6. product([]) // None
*/


function product(numbers){
    if (numbers.length==1){
        return numbers[0];
    }
    else if (!numbers.length){
        return NaN;
    }
    else{
        return numbers.pop()*product(numbers);
    }
}

//demo
console.log(product([1,3,5])) // 15
console.log(product([1,3,5,0])) // 0
console.log(product([-1,3,5])) // -15
console.log(product([-1])) // -1
console.log(product([3])) // 3
console.log(product([])) // None