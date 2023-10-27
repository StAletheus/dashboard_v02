// Fetch models from the API
fetch('/api/get_models')
    .then(response => response.json())
    .then(data => {
        console.log('creating option for: ' + model);
const select = document.getElementById('modelSelect'); // Assuming the dropdown has id="modelSelect"
data.forEach(model => {
    let option = document.createElement('option');
    option.value = model;
    option.innerText = model;
    console.log('Option created:', option);
    select.appendChild(option);

});
    })
    .catch (error => {
    console.error("There was a problem with the fetch operation:", error);
});