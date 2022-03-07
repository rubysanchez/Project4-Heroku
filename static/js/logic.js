function init() {

    // Once database is ready to call the data endpoint
    // d3.json("http://127.0.0.1:5000/data").then((data) => {
    //     console.log(data);
    //     var income = data.income;
    //     var gender = data.gender;
    //     var ethnicity = data.race;
    //     var stage = data.stage;
    //     var site = data.site;
    //     var type = data.type;
    
    
    // Hardcoding the lists with temporary data
    // let ages = ["0-7","8-10"];
    let income = ["$75,000+","$65,000 - $69,999", "$70,000 - $74,999", "$60,000 - $64,999", "< $35,000"];
    let gender = ["Male", "Female"];
    let ethnicity = ["Non-Hispanic Asian or Pacific Islander","Non-Hispanic White", "Hispanic (All Races)", "Non-Hispanic Black", "Non-Hispanic American Indian/Alaska Native"];
    let stage = ["I", "II", "III", "IA", "IB", "IIA", "IIB"];
    let site = ["Prostate", "Ovary", "Breast", "Thyroid"];
    let type = ["Adenomas And Adenocarcinomas", "Ductal And Lobular Neoplasms", "Nevi And Melanomas", "Epithelial Neoplasms, Nos"];

    // Select the form fields
        // let age_select = d3.select("#age");
    let income_select = d3.select("#income");
    let gender_select = d3.select("#gender");
    let ethnicity_select = d3.select("#ethnicity");
    let stage_select = d3.select("#stage");
    let site_select = d3.select("#site");
    let type_select = d3.select("#type");

    // Append the options to the select fields
        // ages.forEach(function(option) {
        //     age_select.append("option").text(option).property("value", option);
        // });
    income.forEach(function (option) {
        income_select.append("option").text(option).property("value", option);
    })
    gender.forEach(function (option) {
        gender_select.append("option").text(option).property("value", option);
    })
    ethnicity.forEach(function (option) {
        ethnicity_select.append("option").text(option).property("value", option);
    })
    stage.forEach(function (option) {
        stage_select.append("option").text(option).property("value", option);
    })
    site.forEach(function (option) {
        site_select.append("option").text(option).property("value", option);
    })
    type.forEach(function (option) {
        type_select.append("option").text(option).property("value", option);
    })
    // });
}

// Initialize the function
init();