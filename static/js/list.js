const currentYear = new Date().getFullYear();
const currentMonth = new Date().getMonth() + 1;
const yearDropdown = document.getElementById("year");
const monthDropdown = document.getElementById("month");

let query = window.location.search;
let param = new URLSearchParams(query);
let paramYear = param.get("year");
let paramMonth = param.get("month");
// create year options
for (let year = 2000; year <= 2050; year++) {
  const option = document.createElement("option");
  option.value = year;
  option.text = year;
  if (year === currentYear && !paramYear) {
    option.selected = true;
  }
  if (year === parseInt(paramYear)) {
    option.selected = true;
  }
  yearDropdown.appendChild(option);
}

// create month options
for (let month = 1; month <= 12; month++) {
  const option = document.createElement("option");
  option.value = month < 10 ? "0" + month : month;
  option.text = month < 10 ? "0" + month : month;
  if (month === currentMonth && !paramMonth) {
    option.selected = true;
  }
  if (month === parseInt(paramMonth)) {
    option.selected = true;
  }
  monthDropdown.appendChild(option);
}
