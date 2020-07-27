/*
Write a function that accepts a sorted array and a vlaue.
If the value is in the array then return the index of the value.
Else return -1.
*/


function mid(low,high) {
    return Math.floor((low+high)/2);
}


//works only on sorted arrays
//O(logN)
function binary_search(array,value) {
    let low = 0;
    let high = array.length-1;
    let middle = mid(low,high);

    while (low!=high){
        if (value>array[middle]){
            low = middle+1;
        }
        else if (value<array[middle]){
            high = middle-1;
        }
        else{
            break;
        }
        middle = mid(low,high);
    }

    if (array[middle]===value){
        return middle;
    }
    return -1;
}





//demo
console.log(binary_search([1,2,3,4],10))
console.log(binary_search([1,2,3,4],2))
console.log(binary_search([1,2,3,4],3))
console.log(binary_search([1,2,3,4],4))
console.log(binary_search([1,2,3,4],1))

