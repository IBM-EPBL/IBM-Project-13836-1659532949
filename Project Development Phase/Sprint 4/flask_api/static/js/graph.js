google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);


function drawChart(fdata) {
  
  var arrValues = [['Month', 'Sales Figure']];      
  for (var key in fdata) {
   
    arrValues.push(["l", "10"]);
  }
  var p = [
      ['Effort', 'Amount given'],
      ['My all',     100],
      ['My all',     100],
      ['My all',     100],
      ['My all',     100],
    ]
    console.log(arrValues)
    console.log(p)
    var data = google.visualization.arrayToDataTable(arrValues);

    var options = {
      pieHole: 0.5,
      pieSliceTextStyle: {
        color: 'black',
      },
      legend: 'none'
    };

    var chart = new google.visualization.PieChart(document.getElementById('piechart'));
    chart.draw(data, options);
  }
