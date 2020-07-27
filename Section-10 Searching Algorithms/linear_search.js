/*
Write a function that accepts an array and a vlaue.
If the value is in the array then return the index of the value.
Else return -1.
*/

//O(n)
function linear_search(array,vlaue){
    for(let index=0;index<array.length;index++){
        if (array[index]===vlaue){
            return index
        }
    }
    return -1
}


//demo
console.log(linear_search([1,2,3],3))
console.log(linear_search([1,2,3],4))