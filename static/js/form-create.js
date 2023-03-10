var tagId = 0;

function addField() {
  tagId++;
  var currentId = tagId;

  var container = document.getElementById("fields-container");

  // Create row div for fields
  var container_item_1 = document.createElement("div");
  container_item_1.id = "item-1-" + tagId;
  container_item_1.className = "form-group col-md-4";
  container.appendChild(container_item_1);

  var container_item_2 = document.createElement("div");
  container_item_2.id = "item-2-" + tagId;
  container_item_2.className = "form-group col-md-2";
  container.appendChild(container_item_2);

  var container_item_3_1 = document.createElement("div");
  container_item_3_1.id = "item-3-1-" + tagId;
  container_item_3_1.className = "form-group col-md-1";
  container.appendChild(container_item_3_1);

  var container_item_3_2 = document.createElement("div");
  container_item_3_2.id = "item-3-2-" + tagId;
  container_item_3_2.className = "form-group col-md-2";
  container.appendChild(container_item_3_2);

  var container_item_4 = document.createElement("div");
  container_item_4.id = "item-4-" + tagId;
  container_item_4.className = "form-group col-md-3";
  container.appendChild(container_item_4);

  // Create label for field
  var label1 = document.createElement("label");
  label1.setAttribute("for", "inputName");
  label1.id = "label-1-" + tagId;
  label1.innerHTML = "Column name";
  container_item_1.appendChild(label1);

  // Create input field
  var input = document.createElement("input");
  input.id = "tag-" + tagId;
  input.type = "text";
  input.className = "form-control";
  input.style.width = "250px";
  input.setAttribute("name", "dynamic-key[]");
  container_item_1.appendChild(input);

  // Create label for selection field
  var label2 = document.createElement("label");
  label2.setAttribute("for", "inputType");
  label2.id = "label-2-" + tagId;
  label2.innerHTML = "Type";
  container_item_2.appendChild(label2);

  var br = document.createElement("br");
  br.id = "br-l-" + tagId;
  container_item_2.appendChild(br);

  // Create selection field
  var select = document.createElement("select");
  select.className = "custom-select mr-sm-2";
  select.id = "select-" + tagId;
  select.style.width = "150px";
  select.setAttribute("name", "dynamic-value[]");
  container_item_2.appendChild(select);

  // Add default option to select field
  var option = document.createElement("option");
  option.value = "name";
  option.disabled = false;
  option.selected = true;
  option.label = "Full Name";
  select.appendChild(option);

  // Add other options to select field
  var option1 = document.createElement("option");
  option1.value = "job";
  option1.innerHTML = "Job";
  select.appendChild(option1);

  var option2 = document.createElement("option");
  option2.value = "email";
  option2.innerHTML = "Email";
  select.appendChild(option2);

  var option3 = document.createElement("option");
  option3.value = "domain-name";
  option3.innerHTML = "Domain Name";
  select.appendChild(option3);
  var option4 = document.createElement("option");
  option4.value = "phone";
  option4.innerHTML = "Phone";
  select.appendChild(option4);
  var option5 = document.createElement("option");
  option5.value = "company";
  option5.innerHTML = "Company";
  select.appendChild(option5);
  var option6 = document.createElement("option");
  option6.value = "text";
  option6.innerHTML = "Text";
  select.appendChild(option6);
  var option7 = document.createElement("option");
  option7.value = "integer";
  option7.innerHTML = "Integer";
  select.appendChild(option7);
  var option8 = document.createElement("option");
  option8.value = "address";
  option8.innerHTML = "Address";
  select.appendChild(option8);
  var option9 = document.createElement("option");
  option9.value = "date";
  option9.innerHTML = "Date";
  select.appendChild(option9);

  // Add event listener to select field
  select.addEventListener("change", function() {
    if (this.value === "integer") {
        try {
          itsNotInt_orText(currentId);
        } catch (error) {
          console.error(error);
        } finally {
          thisInt(currentId);
        }
    }
    else if (this.value === 'text') {
        try {
          itsNotInt_orText(currentId);
        } catch (error) {
          console.error(error);
        } finally {
          thisText(currentId);
        }
    }
    else {
        itsNotInt_orText(currentId);
    }
  });

  // Create delete button
  var br = document.createElement("br");
  br.id = "br-del-" + tagId;
  container_item_4.appendChild(br);


  var deleteBTN = document.createElement("a");
  deleteBTN.style.color = "red";
  deleteBTN.id = "delete-" + tagId;
  deleteBTN.innerHTML = "Delete";
  deleteBTN.addEventListener("click", function() {
    delField(currentId);
  });
  container_item_4.appendChild(deleteBTN);

  var br = document.createElement("br");
  br.id = "br-" + tagId;
  container.appendChild(br);
}

