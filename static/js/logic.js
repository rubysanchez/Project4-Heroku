function init() {

    // Once database is ready to call the data endpoint
    d3.json("/data").then((data) => {
        console.log(data.prediction);
        var ages = data.Age;
        var income = data.Median_Household_Income;
        var gender = data.Gender;
        var ethnicity = data.Race;
        var stage = data.Cancer_Stage;
        var site = data.Cancer_Site;
        var type = data.Cancer_Type;
    
    
    // Hardcoding the lists with temporary data
    // let ages = ["0-7","8-10"];
    // let income = ["<15K",">25k"];
    // let gender = ["Male", "Female"];
    // let ethnicity = ["Non-Hispanic White", "Hispanic (All Races)", "Non-Hispanic Black"];
    // let stage = ["I", "II", "III", "IA", "IB", "IIA", "IIB"];
    // let site = ["Prostate", "Ovary", "Breast", "Thyroid"];

    // Select the form fields
        let age_select = d3.select("#age");
        let income_select = d3.select("#income");
        let gender_select = d3.select("#gender");
        let ethnicity_select = d3.select("#ethnicity");
        let stage_select = d3.select("#stage");
        let site_select = d3.select("#site");
        let type_select = d3.select("#type");

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
        type.forEach(function(option){
            type_select.append("option").text(option).property("value",option);
        })
    });
}

// Initialize the function
init();