/*
Write a function that accepts 2 strings.
Long string and a short string.
If the short string is in the long string then return 
the starting index of the short string in the long string.
Else return -1.
*/


function naive_string_search(long,short) {
    if (long===short){
        return 0;
    }
    if (long.length<short.length){
        return -1;
    }

    for (let i = 0; i <= long.length-short.length; i++) {
        for (let j = 0; j < short.length; j++) {
            if (long[i+j]!=short[j]){
                break
            }
            if (j==short.length-1){
                return i
            }
        }
    }

    return -1
}


//demo
console.log(naive_string_search('hello world','ld'))