function delField(id) {
  var container_item_1 = document.getElementById("item-1-" + id);
  var container_item_2 = document.getElementById("item-2-" + id);
  var container_item_3_1 = document.getElementById("item-3-1-" + id);
  var container_item_3_2 = document.getElementById("item-3-2-" + id);
  var container_item_4 = document.getElementById("item-4-" + id);
  var label1 = document.getElementById("label-1-" + id);
  var input = document.getElementById("tag-" + id);
  var label2 = document.getElementById("label-2-" + id);
  var br1 = document.getElementById("br-l-" + id);
  var br2 = document.getElementById("br-" + id);
  var br3 = document.getElementById("br-del-" + id);
  var select = document.getElementById("select-" + id);
  var option = document.querySelector("#select-" + id + " option[value='name']");
  var option1 = document.querySelector("#select-" + id + " option[value='job']");
  var option2 = document.querySelector("#select-" + id + " option[value='email']");
  var option3 = document.querySelector("#select-" + id + " option[value='domain-name']");
  var option4 = document.querySelector("#select-" + id + " option[value='phone']");
  var option5 = document.querySelector("#select-" + id + " option[value='company-name']");
  var option6 = document.querySelector("#select-" + id + " option[value='text']");
  var option7 = document.querySelector("#select-" + id + " option[value='integer']");
  var option8 = document.querySelector("#select-" + id + " option[value='address']");
  var option9 = document.querySelector("#select-" + id + " option[value='date']");
  var deleteBTN = document.getElementById("delete-" + id);

  container_item_1.parentNode.removeChild(container_item_1);
  container_item_2.parentNode.removeChild(container_item_2);
  container_item_3_1.parentNode.removeChild(container_item_3_1);
  container_item_3_2.parentNode.removeChild(container_item_3_2);
  container_item_4.parentNode.removeChild(container_item_4);
  label1.parentNode.removeChild(label1);
  input.parentNode.removeChild(input);
  label2.parentNode.removeChild(label2);
  br1.parentNode.removeChild(br1);
  br2.parentNode.removeChild(br2);
  br3.parentNode.removeChild(br3);
  select.parentNode.removeChild(select);
  option.parentNode.removeChild(option);
  option1.parentNode.removeChild(option1);
  option2.parentNode.removeChild(option2);
  option3.parentNode.removeChild(option3);
  option4.parentNode.removeChild(option4);
  option5.parentNode.removeChild(option5);
  option6.parentNode.removeChild(option6);
  option7.parentNode.removeChild(option7);
  option8.parentNode.removeChild(option8);
  deleteBTN.parentNode.removeChild(deleteBTN);
}

function thisInt(id) {
    var container_item_3_1 = document.getElementById("item-3-1-" + id);
    var label3 = document.createElement("label");
    label3.id = "int-1-" + id;
    label3.innerHTML = "From";
    container_item_3_1.appendChild(label3);

    var input = document.createElement("input");
    input.id = "int-field-1-" + id;
    input.type = "number";
    input.className = "form-control";
    input.style.width = "70px";
    input.setAttribute("name", "integer-value[]");
    container_item_3_1.appendChild(input);

    var container_item_3_2 = document.getElementById("item-3-2-" + id);

    var label4 = document.createElement("label");
    label4.id = "int-2-" + id;
    label4.innerHTML = "To";
    container_item_3_2.appendChild(label4);

    var input1 = document.createElement("input");
    input1.id = "int-field-2-" + id;
    input1.type = "number";
    input1.className = "form-control";
    input1.style.width = "70px";
    input1.setAttribute("name", "integer-value[]");
    container_item_3_2.appendChild(input1);
}

function thisText(id) {
    var container_item_3_1 = document.getElementById("item-3-1-" + id);
    var label3 = document.createElement("label");
    label3.id = "int-1-" + id;
    label3.innerHTML = "From";
    container_item_3_1.appendChild(label3);

    var input = document.createElement("input");
    input.id = "int-field-1-" + id;
    input.type = "number";
    input.className = "form-control";
    input.style.width = "70px";
    input.setAttribute("name", "text-value[]");
    container_item_3_1.appendChild(input);

    var container_item_3_2 = document.getElementById("item-3-2-" + id);

    var label4 = document.createElement("label");
    label4.id = "int-2-" + id;
    label4.innerHTML = "To";
    container_item_3_2.appendChild(label4);

    var input1 = document.createElement("input");
    input1.id = "int-field-2-" + id;
    input1.type = "number";
    input1.className = "form-control";
    input1.style.width = "70px";
    input1.setAttribute("name", "text-value[]");
    container_item_3_2.appendChild(input1);
}

function itsNotInt_orText(id) {
    var label3 = document.getElementById("int-1-" + id);
    var input = document.getElementById("int-field-1-" + id);
    var label4 = document.getElementById("int-2-" + id);
    var input1 = document.getElementById("int-field-2-" + id);

    label3.parentNode.removeChild(label3);
    input.parentNode.removeChild(input);
    label4.parentNode.removeChild(label4);
    input1.parentNode.removeChild(input1);
}


document.getElementById("add-field").addEventListener("click", addField);