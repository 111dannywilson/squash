const link = document.getElementById("a")


link.addEventListener("click", function(event) {
event.preventDefault();  // Prevents the default link behavior
    
var linkText = event.target.innerHTML;  // Get the innerHTML of the clicked <a> tag
    
// Send an AJAX request to the server
fetch("/handle_link", {
    method: "POST",
    headers: {
    "Content-Type": "application/json"
    },
    body: JSON.stringify({ linkText: linkText })
}).then(function(response) {
    // Handle the response from the server if needed
});
});

