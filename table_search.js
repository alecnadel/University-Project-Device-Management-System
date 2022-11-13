function formatDate(dateVal) {
    // creates data string in correct format
    var newDate = new Date(dateVal);

    var sMonth = padValue(newDate.getMonth() + 1);
    var sDay = padValue(newDate.getDate());
    var sYear = newDate.getFullYear();
    var sHour = newDate.getHours();
    var sMinute = padValue(newDate.getMinutes());
    var sSeconds = padValue(newDate.getSeconds());
    var sAMPM = "AM";

    var iHourCheck = parseInt(sHour);

    if (iHourCheck > 12) {
        sAMPM = "PM";
        sHour = iHourCheck - 12;
    }
    else if (iHourCheck === 0) {
        sHour = "12";
    }

    sHour = padValue(sHour);

    return sYear+ "-" + sMonth + "-" + sDay + " " + sHour + ":" + sMinute + ":" + sSeconds;
}

function padValue(value) {
    return (value < 10) ? "0" + value : value;
}

function submitform() {
  var x = document.getElementsByName('DeviceBorrow');
    x[0].submit(); // Form submission
}
 
// function redirect(url)
//     {
//     // var url = "http://www.(url).com";
//     window.location(url);
//     }


document.addEventListener("DOMContentLoaded", () => {
    // actives search features on device list page load in


    function searchfilter(col_inputs,all_cols) {
        // function checks if a device in table it fits the search criteria
        
        //  getting imput data 
        const searchableCellscols = Array() 
        const tableRows1 = col_inputs[0][1]
            .closest("table")
            .querySelectorAll("tbody > tr");
        // input cols data
        for (let index = 0; index < 9; index++) {
            const searchableCell = Array.from(tableRows1).map(
            (row) => row.querySelectorAll("td")[index]
            );
            searchableCellscols.push(searchableCell)
        };
        // input search cols search querys & setting them to lower case
        const searchQuerys = Array()
        for (const col_ind in col_inputs) {
            var colinput = col_inputs[col_ind][1].value.toLowerCase().trim()
            if (colinput != "") {
                searchQuerys.push(colinput)
            } else {
                searchQuerys.push(null)
            }
            
            
        };
        // General seaerch query & setting it to lower case
        const GeneralQuery = general[1].value.toLowerCase().trim();

    
    
    for (var row = 0; row < tableRows1.length;row++) { // resets all rows to visibile
        tableRows1[row].style.visibility = null;
    };

    
    for (var n = 0; n < tableRows1.length;n++){ // looping over all device table rows
        var result = 1 
        var gen_count = 0
        for (var j = 0; j < 9;j++){ // looping over all device table columns entries
            var value = searchableCellscols[j][n].innerText.toLowerCase().replace(",", "")
            
            if (searchQuerys[j]) { // checks col input exists
                
            if ((value.search(searchQuerys[j])) === -1){ // checks the search result is true
                result = -1;
            };};
            if (GeneralQuery) { // checks General query input exists any column 
            if ((value.search(GeneralQuery)) === -1) {
                gen_count += 1
            };};

        };
        if (gen_count == 9) { // check of general search result has shown up at least once 
            result = -1
        };
        
        const notborrowed = document.querySelector(".availability_check")
        if (notborrowed.checked) { // check if device avaliable is selected or not 
            const borrowed = tableRows1[n].querySelectorAll(".popup")
            // console.log("borrowed",borrowed)
            if (borrowed.length === 1) { // if device borrowed selected return result false (-1) 
                result = -1
            }
            
        } 
        
        if (result === -1){ // applies search result to device table
            tableRows1[n].style.visibility = "collapse";
        };
        
    };

    //  check any device are still visable to the user & displays alert message if none are.
    const notvis_rows = document.querySelectorAll("#table_body tr[style='visibility: collapse;']");
    const all_rows = document.querySelectorAll("#table_body tr");
    var i = all_rows.length - notvis_rows.length
    console.log("vis",  i)
    const alert = document.querySelector(".alert");
    if (i == 0) {
    alert.style.visibility = null;
        } else {
    alert.style.visibility = "hidden";
        };
    };

    // setup required inputs
    const inputField = document.querySelectorAll(".search-input");
    const entries = Object.entries(inputField);
    const general = entries[0]
    const col_inputs = entries.slice(1,5)
    // apply search inputs on page load
    searchfilter(col_inputs)



    // input to fields update event to update s
    inputField.forEach((inputField) => {
    inputField.addEventListener("input", () => {
        searchfilter(col_inputs)
    

    });
});
    // });

    

    //  check if availability_check as changed and applies the required change
    const notborrowed = document.querySelector(".availability_check")
    
    notborrowed.addEventListener("change", () => {

        searchfilter(col_inputs)

        });


});

