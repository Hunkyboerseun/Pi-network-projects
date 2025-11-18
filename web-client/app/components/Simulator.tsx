"use client";

import React, { useState } from "react";
import Chart from "./Chart";

export default function Simulator() {
  const [output, setOutput] = useState([]);

  async function runSim() {
    const res = await fetch("http://localhost:8000/api/simulate", {
      method: "POST"
    });
    const data = await res.json();
    setOutput(data);
  }

  return (
    <div>
      <button
        style={{
          padding: "10px 20px",
          background: "#5a31f4",
          color: "#fff",
          border: "none",
          borderRadius: 5,
          cursor: "pointer"
        }}
        onClick={runSim}
      >
        Run Simulation
      </button>

      {output.length > 0 && <Chart data={output} />}
    </div>
  );
}
