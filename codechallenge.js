let array = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

function divisibleBy3(checkarray) {
    for (i = 0; i < checkarray.length; i++) {
        if (checkarray[i] % 3 == 0) {
            console.log(checkarray[i])
        } 
    }
}

divisibleBy3(array)