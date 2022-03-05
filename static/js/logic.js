function init() {

    // Once database is ready to call the data endpoint
    // d3.json("/data").then((data) => {
    //     let ages = data.Age;
    //     let income = data.Median_Household_Income;
    //     let gender = data.Gender;
    //     let ethnicity = data.Race;
    //     let stage = data.Cancer_Stage;
    //     let site = data.Cancer_Site;
    //     let type = data.Cancer_Type;
    // });
    
    // Hardcoding the lists with temporary data
    let ages = ["0-7","8-10"];
    let income = ["<15K",">25k"];
    let gender = ["Male", "Female"];
    let ethnicity = ["Non-Hispanic White", "Hispanic (All Races)", "Non-Hispanic Black"];
    let stage = ["I", "II", "III", "IA", "IB", "IIA", "IIB"];
    let site = ["Prostate", "Ovary", "Breast", "Thyroid"];

    // Select the form fields
    let age_select = d3.select("#age");
    let income_select = d3.select("#income");
    let gender_select = d3.select("#gender");
    let ethnicity_select = d3.select("#ethnicity");
    let stage_select = d3.select("#stage");
    let site_select = d3.select("#site");

    // Append the options to the select fields
    ages.forEach(function(option) {
        age_select.append("option").text(option).property("value", option);
    });
    income.forEach(function(option){
        income_select.append("option").text(option).property("value",option);
    })
    gender.forEach(function(option){
        gender_select.append("option").text(option).property("value",option);
    })
    ethnicity.forEach(function(option){
        ethnicity_select.append("option").text(option).property("value",option);
    })
    stage.forEach(function(option){
        stage_select.append("option").text(option).property("value",option);
    })
    site.forEach(function(option){
        site_select.append("option").text(option).property("value",option);
    })
}

// Initialize the function
init();