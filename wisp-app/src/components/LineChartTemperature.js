import React from 'react';
import {Line as LineChart} from 'react-chartjs-2';

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

class LineChartTemperature extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div style={styles.graphContainer}>
        <LineChart data={this.props.chartData}
          options={options}
          width="600" height="250"/>
      </div>
    )
  }
}

export default LineChartTemperature;