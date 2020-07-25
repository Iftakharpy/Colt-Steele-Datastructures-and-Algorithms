/*
# Problem Pattern: Divide and Conquer

Problem Statement
-----------------
Write a function that called search which accepts a sorted array and a number.
Function should return the index of the number.
If the number is not in the array it should return None/undefined

Examples:
1. search([1,2,3,4,5,6,7,8,9,10],5) #4
1. search([1,2,3,4,5,6,7,8,9,10],0) #None
1. search([1,2,3,4,5,6,7,8,9,10],10) #9
1. search([1,2,3,4,5,6,7,8,9,10],2) #1
*/

function mid_idx(low,high) {
    return Math.floor((low+high)/2);
}

function search(arr,num) {
    let min = 0;
    let max = arr.length-1;
    while (min<=max){
        let mid = mid_idx(min,max);
        if (num>arr[mid]){
            min = mid;
        }
        else if (num<arr[mid]){
            max = mid;
        }
        else{
            return mid;
        }
    }
    return NaN;
}