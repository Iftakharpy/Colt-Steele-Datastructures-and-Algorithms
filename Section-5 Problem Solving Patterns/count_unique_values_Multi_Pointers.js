/*
// Problem Pattern: Multi Pointers

Problem Statement
-----------------
Write a fuction which accepts a sorted array. And counts number of unique values in a given sorted array.

Examples:
1. count_unique_values([-1,0,1,2,3,4]) //6
2. count_unique_values([]) //0
2. count_unique_values([1,1,1,2]) //2
*/



// O(n)
// Using extra memory/space
function cont_unique_values(lst) {
    let unique_values = 0;
    lookup = {};
    for (let item of lst){  //O(n)
        if (lookup.hasOwnProperty(item)){
            continue;
        }else{
            unique_values+=1
            lookup[item]=true
        }
    }
    return unique_values
}



//O(n)
// Without using any extra memory/space
function count_unique_values(lst) {
    if (!lst){
        return 0;
    }
    let count=1;
    i=0;
    for (j=1;j<lst.lenght;j++){
        if (lst[i]!=lst[j]){
            count+=1;
            i=j;
        }
    }
    return count;
}