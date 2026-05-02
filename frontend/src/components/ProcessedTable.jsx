import { useEffect, useState } from "react";
import { fetchProcessed } from "../services/api";

export default function ProcessedTable() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchProcessed()
      .then(res => {
        setData(res.data.data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setError("Failed to load processed data");
        setLoading(false);
      });
  }, []);

  if (loading) return <p>⏳ Loading Processed Data...</p>;
  if (error) return <p>❌ {error}</p>;

  return (
    <div>
      <h2>⚙️ Processed Data</h2>
      <table border="1">
        <thead>
          <tr>
            <th>Coin</th>
            <th>Price</th>
            <th>Category</th>
          </tr>
        </thead>
        <tbody>
          {data.map((row, i) => (
            <tr key={i}>
              <td>{row.coin_id}</td>
              <td>{row.price}</td>
              <td>{row.price_category}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}