import React from 'react';
import {Line as LineChart} from 'react-chartjs-2';
import Websocket from 'react-websocket';

function chartData(the_data, the_labels) {
  return {
    labels: the_labels,
    datasets: [
      {
        label: 'Wind Speed',
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

function extractPoints(response) {
    let arr = [];
    for (const item of response){
      arr.push(item.wind_speed)
    }
    return arr;
}

function extractLabels(response) {
    let arr = [];
    for (const item of response){
      arr.push(item.date_created)
    }
    return arr;
}

const options = {

  scaleShowGridLines: true,
  scaleGridLineColor: 'rgba(0,0,0,.05)',
  scaleGridLineWidth: 1,
  scaleShowHorizontalLines: true,
  scaleShowVerticalLines: true,
  bezierCurve: true,
  bezierCurveTension: 0.4,
  pointDot: true,
  pointDotRadius: 4,
  pointDotStrokeWidth: 1,
  pointHitDetectionRadius: 20,
  datasetStroke: true,
  datasetStrokeWidth: 2,
  datasetFill: true,

};

const styles = {
  graphContainer: {
    border: '1px solid black',
    padding: '15px'
  }
};

class LineChartWind extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      data: {}
    }
  }

  handleData(data) {
      let result = JSON.parse(data);
      this.setState({ data : chartData(extractPoints(result),extractLabels(result)) });
    };

  render() {
    return (
      <div style={styles.graphContainer}>
        <LineChart data={this.state.data}
          options={options}
          width="600" height="250"/>
        <Websocket url='ws://192.168.3.7:5000/wind'
              onMessage={this.handleData.bind(this)}/>
      </div>
    )
  }
}

export default LineChartWind;