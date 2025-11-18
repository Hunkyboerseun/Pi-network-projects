import PriceCard from "./components/PriceCard";
import Simulator from "./components/Simulator";

export default function Home() {
  return (
    <main style={{ padding: 20 }}>
      <h1>AntiBank + Pi Engine</h1>
      <PriceCard />
      <Simulator />
    </main>
  );
}
