import React from 'react';
import {Line as LineChart} from 'react-chartjs-2';

function chartData(the_data, the_labels) {
  return {
    labels: the_labels,
    datasets: [
      {
        label: 'Pressure',
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
      arr.push(item.pressure)
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

class LineChartPressure extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      data: {}
    }
  }

  componentDidMount(){
      fetch("http://127.0.0.1:8080/passive_measurements")
            .then(response => response.json())
            .then(data => this.setState({ data : chartData(extractPoints(data.results),extractLabels(data.results)) }));
    }

  render() {
    return (
      <div style={styles.graphContainer}>
        <LineChart data={this.state.data}
          options={options}
          width="600" height="250"/>
      </div>
    )
  }
}

export default LineChartPressure;