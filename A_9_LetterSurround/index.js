function changeString() {
    var ans = true;
    var original = document.getElementById("strinput").value;
    // check starting and ending characters 
    if (original[0] != "+" || original[original.length - 1] != "+") {
        ans = false;
    }
    // split and check if any element's length is == 1 (every letter must be surrounded by a "+")
    // eg - Input = +a+s+d+f+g+h+j+ -> split = ["","a","s","d","f","g","h","j",""], each element's(ignore first and last) length == 1, String accepted
    // eg - Input = +a+s+d+f+g+h+jk+ -> split = ["","a","s","d","f","g","h","jk",""], last element's (ignore first and last) length > 1, string rejected
    else {
        original = original.slice(1, original.length - 1); //first and last elements in the array are "" since "+".split("+") = ["",""]
        let temp = original.split("+");
        for (let i = 0; i < temp.length; i++) {
            if (temp[i].length != 1) {
                ans = false;
                break;
            }
        }
    }
    document.getElementById("answer").innerHTML = "Result :" + ans;
}