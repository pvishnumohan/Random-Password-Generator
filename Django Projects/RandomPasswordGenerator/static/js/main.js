
// console.log("hello JS");

function copyToClipBoard(){
    var copyText = document.getElementById('myInput');

    copyText.select();
    copyText.setSelectionRange(0, 99999);

    document.execCommand("copy");

    alert("Copied the text : " + copyText.value);

}