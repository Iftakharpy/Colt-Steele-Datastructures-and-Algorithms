//takes 2 sorted arrays and returns a sorted array by merging them together
//O(n+m)
function merge(array1,array2){
    let merged_array = [];
    
    let array1_index = 0;
    let array2_index = 0;
    while (array1_index<array1.length && array2_index<array2.length) {
        if (array1[array1_index]<array2[array2_index]){
            merged_array.push(array1[array1_index]);
            array1_index++;
        }
        else{
            merged_array.push(array2[array2_index]);
            array2_index++;
        }
    }

    while (array1_index<array1.length) {
        merged_array.push(array1[array1_index]);
        array1_index++;
    }
    while (array2_index<array2.length) {
        merged_array.push(array2[array2_index]);
        array2_index++;
    }

    return merged_array;
}


//time complexity is O(nlog(n)) because we are recursively calling the merge_sort function n times
//where time complexity of the left_slice or right_slice is O(log(n))
//O(nlog(n)) - time
//space complexity is n because we are splitting the list in n smaller arrays
//O(n) - space
function merge_sort(array){
    if (array.length<=1){
        return array;
    }
    
    let mid  = Math.floor(array.length/2);
    let left = merge_sort(array.slice(0,mid)); //O(log(n))
    let right = merge_sort(array.slice(mid,array.length)); //O(log(n))
    return merge(left,right); //O(n)
}

console.log(merge_sort([1,1,3,5,9,8,6,7,1,3,4]));