//  constructs the device borrowing form onclick of device borrow button
document.getElementById("deviceborrow").onclick = function() {
    const checked_devices = document.querySelectorAll(".check_device:checked");
    var count = parseInt(document.querySelector('#BorrowedDevice').getAttribute("data-name"));
    const device_form = document.querySelector("#deviceform_input");
  
    device_form.innerHTML = "";
    if (count + checked_devices.length > 3) {
      
      const message = document.createElement("span")
      message.id = "error_message";
      message.innerHTML = "Maximum number of Borrowed devices already reached";
      device_form.appendChild(message)
      document.getElementById("btn_submit").disabled = true;//.style.visibility = "hidden";
    
    } else if (checked_devices.length <= 0) {
      const message = document.createElement("span")
      message.id = "error_message";
      // message.removeChild(message.firstChild)
      while (message.firstChild) message.removeChild(message.firstChild);
      message.innerHTML = "No new Devices selected";
      device_form.appendChild(message)
      document.getElementById("btn_submit").disabled = true;
    } else if (count + checked_devices.length <=3) {
    console.log("device_form",device_form)
    var checkedrows = [];
    document.getElementById("btn_submit").disabled = false;
    // console.log("1checked_devices",checked_devices)
  
    var devForm = document.createElement("form");
    devForm.method = "POST"
    devForm.action = "/Search"
    devForm.name = "DeviceBorrow"
    device_form.appendChild(devForm)
    
    var i = checked_devices.length
    var count = document.createElement("input");
    count.type = "hidden"
    count.id = "count"
    count.name = "count"
    count.value = i
    devForm.appendChild(count);
  
    var n = 0
    for (const inputcheck of checked_devices) {
      n += 1;
      var title = (inputcheck.parentNode.parentNode.children[0]).cloneNode(true)
      var labeltitle = document.createElement("label");
      labeltitle.innerText = "Device name:  "
      
      var current = new Date(); //'Mar 11 2015' current.getTime() = 1426060964567
      var ReturnDate = new Date(current.getTime() + 14*86400000); // + 1 day in ms
  
      var labelReturn = document.createElement("label");
      labelReturn.for = `ReturnDate_${n}`
      labelReturn.innerText = "Return date:  "
      var Return = document.createElement("input");
      Return.type = "datetime-local";
      Return.className = "form-control px-3 py-2"
      Return.id = `ReturnDate_${n}`;
      Return.name = `ReturnDate_${n}`;
      console.log("ReturnDate.toISOString().slice(0,16)",ReturnDate.toISOString().slice(0,16))
      var ReturnDate = ReturnDate.toISOString().slice(0,16)
      Return.value = ReturnDate;
      // console.log(`ReturnDate_${n}`);
      
      var Device_name = document.createElement("input");
      Device_name.type = "hidden";
      Device_name.id = `Device_name_${n}`;
      Device_name.name = `Device_name_${n}`;
      Device_name.value = title.innerHTML;
  
      var Start_Date = document.createElement("input");
      Start_Date.type = "hidden";
      Start_Date.id = `Start_Date_${n}`;
      Start_Date.name = `Start_Date_${n}`;
      var start = Date();
      start = formatDate(start)
      Start_Date.value = start;
  
      devForm.appendChild(Start_Date);
      devForm.appendChild(Device_name);
      devForm.appendChild(labeltitle)
      devForm.appendChild(title);
      devForm.appendChild(labelReturn)
      devForm.appendChild(Return); 
    } 
    };
    
    
  


  };




//
// Sorts a HTML table.
// 
//  table, the HTML table to be sort
//  column, index if the column to sort table on
//  asc, current stat of the determines if the sorting will be in ascending or descending order
//
 
 function sortTableByColumn(table, column, asc = true) {
    const dirModifier = asc ? 1 : -1;
    const tBody = table.tBodies[0];
    const rows = Array.from(tBody.querySelectorAll("tr"));

    // Sort each row
    const sortedRows = rows.sort((a, b) => {
        const aColText = a.querySelector(`td:nth-child(${ column + 1 })`).textContent.trim();
        const bColText = b.querySelector(`td:nth-child(${ column + 1 })`).textContent.trim();

        return aColText > bColText ? (1 * dirModifier) : (-1 * dirModifier);
    });

    // Remove all existing TRs from the table
    while (tBody.firstChild) {
        tBody.removeChild(tBody.firstChild);
    }

    // Re-add the newly sorted rows
    tBody.append(...sortedRows);

    // Remember how the column is currently sorted
    table.querySelectorAll("th").forEach(th => th.classList.remove("th-sort-asc", "th-sort-desc"));
    table.querySelector(`th:nth-child(${ column + 1})`).classList.toggle("th-sort-asc", asc);
    table.querySelector(`th:nth-child(${ column + 1})`).classList.toggle("th-sort-desc", !asc);
}

document.querySelectorAll(".sort").forEach(headerCell => { // table-sortable th
    headerCell.addEventListener("click", () => {
        //  checks if device header as been click then sorts table based on that column
        const tableElement = headerCell.parentElement.parentElement.parentElement;
        const headerCells = document.querySelectorAll(".sort")
        const headerIndex = Array.prototype.indexOf.call(headerCells, headerCell); //headerCell.parentElement.children
        const currentIsAscending = headerCell.classList.contains("th-sort-asc");

        sortTableByColumn(tableElement, headerIndex, !currentIsAscending);
    });
});


function myFunction(texts) {
    // alert for unavaliable device in device table
    window.alert(texts);
    }
