/*
# Problem Pattern: Freequency Counter/Multi Pointer

Problem Statement
-----------------
Write a function called are_there_duplicates, which acepts an array.
Which should return True if all elements are unique.
Else this should return False.

Examples:
1. are_there_duplicates([1,2,5,3]) #True
2. are_there_duplicates([1,2]) #True
3. are_there_duplicates([1,2,6,5]) #True
4. are_there_duplicates([0,0]) #False
5. are_there_duplicates([1,2,3,1]) #False
*/




//are_there_duplicates Solution (Frequency Counter)
function are_there_duplicates(arguments) {
  let collection = {}
  for(let val in arguments){
    collection[arguments[val]] = (collection[arguments[val]] || 0) + 1
  }
  for(let key in collection){
    if(collection[key] > 1) return true
  }
  return false;
}


//are_there_duplicates Solution (Multiple Pointers)
function are_there_duplicates(arguments) {
  // Two pointers
  args.sort((a,b) => a > b);
  let start = 0;
  let next = 1;
  while(next < args.length){
    if(args[start] === args[next]){
        return true
    }
    start++
    next++
  }
  return false
}


//are_there_duplicates One Liner Solution
function are_there_duplicates(arguments) {
  return new Set(arguments).size !== arguments.length;
}