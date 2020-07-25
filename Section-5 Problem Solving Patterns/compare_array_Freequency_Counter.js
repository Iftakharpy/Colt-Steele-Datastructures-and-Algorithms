/*
// Problem Pattern: Freequency Counter

Problem Statement
-----------------
Write a function called naive_Same, which acepts two arrays.
And returns if every value in the first array has it's corresponding value squared in the second array.
The frequency of values must be the same.

Examples:
1. naive_Same([1,2,3], [1,4,9]) //true
2. naive_Same([2,1,3], [9,4,1]) //true
3. naive_Same([2,3], [1,4,9]) //false
4. naive_Same([1,2,4], [1,4,9]) //false
5. naive_Same([1,2,1], [4,4,1]) //false
*/


//O(n^3)
function naive_Same(list1, list2){
    if (list1.length!=list2.length){
        return false;
    }

    for (let num of list1){ //O(n)
        num=num**2
        if (list2.includes(num)){ //O(n)
            let index = list2.indexOf(num);
            list2.splice(index,1); //O(n)
        }
        else{
            return false;
        }
    }
    return true;
}

//O(n+m) -> O(n)
function fairly_good_Same(list1, list2){
    if (list1.length!=list2.length){
        return false;
    }

    lookup_table = {}
    for (const item of list2){ //O(n)
        if (lookup_table.item){ //O(1)
            lookup_table[item]+=1
        } 
        else{
            lookup_table[item]=1
        }
    }

    for (let num of list1){ //O(m)
        num = num**2
        if (lookup_table[num]){ //O(1)
            lookup_table[num]-=1
        }
        else{
            return false
        }
    }
    return true
}



console.log(naive_Same([1,2,3], [1,4,9])) //true
console.log(naive_Same([2,1,3], [9,4,1])) //true
console.log(naive_Same([1,2,4], [1,4,9])) //false
console.log(naive_Same([1,2,1], [4,4,1])) //false
console.log(naive_Same([2,3], [1,4,9])) //false