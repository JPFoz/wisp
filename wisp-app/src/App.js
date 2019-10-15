import React, {Component} from 'react';
import './App.css';
import LineChartWind from "./components/LineChartWind.js";
import LineChartTemperature from "./components/LineChartTemperature.js";
import LineChartPressure from "./components/LineChartPressure.js";
import LineChartHuimdity from "./components/LineChartHumidity";

function chartData(chart_name, the_data, the_labels) {
  return {
    labels: the_labels,
    datasets: [
      {
        label: chart_name,
        fillColor: 'rgba(220,220,220,0.2)',
        strokeColor: 'rgba(220,220,220,1)',
        pointColor: 'rgba(220,220,220,1)',
        pointStrokeColor: '#fff',
        pointHighlightFill: '#fff',
        pointHighlightStroke: 'rgba(220,220,220,1)',
        data: the_data,
      },
    ]
  }
}

function extractData(response) {
    let data = {};
    let arrPressure = [];
    let arrHumidity = [];
    let arrTemperature = [];
    let labels = [];

    for (const item of response){
      arrPressure.push(item.pressure);
      arrHumidity.push(item.humidity);
      arrTemperature.push(item.temperature);
      labels.push(item.date_created)
    }
    data.pressure_data = chartData("Pressure", arrPressure,labels);
    data.humidity_data = chartData("Humidity", arrHumidity,labels);
    data.temp_data = chartData("Temperature", arrTemperature, labels);

    return data;
}

class App extends Component {
    constructor(props){
        super(props);
        this.state = {
            data: {}
        };
    }

    componentDidMount(){
      fetch("http://192.168.3.7:8080/passive_measurements")
            .then(response => response.json())
            .then(data => this.setState({ data : extractData(data.results) }));
    }

    render(){
        return [<li key="one"><LineChartWind/></li>,
        <li key="two"><LineChartHuimdity chartData={this.state.data.humidity_data}/></li>,
        <li key="three"><LineChartPressure chartData={this.state.data.pressure_data} /></li>,
        <li key="four"><LineChartTemperature chartData={this.state.data.temp_data} /></li>];
    }
}

export default App;
