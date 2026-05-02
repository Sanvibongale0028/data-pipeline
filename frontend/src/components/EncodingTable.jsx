import { useEffect, useState } from "react";
import { fetchEncoding } from "../services/api";

export default function EncodingTable() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchEncoding()
      .then(res => setData(res.data.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="card">
      <h2>🔤 Categorical Encoding</h2>
      <table>
        <thead>
          <tr>
            <th>Column</th>
            <th>Before</th>
            <th>After</th>
          </tr>
        </thead>
        <tbody>
          {data.map((row, i) => (
            <tr key={i}>
              <td>{row.column}</td>
              <td>{row.before}</td>
              <td>{row.after}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}