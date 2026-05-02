import { useEffect, useState } from "react";
import { fetchConsistency } from "../services/api";

export default function ConsistencyTable() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchConsistency()
      .then(res => setData(res.data.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="card">
      <h2>🔁 Pipeline Consistency</h2>
      <table>
        <thead>
          <tr>
            <th>Run</th>
            <th>Shape</th>
            <th>Missing</th>
            <th>Mean</th>
            <th>Std</th>
          </tr>
        </thead>
        <tbody>
          {data.map((row, i) => (
            <tr key={i}>
              <td>{row.run}</td>
              <td>{row.shape.join(", ")}</td>
              <td>{row.missing_values}</td>
              <td>{row.mean.toFixed(2)}</td>
              <td>{row.std.toFixed(2)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}