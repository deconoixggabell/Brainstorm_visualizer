function updateCategoryFields() {
    const numCategories = parseInt(document.getElementById("num_categories").value);
    const categoryFieldsDiv = document.getElementById("category_fields");
    const dMainIdead = document.getElementById("d-main-idea"); //not being used yet - Franco
    categoryFieldsDiv.innerHTML = ""; // Clear existing fields

    for (let i = 1; i <= numCategories; i++) {
        const categoryLabel = document.createElement("label");
        //<label></label>
        //categoryLabel.innerText = `Category ${i}`;
        
        //<label>Category #</label>
        const categoryInput = document.createElement("input");
        categoryInput.type = "text";
        categoryLabel.htmlFor = `cat_${i}`;
        categoryInput.name = `cat_${i}`;
        categoryInput.className = "form-control";
        categoryFieldsDiv.appendChild(categoryLabel);
        categoryFieldsDiv.appendChild(categoryInput);

        // Create sub-category input fields
        for (let j = 1; j <= 3; j++) {
            const subCategoryLabel = document.createElement("label");
            subCategoryLabel.innerText = `Sub-Category ${j}`;
            const subCategoryInput = document.createElement("input");
            subCategoryInput.type = "text";
            subCategoryInput.name = `sub_cat_${i}_${j}`;
            subCategoryInput.className = "form-control";
            categoryFieldsDiv.appendChild(subCategoryLabel);
            categoryFieldsDiv.appendChild(subCategoryInput);
        }
    }
}

function updateDiagram() {
    const ideaCloud = document.getElementById("d-main-idea"); //not being used yet - Franco
    const ideaInput = document.getElementById("main-idea-input");
    ideaCloud.innerHTML = ideaInput.value;

}
