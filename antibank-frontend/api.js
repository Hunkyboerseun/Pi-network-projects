// Simple client for ANTIBANK backend. Update BASE when backend URL changes.
const Api = (() => {
  const BASE = (location.origin.indexOf('localhost') !== -1) ? 'http://localhost:8000' : (location.origin.replace(/:\d+$/,'') + ':8000');

  async function post(path, body) {
    const res = await fetch(BASE + path, {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify(body)
    });
    return res.json().catch(()=>({ok:false}));
  }
  async function get(path) {
    const res = await fetch(BASE + path);
    return res.json().catch(()=>({ok:false}));
  }

  return {
    createInvoice: (body) => post('/api/invoices/create', body),
    createWallet: (body) => post('/api/fiat-wallets/create', body),
    topupWallet: (walletId, body) => post(`/api/fiat-wallets/${walletId}/topup`, body),
    getWallet: (walletId) => get(`/api/fiat-wallets/${walletId}`),
    getRate: (currency) => get(`/api/exchange/rates`)
  };
})();
