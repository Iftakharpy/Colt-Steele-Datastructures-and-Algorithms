function swap(array,low,high){
    let temp = array[low];
    array[low] = array[high];
    array[high] = temp;
}



function bubble_sort(array){
    for (i=array.length;0<=i;i--){
        let swapped = false;
        for (j=0;j<i;j++){
            if (array[j]>array[j+1]){
                swap(array,j,j+1);
                swapped = true;
            }
        }
        if (!swapped){
            break
        }
    }
    return array
}

//demo
console.log(bubble_sort([4,2,5,1,5,1,6,7,8,9,3,0,10]))