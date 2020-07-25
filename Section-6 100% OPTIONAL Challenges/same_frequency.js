/*
# Problem Pattern: Freequency Counter

Problem Statement
-----------------
Write a function called same_frequency, which acepts two arrays.
Which should return True if the frequency of the elements in the arrays for every element is same.
Else this should return False.

Examples:
1. same_frequency([1,2,5,1,3],[1,2,1,5,3]) #True
2. same_frequency([1,2],[2,1]) #True
3. same_frequency([1,2,6,5],[5,1,2,6]) #True
4. same_frequency([1,2,5,1,3],[1,2,1,5,3,4]) #False
5. same_frequency([1,2,5,1,3],[1,2]) #False
*/




function sameFrequency(num1, num2){
  let strNum1 = num1.toString();
  let strNum2 = num2.toString();
  if(strNum1.length !== strNum2.length) return false;
  
  let countNum1 = {};
  let countNum2 = {};
  
  for(let i = 0; i < strNum1.length; i++){
    countNum1[strNum1[i]] = (countNum1[strNum1[i]] || 0) + 1
  }
  
  for(let j = 0; j < strNum1.length; j++){
    countNum2[strNum2[j]] = (countNum2[strNum2[j]] || 0) + 1
  }
  
  for(let key in countNum1){
    if(countNum1[key] !== countNum2[key]) return false;
  }

  return true;
}