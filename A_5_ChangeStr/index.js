function changeString() {
    var temp = "";
    var ans = "";
    let asc = 0;
    const vowels = ["a", "e", "i", "o", "u"];
    var original = document.getElementById("strinput").value;
    original.toLowerCase()
        // replace every letter with the letter that follows in alphabetical order
    for (let i = 0; i < original.length; i++) {
        asc = original.charCodeAt(i) + 1;
        if (asc > "z".charCodeAt(0)) {
            asc = "a".charCodeAt(0)
        }
        temp = temp + String.fromCharCode(asc);

    }
    //capitalize vowels in new string
    for (let i = 0; i < temp.length; i++) {
        if (vowels.includes(temp[i])) {
            ans = ans + temp[i].toUpperCase();
        } else {
            ans = ans + temp[i];
        }
    }
    document.getElementById("answer").innerHTML = "Modified String :" + ans;
}