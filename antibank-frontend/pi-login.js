// Loads the Pi SDK
const Pi = window.Pi;

export async function piLogin() {
  try {
    const scopes = ['username', 'payments'];
    
    const authResult = await Pi.authenticate(scopes, onIncompletePayment);

    return authResult;
  } catch (err) {
    console.error("Pi authentication failed:", err);
    return null;
  }
}

function onIncompletePayment(payment) {
  console.log("Incomplete Pi payment:", payment);
}
