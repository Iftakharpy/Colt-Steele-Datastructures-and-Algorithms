function swap(array,low,high){
    let temp = array[low];
    array[low] = array[high];
    array[high] = temp;
}


//O(n^2)
function selection_sort(array) {
    for (let i = 0; i < array.length; i++) {
        let index_of_min_value = i;
        for (let j = i+1; j < array.length; j++) {
            if (array[j]<array[index_of_min_value]){
                index_of_min_value = j;
            }
        }
        //swap
        swap(array,i,index_of_min_value);
    }
    return array;
}


console.log(selection_sort([3,2,1,8,9,0,5,6,2,4,7]))