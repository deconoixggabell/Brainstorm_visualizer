var idea_id; //get idea from somewhere in jinja first
var address = 'http://127.0.0.1:5001';
// const ideaInputField = document.getElementById("idea-input-field");

async function getIdeaInfo(){
    //NO ERROR HANDLING FOR NONE FOUND IDs - MUST ADD EVENTUALLY
    const ideaInputField = document.getElementById("idea-input-field");
    const ideaCloudText = document.querySelector("#d-main-idea>span");


    if (ideaInputField) {
        var idead_id = ideaInputField.value;
        var ideaResults = await fetch(`${address}/api/${idead_id}`)
        console.log(ideaResults)
        ideaResults = await ideaResults.json()
		for (const key in ideaResults){
            if(ideaResults.hasOwnProperty(key)){
                console.log(`${key} : ${ideaResults[key]}`)
                if (key == 'main_idea') {
                    ideaCloudText.innerHTML = ideaResults[key];
                }
                if (key == 'cat_1') {
                    const categoryLeft = document.querySelector(".cat-container>.cat-bubble-left>span");
                    categoryLeft.innerHTML = ideaResults[key];
                }
                if (key == 'sub_c_1_1') {
                    const subLeftCategoryLeft = document.querySelector(".subcat-left-container>.cat-bubble-left>span");
                    subLeftCategoryLeft.innerHTML = ideaResults[key];
                }
                if (key == 'sub_c_1_2') {
                    const subLeftCategoryRight = document.querySelector(".subcat-left-container>.cat-bubble-right>span");
                    subLeftCategoryRight.innerHTML = ideaResults[key];
                }
                if (key == 'cat_2') {
                    const categoryRight = document.querySelector(".cat-container>.cat-bubble-right>span");
                    categoryRight.innerHTML = ideaResults[key];
                }
                if (key == 'sub_c_2_1') {
                    const subRightCategoryLeft = document.querySelector(".subcat-right-container>.cat-bubble-left>span");
                    subRightCategoryLeft.innerHTML = ideaResults[key];
                }
                if (key == 'sub_c_2_2') {
                    const subRightCategoryRight = document.querySelector(".subcat-right-container>.cat-bubble-right>span");
                    subRightCategoryRight.innerHTML = ideaResults[key];
                }
            }
		}

    }
}


function updateDiagram(API) {
    if (API = 'API') {
        const ideaCloudText = document.querySelector("#d-main-idea>span");
        const ideaInput = document.getElementById("main-idea-input");
        ideaCloudText.innerHTML = ideaInput.value;
        //CATEGORY 1
        if(document.getElementById("cat_1")){
            console.log("Cat 1 trigger")
            const cat1Input = document.getElementById("cat_1");
            const categoryLeft = document.querySelector(".cat-container>.cat-bubble-left>span");
            categoryLeft.innerHTML = cat1Input.value;
        }
        //CATEGORY 1 - SUB CAT 1
        if(document.getElementById("sub_c_1_1")){
            console.log("Cat 1 - 1 trigger")
            const cat1Sub1Input = document.getElementById("sub_c_1_1");
            const subLeftCategoryLeft = document.querySelector(".subcat-left-container>.cat-bubble-left>span");
            subLeftCategoryLeft.innerHTML = cat1Sub1Input.value;
        }
        //CATEGORY 1 - SUB CAT 2
        if(document.getElementById("sub_c_1_2")) {
            console.log("Cat 1 - 2 trigger")
            const cat1Sub2Input = document.getElementById("sub_c_1_2");
            const subLeftCategoryRight = document.querySelector(".subcat-left-container>.cat-bubble-right>span");
            subLeftCategoryRight.innerHTML = cat1Sub2Input.value;
        }

        //CATEGORY 2
        if(document.getElementById("cat_2")) {
            console.log("Cat 2 trigger")
            const cat2Input = document.getElementById("cat_2");
            const categoryRight = document.querySelector(".cat-container>.cat-bubble-right>span");
            categoryRight.innerHTML = cat2Input.value;

        }
        //CATEGORY 2 - SUB CAT 1
        if(document.getElementById("sub_c_2_1")) {
            console.log("Cat 2 - 1 trigger")
            const cat2Sub1Input = document.getElementById("sub_c_2_1");
            const subRightCategoryLeft = document.querySelector(".subcat-right-container>.cat-bubble-left>span");
            subRightCategoryLeft.innerHTML = cat2Sub1Input.value;
        }
        //CATEGORY 2 - SUB CAT 2
        if(document.getElementById("sub_c_2_2")){
            console.log("Cat 2 - 2 trigger")
        const cat2Sub2Input = document.getElementById("sub_c_2_2");
        const subRightCategoryRight = document.querySelector(".subcat-right-container>.cat-bubble-right>span");
        subRightCategoryRight.innerHTML = cat2Sub2Input.value;
        }
    } else {
        console.log("API doesn't = API in updateDiagram(API)")
    }
    

}
