/*
// Problem Pattern: Mulitple Pointers

Problem Statement
-----------------
Write a function called sum_zero which accepts a sorted array of integers.
The function should find the first pair where sum is 0.
Return an array/tuple that includes both vallues that sum to zero or None/undefined if a pair does not exist.

Examples:
1. sum_zero([1,2,3]) // None
2. sum_zero([-1,0,1,2,3]) // [-1,1]
3. sum_zero([-2,-1,0,1,2,3]) // [-2,2]
4. sum_zero([-4,1,2,3,4,5,6,7,8]) // [-4,4]
*/

//O(n)
function sum_zero(lst) {
    let left_pointer = 0;
    let right_pointer = lst.length-1;

    while (left_pointer!=right_pointer){
        let sum = lst[left_pointer]+lst[right_pointer];
        if (sum==0){
            return [lst[left_pointer],lst[right_pointer]]
        }
        else if (sum>0){
            right_pointer-=1;
        }
        else{
            left_pointer+=1;
        }
    }
    return NaN;
}


//O(n^2)
function naive_sum_zero(lst){
    for (let index = 0; index < array.length; index++) {
        for (let index_2 = index+1; index_2 < array.length; index_2++) {
            if (lst[index]+lst[index_2]==0){
                return [lst[index],lst[index_2]];
            }
        }
    }
    return None;
}