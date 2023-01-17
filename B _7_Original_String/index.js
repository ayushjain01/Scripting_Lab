var MyLength = [];
var Original_String = [];
var count = 0;
var text = "Strings with length less than 3 are : ";

function update(arr1, arr2) {
    for (let i = count; i < arr2.length; i++)
        if (arr2[i] <= 3)
            text = text + arr1[i] + " ";
    document.getElementById("result2").innerHTML = text;
}

function add() {
    var x = document.getElementById("string").value;
    Original_String.push(x);
    MyLength[count] = Original_String[count].length;
    document.getElementById("result1").innerHTML = "Original String Array:" + Original_String;
    update(Original_String, MyLength);
    count++;
}