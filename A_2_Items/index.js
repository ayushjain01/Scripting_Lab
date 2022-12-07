function calculate() {
    var price = document.getElementById("menu").value;
    var qty = document.getElementById("quantity").value;
    var ans = price * qty;
    document.getElementById("answer").innerHTML = "Total Payable Amount :" + ans;
}

function paid() {
    alert("Payment Done!")
}