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
        const subCategoryInput = document.createElement("input");
        subCategoryInput.type = "text";
        subCategoryInput.name = `sub_cat_${categoryIndex}_${j}`;
        subCategoryInput.id = `sub_cat_${categoryIndex}_${j}`;
        subCategoryInput.setAttribute("oninput", "updateDiagram();")
        subCategoryInput.className = "form-control";
        categoryFieldsDiv.appendChild(subCategoryLabel);
        categoryFieldsDiv.appendChild(subCategoryInput);
    }

    
}

    //MUST FIX WITH A PARAMETER PASSED INSTEAD. OTHERWISE IF A DIV DOESN'T EXISTS, IT WILL STOP RUNNING
    //... THE REMAINDER OF THE CODE
function updateDiagram() {
    // const ideaCloud = document.getElementById("d-main-idea"); 
    const ideaCloudText = document.querySelector("#d-main-idea>span");

    const ideaInput = document.getElementById("main-idea-input");
    const cat1Input = document.getElementById("cat_1");
    const cat2Input = document.getElementById("cat_2");


    const categoryLeft = document.querySelector(".cat-container>.cat-bubble-left");
    const categoryRight = document.querySelector(".cat-container>.cat-bubble-right");
    
    //Inputs need to be checked if they exist first
    //...if they do not exist, DO NOT SET .VALUE or JS will stop processing
    //...remaining code.
    const cat1Sub1Input = document.getElementById("sub_cat_1_1");
    const cat1Sub2Input = document.getElementById("sub_cat_1_2");

    const cat2Sub1Input = document.getElementById("sub_cat_2_1");
    const cat2Sub2Input = document.getElementById("sub_cat_2_2");

    const subLeftCategoryLeft = document.querySelector(".subcat-left-container>.cat-bubble-left");
    const subLeftCategoryRight = document.querySelector(".subcat-left-container>.cat-bubble-right");

    const subRightCategoryLeft = document.querySelector(".subcat-right-container>.cat-bubble-left");
    const subRightCategoryRight = document.querySelector(".subcat-right-container>.cat-bubble-right");

    //MUST FIX WITH A PARAMETER PASSED INSTEAD. OTHERWISE IF A DIV DOESN'T EXISTS, IT WILL STOP RUNNING
    //... THE REMAINDER OF THE CODE
    ideaCloudText.innerHTML = ideaInput.value;
    categoryLeft.innerHTML = cat1Input.value;
    categoryRight.innerHTML = cat2Input.value;


    subLeftCategoryLeft.innerHTML = cat1Sub1Input.value;
    subLeftCategoryRight.innerHTML = cat1Sub2Input.value;

    subRightCategoryLeft.innerHTML = cat2Sub1Input.value;
    subRightCategoryRight.innerHTML = cat2Sub2Input.value;





}
