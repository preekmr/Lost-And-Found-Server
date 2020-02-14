import "./styles.css";
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import $ from "jquery";

const HOST = "http://138.68.48.60";

function getItems() {
  $.get(HOST + "/items", function (data) {

    var html = "";

    data.forEach(element => {
      console.log(element);
      var ele = '';
      if(element.file_name!="") {
        ele = 
        `<div class="col-lg-3 col-md-4 col-sm-12">
          <div class="card" style="width: 14rem;">
            <a href="${HOST+'/uploads/'+element.file_name}" target="_blank">
            <img src="${HOST+'/uploads/'+element.file_name}" class="card-img-top" alt="${element.name}"></a>
            <div class="card-body">
              <h5 class="card-title">${element.name.toUpperCase()}</h5>
              <p class="card-text">Owner: <b>${element.owner}</b></p>
              <p class="card-text">Found on: <b>${element.date_found}</b></p>
              <p class="card-text">Found at: <b>${element.location_found}</b></p>
              <p class="card-text">Color: <b>${element.color}</b></p>
            </div>
          </div><br/>
        </div>
      `;
      } else {
        ele = 
      `<div class="col-lg-3 col-md-4 col-sm-12">
        <div class="card" style="width: 14rem;">
          <div class="card-body">
            <h5 class="card-title">${element.name.toUpperCase()}</h5>
            <p class="card-text">Owner: <b>${element.owner}</b></p>
            <p class="card-text">Found on: <b>${element.date_found}</b></p>
            <p class="card-text">Found at: <b>${element.location_found}</b></p>
            <p class="card-text">Color: <b>${element.color}</b></p>
          </div>
        </div><br/>
      </div>
    `;
      }
    html = html + ele;
    });

    $("#result").html(html);
  });
}
getItems();
