function changeString() {
    var sentence = document.getElementById("txtinput").value;
    var word = document.getElementById("strinput").value;
    let noNum = 0;
    let noAlp = 0;
    let noWhite = 0;
    document.getElementById("display").innerHTML = "Entered Text :" + sentence; //display entered text
    //number of alphabets, digits and whitespaces
    for (let i = 0; i < sentence.length; i++) {
        if (sentence[i].toLowerCase() >= "a" && sentence[i].toLowerCase() <= "z") noAlp++;
        else if (sentence[i] >= "0" & sentence[i] <= "9") noNum++;
        else if (sentence[i] == " ") noWhite++;
    }
    let text = "Number of Digits : " + noNum + "\nNumber of Alphabets : " + noAlp + "\nNumber of Whitespace : " + noWhite;
    document.getElementById("number").innerHTML = text; //display breakdown of text
    let count = sentence.split(word).length - 1;
    let pos = sentence.indexOf(word);
    let text2 = "Number of occurrences of the word " + word + " in teh text is " + count + "\nStarting position of search string : " + pos;
    document.getElementById("occurrences").innerHTML = text2; //Search string occurrences and position

}