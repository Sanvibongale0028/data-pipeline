import { useEffect, useState } from "react";
import { fetchAnalysis } from "../services/api";

export default function DataAnalysis() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetchAnalysis()
      .then(res => setData(res.data.data))
      .catch(err => console.error(err));
  }, []);

  if (!data) return <p>⏳ Loading Analysis...</p>;

  const renderSection = (title, section) => (
    <div className="card">
      <h3>{title}</h3>

      {/* Missing Values */}
      <h4>❌ Missing Values</h4>
      <ul>
        {Object.entries(section.missing).map(([col, val]) => (
          <li key={col}>{col}: {val}</li>
        ))}
      </ul>

      {/* Range */}
      <h4>📏 Range</h4>
      <ul>
        {Object.entries(section.range).map(([col, val]) => (
          <li key={col}>
            {col}: {val.min} → {val.max}
          </li>
        ))}
      </ul>

      {/* Distribution */}
      <h4>📊 Distribution</h4>
      <ul>
        {Object.entries(section.distribution).map(([col, val]) => (
          <li key={col}>
            {col}: {JSON.stringify(val)}
          </li>
        ))}
      </ul>
    </div>
  );

  return (
    <div>
      <h2>📊 Data Analysis</h2>

      <div className="grid">
        {renderSection("📥 Raw Data", data.raw)}
        {renderSection("⚙️ Processed Data", data.processed)}
      </div>
    </div>
  );
}