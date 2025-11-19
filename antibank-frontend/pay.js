export async function sendPiPayment(amount) {
  const payment = await window.Pi.createPayment({
    amount: amount,
    memo: "ANTIBANK Deposit",
    metadata: { type: "deposit" }
  });

  return payment;
}
