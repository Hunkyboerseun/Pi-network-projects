"use client";

import { Line } from "react-chartjs-2";
import { Chart as ChartJS, LineElement, CategoryScale, LinearScale, PointElement } from "chart.js";

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement);

export default function Chart({ data }) {
  const chartData = {
    labels: data.map(d => `Day ${d.day}`),
    datasets: [
      {
        label: "Pi Price",
        data: data.map(d => d.price),
        borderWidth: 2
      }
    ]
  };

  return (
    <div style={{ width: "100%", maxWidth: 800, marginTop: 20 }}>
      <Line data={chartData} />
    </div>
  );
}
