/*
Write a recursive function that takes 2 arguments NUM and POW.
This function should return NUM^POW.

Example:
1. power(5,1)  //5
2. power(5,2)  //25
3. power(1,16)  //1
4. power(5,0)  //1
5. power(5,-2)  //1/25
*/


function power(number,power) {
    if (power==0){
        return 1;
    }else if (power<0){
        return 1/number * power(number,power+1);
    }else{
        return number * power(number,power-1);
    }
}



console.log(power(5,1) ) //5
console.log(power(5,2) ) //25
console.log(power(1,16))  //1
console.log(power(5,0) ) //1
console.log(power(1,-996))  //1
console.log(power(2,-3)) //1/8