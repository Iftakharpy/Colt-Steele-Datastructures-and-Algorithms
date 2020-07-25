function is_alpha_numeric(character){
    if (48 <= character.charCodeAt(0) && character.charCodeAt(0) <= 57){
        return true;
    } else if (97 <= character.charCodeAt(0) && character.charCodeAt(0) <= 122){
        return true;
    } else {
        return false;
    }
}

// O(n)
function character_count(sentence){
    character_counts = {};  // dict or object to keep track of character numbers
    
    for (let character of sentence ){
        character = character.toLowerCase() // converting the number to lowercase

        if (is_alpha_numeric(character)){
            // if character exists in the dict or object then increment else initiate 1
            if (character_counts[character]){ 
                character_counts[character]+=1;
            } else{
                character_counts[character] = 1;
            }
        }
    }

    return character_counts
}

// demo
console.log(character_count("Hello world!"))