export const metadata = {
  title: "AntiBank Pi Engine",
  description: "Decentralized Pi Network financial simulator"
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body style={{ fontFamily: "Arial, sans-serif", margin: 0 }}>
        {children}
      </body>
    </html>
  );
}
