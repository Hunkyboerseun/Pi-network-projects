"use client";
import React, { useEffect, useState } from "react";

export default function PriceCard() {
  const [price, setPrice] = useState(null);
  const [supply, setSupply] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8000/api/rates")
      .then(r => r.json())
      .then(d => {
        setPrice(d.pi_price);
        setSupply(d.pi_supply);
      });
  }, []);

  return (
    <div style={{
      margin: "20px 0",
      padding: "15px",
      borderRadius: 8,
      border: "1px solid #ddd",
      width: 300
    }}>
      <h2>Current Pi Network Rate</h2>
      <p><b>Price:</b> ${price}</p>
      <p><b>Circulating:</b> {supply?.toLocaleString()} Pi</p>
    </div>
  );
}
