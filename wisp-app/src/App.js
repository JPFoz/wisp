import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import LineChartWind from "./components/LineChartWind.js";
import LineChartTemperature from "./components/LineChartTemperature.js";
import LineChartPressure from "./components/LineChartPressure.js";
import LineChartHuimdity from "./components/LineChartHumidity";

class App extends Component {
    constructor(props){
        super(props);
        this.state = {
            results: [],
        };
    }

    render(){
        return [
        <li key="one"><LineChartHuimdity/></li>,
        <li key="two"><LineChartPressure/></li>,
        <li key="three"><LineChartTemperature/></li>,
        <li key="four"><LineChartWind/></li>];
    }
}

export default App;
