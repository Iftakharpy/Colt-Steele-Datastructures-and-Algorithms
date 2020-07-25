/*
Write a recursive function that takes a number.
This function should return N-th number of the fibonacci series.
If the number is negative this function should return None.

Example:
1. fibonacci(-1) # None
2. fibonacci(0) # 1
3. fibonacci(1) # 1
4. fibonacci(2) # 2
5. fibonacci(3) # 3
6. fibonacci(4) # 5
7. fibonacci(5) # 8
*/

// I don't know the time complexity of these functions


//without memoization
function fibonacci(number) {
    if (number<=-1) {
        return NaN;
    }
    else if(number<=1){
        return 1;
    }else{
        return fibonacci(number-2)+fibonacci(number-1);
    }
}


//with memoization
function memo_fibonacci(number,memo={}) {
    if (number<=-1){
        return NaN;
    }else if(number<=1){
        return 1;
    }else{
        if (memo.number){
            return memo.number;
        }else{
            memo.number = memo_fibonacci(number-2,memo)+memo_fibonacci(number-1,memo);
        }
    }
    return memo_fibonacci(number-2,memo)+memo_fibonacci(number-1,memo);
}


//test
range = 90;
for (let number = -5; number < range; number++) {
    console.log(memo_fibonacci(number));
}