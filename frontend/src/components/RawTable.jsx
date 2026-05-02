import { useEffect, useState } from "react";
import { fetchRaw } from "../services/api";

export default function RawTable() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchRaw()
      .then(res => {
        setData(res.data.data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setError("Failed to load raw data");
        setLoading(false);
      });
  }, []);

  if (loading) return <p>⏳ Loading Raw Data...</p>;
  if (error) return <p>❌ {error}</p>;

  return (
    <div>
      <h2>📥 Raw Data</h2>
      <table border="1">
        <thead>
          <tr>
            <th>Coin</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>
          {data.map((row, i) => (
            <tr key={i}>
              <td>{row.coin_id}</td>
              <td>{row.price}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}