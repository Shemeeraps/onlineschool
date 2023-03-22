let data = [
  {
    item:"Computer Science",
    subitems:["Data Structures","Artificial Intelligence","Databases","C","C++"]
  },
  {
    item:"Physics",
    subitems:["Thermodynamics","Geology","Fluid Dynamics","Astronomy","Space and Time"]
  },
  {
    item:"Biology",
    subitems:["Anatomy","Genetics","Microbiology","Forensic Biology","Zoology","Natural Science"] 
  },
  {
    item:"Commerce",
    subitems:["Accountancy","Business Studies","Ecnomics","Informatics"]
  },
  {
    items:"Humanities",
    subitems:["History","Philosophy","Geography","Ecnomics","Sociology"]
  },
  {
    items:"Mathematics",
    subitems:["Algebra","Calculus","Trigonometry","Integration","Set Theory"]
  }
];
window.onload = function() {
    var departmentSel = document.getElementById("department");
    var courseSel = document.getElementById("course");
  
    for (var x in data) {
      departmentSel.options[departmentSel.options.length] = new Option(data[x].item, x);
    }
    departmentSel.onchange = function() {
      //empty 
      courseSel.length = 1
      //display correct values
      for (var y of data[this.value].subitems) {
        courseSel.options[courseSel.options.length] = new Option(y, y);
      }
    }
}
