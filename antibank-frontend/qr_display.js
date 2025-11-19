function QRDisplay(qrDataUrl, payload) {
  return `
    <div class="card">
      <h3>Scan with Pi Wallet</h3>
      <img src="${qrDataUrl}" alt="qr" style="width:260px;height:260px;border-radius:8px;" />
      <div style="margin-top:8px;">
        <div>Invoice: <code>${payload.invoiceId}</code></div>
        <div>Fiat: ${payload.fiatAmount} ${payload.currency}</div>
        <div>Pi: ${Number(payload.piAmount).toFixed(8)} π</div>
      </div>
    </div>
  `;
}
