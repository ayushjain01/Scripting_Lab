var total = 0;

function addCake() {
    total += 50
    document.getElementById("total").innerHTML = "Total Payable Amount :" + total;
}

function addBread() {
    total += 35
    document.getElementById("total").innerHTML = "Total Payable Amount :" + total;
}

function addCookies() {
    total += 100
    document.getElementById("total").innerHTML = "Total Payable Amount :" + total;
}

function addBun() {
    total += 15
    document.getElementById("total").innerHTML = "Total Payable Amount :" + total;
}

function addChips() {
    total += 10
    document.getElementById("total").innerHTML = "Total Payable Amount :" + total;
}

function removeAll() {
    total = 0
    document.getElementById("total").innerHTML = "Total Payable Amount :" + total;
}


function checkout() {
    alert("Total Amount to be paid : " + total + "\nThank you!")
}