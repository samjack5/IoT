const url_package = require("url");
const url= "https://archive-api.open-meteo.com/v1/era5?latitude=52.52&longitude=13.41&start_date=2021-01-01&end_date=2021-12-31&hourly=temperature_2m"
console.log(url_package.forms(url));
console.log(queryString.parse(url));

console-log(url_package.format(queryString.parse(url)));