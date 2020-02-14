import "./styles.css";
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import $ from "jquery";

const HOST = "http://138.68.48.60";

$(document).ready(function () {

  $("#btnSubmit").click(function (event) {

      //stop submit the form, we will post it manually.
      event.preventDefault();

      // Get form
      var form = $('#fileUploadForm')[0];

      var extra_data = {};
      extra_data["name"] = form[0].value;
      extra_data["owner"] = form[1].value;
      extra_data["color"] = form[2].value;
      extra_data["shape"] = form[3].value;
      extra_data["date_found"] = form[4].value;
      extra_data["location_found"] = form[5].value;


  // Create an FormData object 
      var data = new FormData(form);
      console.log(JSON.stringify(extra_data))
  // If you want to add an extra field for the FormData
      data.append("data", JSON.stringify(extra_data));
      if(form[6].files[0] != undefined) {
        data.append("file", form[6].files[0]);
      }
    

  // disabled the submit button
      $("#btnSubmit").prop("disabled", true);

      $.ajax({
          type: "POST",
          enctype: 'multipart/form-data',
          url: HOST+"/insert",
          data: data,
          processData: false,
          contentType: false,
          cache: false,
          timeout: 600000,
          success: function (data) {

              $("#result").text(data);
              console.log("SUCCESS : ", data);
              $("#btnSubmit").prop("disabled", false);
              alert("Data submitted successfully.");
              window.top.location="index.html";
          },
          error: function (e) {

              $("#result").text(e.responseText);
              console.log("ERROR : ", e);
              alert("Error: "+e.responseJSON.message);
              $("#btnSubmit").prop("disabled", false);

          }
      });

  });

});
