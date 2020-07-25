/*
// Problem Pattern: Sliding Window

Problem Statement
-----------------
Write a fuction that accepts a list and a number N.
The function should return the maximum sum of N consecutive numbers in the array.

Examples:
1. max_subarray_sum([1], 2) //None
2. max_subarray_sum([1, 3, 4, 2, 12, 3], 1) //12
3. max_subarray_sum([2, 3, 4, 5, 12, 4], 2) //17
4. max_subarray_sum([9, 2, 3, 1, 2, 10], 2) //12
*/


//O(n^2)
function naive_max_subarray_sum(lst, N){
    if (lst.length<N){
        return NaN
    }

    let max_sum = 0;
    for (let index = 0; index < array.length-N; index++) {
        let temp_sum = 0;
        for (let j = index; j < index+N; j++) {
            temp_sum+=lst[index];
        }
        if (temp_sum>max_sum){
            max_sum=temp_sum;
        }
    }
    return max_sum;
}


//O(n)
function max_subarray_sum(lst,N) {
    if (lst.length<N){
        return NaN;
    }

    max_sum=0
    for (let index = 0; index < lst.length; index++) {
        max_sum += lst[index];
    }

    temp_sum=max_sum;
    for (let index = N; index < array.length; index++) {
        temp_sum = (temp_sum-lst[i-N]) + lst[index];
        max_sum = Math.max(temp_sum,max_sum);
    }
    return max_sum
}