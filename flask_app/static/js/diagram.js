function updateCategoryFields() {
    const numCategories = parseInt(document.getElementById("num_categories").value);
    const numSubCategories = parseInt(document.getElementById("num_sub_categories").value);
    const categoryFieldsDiv = document.getElementById("category_fields");
    const dMainIdead = document.getElementById("d-main-idea"); //not being used yet - Franco
    categoryFieldsDiv.innerHTML = ""; // Clear existing fields

    for (let i = 1; i <= numCategories; i++) {
        const categoryLabel = document.createElement("label");
        //<label></label>
        categoryLabel.innerText = `Category ${i}`;
        //<label>Category #</label>
        const categoryInput = document.createElement("input");
        categoryInput.type = "text";
        categoryLabel.htmlFor = `cat_${i}`;
        categoryInput.name = `cat_${i}`;
        categoryInput.id = `cat_${i}`;
        categoryInput.setAttribute("oninput", "updateDiagram();")
        categoryInput.className = "form-control";
        categoryFieldsDiv.appendChild(categoryLabel);
        categoryFieldsDiv.appendChild(categoryInput);

        //pass these paramters to the below function
        updateSubCategoryFields(numSubCategories, i);
    }
}

function updateSubCategoryFields(numOfSubCategories, categoryIndex) {
    //const numSubCategories = parseInt(document.getElementById("num_sub_categories").value);
    const categoryFieldsDiv = document.getElementById("category_fields");

    // Create sub-category input fields
    for (let j = 1; j <= numOfSubCategories; j++) {
        const subCategoryLabel = document.createElement("label");
        subCategoryLabel.innerText = `Sub-Category ${j}`;
        subCategoryLabel.htmlFor = `sub_c_${categoryIndex}_${j}`;
        const subCategoryInput = document.createElement("input");
        subCategoryInput.type = "text";
        subCategoryInput.name = `sub_c_${categoryIndex}_${j}`;
        subCategoryInput.id = `sub_c_${categoryIndex}_${j}`;
        subCategoryInput.setAttribute("oninput", "updateDiagram();")
        subCategoryInput.className = "form-control";
        categoryFieldsDiv.appendChild(subCategoryLabel);
        categoryFieldsDiv.appendChild(subCategoryInput);
    }

    
}

// MUST FIX: SUB CATS NOW USE SPANS, MUST CHANGE ALL QUERY SELECTORS TO MATCH SUB CATEOGIES SPANS
function updateDiagram() {
    const ideaCloudText = document.querySelector("#d-main-idea>span");
    const ideaInput = document.getElementById("main-idea-input");
    ideaCloudText.innerHTML = ideaInput.value;
    //CATEGORY 1
    if(document.getElementById("cat_1")){
        console.log("Cat 1 trigger")
        const cat1Input = document.getElementById("cat_1");
        const categoryLeft = document.querySelector(".cat-container>.cat-bubble-left");
        categoryLeft.innerHTML = cat1Input.value;
    }
    //CATEGORY 1 - SUB CAT 1
    if(document.getElementById("sub_c_1_1")){
        console.log("Cat 1 - 1 trigger")
        const cat1Sub1Input = document.getElementById("sub_c_1_1");
        const subLeftCategoryLeft = document.querySelector(".subcat-left-container>.cat-bubble-left");
        subLeftCategoryLeft.innerHTML = cat1Sub1Input.value;
    }
    //CATEGORY 1 - SUB CAT 2
    if(document.getElementById("sub_c_1_2")) {
        console.log("Cat 1 - 2 trigger")
        const cat1Sub2Input = document.getElementById("sub_c_1_2");
        const subLeftCategoryRight = document.querySelector(".subcat-left-container>.cat-bubble-right");
        subLeftCategoryRight.innerHTML = cat1Sub2Input.value;
    }

    //CATEGORY 2
    if(document.getElementById("cat_2")) {
        console.log("Cat 2 trigger")
        const cat2Input = document.getElementById("cat_2");
        const categoryRight = document.querySelector(".cat-container>.cat-bubble-right");
        categoryRight.innerHTML = cat2Input.value;

    }
    //CATEGORY 2 - SUB CAT 1
    if(document.getElementById("sub_c_2_1")) {
        console.log("Cat 2 - 1 trigger")
        const cat2Sub1Input = document.getElementById("sub_c_2_1");
        const subRightCategoryLeft = document.querySelector(".subcat-right-container>.cat-bubble-left");
        subRightCategoryLeft.innerHTML = cat2Sub1Input.value;
    }
    //CATEGORY 2 - SUB CAT 2
    if(document.getElementById("sub_c_2_2")){
        console.log("Cat 2 - 2 trigger")
    const cat2Sub2Input = document.getElementById("sub_c_2_2");
    const subRightCategoryRight = document.querySelector(".subcat-right-container>.cat-bubble-right");
    subRightCategoryRight.innerHTML = cat2Sub2Input.value;
    }
    

}
