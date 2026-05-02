import { useEffect, useState } from "react";
import { fetchSummary } from "../services/api";

export default function SummaryCard() {
  const [data, setData] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchSummary()
      .then(res => {
        setData(res.data.data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setError("Failed to load summary");
        setLoading(false);
      });
  }, []);

  if (loading) return <p>⏳ Loading Summary...</p>;
  if (error) return <p>❌ {error}</p>;

  return (
    <div>
      <h2>📊 Summary</h2>
      <p>Total: {data.total_records}</p>
      <p>Avg: {data.avg_price}</p>
      <p>Max: {data.max_price}</p>
      <p>Min: {data.min_price}</p>
    </div>
  );
}

