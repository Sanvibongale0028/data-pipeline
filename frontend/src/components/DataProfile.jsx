// import { useEffect, useState } from "react";
// import { fetchProfile } from "../services/api";

// export default function DataProfile() {
//   const [data, setData] = useState(null);

//   useEffect(() => {
//     fetchProfile()
//       .then(res => setData(res.data.data))
//       .catch(err => console.error(err));
//   }, []);

//   if (!data) return <p>⏳ Loading Profile...</p>;

//   const renderTable = (title, dataset) => (
//     <div className="card">
//       <h2>{title}</h2>

//       <p><b>Rows:</b> {dataset.rows}</p>
//       <p><b>Columns:</b> {dataset.columns}</p>

//       <table>
//         <thead>
//           <tr>
//             <th>Column</th>
//             <th>Type</th>
//             <th>Unique</th>
//             <th>Missing</th>
//             <th>Stats</th>
//           </tr>
//         </thead>
//         <tbody>
//           {dataset.details.map((col, i) => (
//             <tr key={i}>
//               <td>{col.column}</td>
//               <td>{col.dtype}</td>
//               <td>{col.unique}</td>
//               <td>{col.missing}</td>
//               <td>
//                 {col.mean !== undefined ? (
//                   <>
//                     Mean: {col.mean.toFixed(2)} <br />
//                     Median: {col.median.toFixed(2)} <br />
//                     Min: {col.min} <br />
//                     Max: {col.max}
//                   </>
//                 ) : (
//                   <>
//                     Mode: {col.mode} <br />
//                     Top: {JSON.stringify(col.top_values)}
//                   </>
//                 )}
//               </td>
//             </tr>
//           ))}
//         </tbody>
//       </table>
//     </div>
//   );

//   return (
//     <div>
//       <h1>📊 Data Profile</h1>

//       <div className="grid">
//         {renderTable("📥 Raw Data", data.raw)}
//         {renderTable("⚙️ Processed Data", data.processed)}
//       </div>
//     </div>
//   );
// }

import { useEffect, useState } from "react";
import { fetchProfile } from "../services/api";

export default function DataProfile({ type }) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchProfile()
      .then(res => {
        console.log("PROFILE RESPONSE:", res.data); // 🔍 debug
        setData(res.data.data);
      })
      .catch(err => {
        console.error(err);
        setError("Failed to load profile");
      });
  }, []);

  // 🔹 Loading
  if (!data) return <p>⏳ Loading Profile...</p>;

  // 🔹 Error
  if (error) return <p>❌ {error}</p>;

  // 🔹 Safe dataset selection
  const dataset = type === "raw" ? data?.raw : data?.processed;

  if (!dataset) {
    return <p>⚠️ No dataset available</p>;
  }

  if (!dataset.details || !Array.isArray(dataset.details)) {
    return <p>⚠️ Invalid data format</p>;
  }

  return (
    <div className="card">
      <h2>
        {type === "raw"
          ? "📥 Raw Data Profile"
          : "⚙️ Processed Data Profile"}
      </h2>

      <p><b>Rows:</b> {dataset.rows ?? "-"}</p>
      <p><b>Columns:</b> {dataset.columns ?? "-"}</p>

      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>Column</th>
              <th>Type</th>
              <th>Unique</th>
              <th>Missing</th>
              <th>Mean</th>
              <th>Median</th>
              <th>Min</th>
              <th>Max</th>
              <th>Mode</th>
            </tr>
          </thead>

          <tbody>
            {dataset.details.map((col, i) => (
              <tr key={i}>
                <td>{col.column}</td>
                <td>{col.dtype}</td>
                <td>{col.unique}</td>

                <td style={{ color: col.missing > 0 ? "red" : "black" }}>
                  {col.missing ?? "-"}
                </td>

                <td>{col.mean !== undefined ? col.mean.toFixed(2) : "-"}</td>
                <td>{col.median !== undefined ? col.median.toFixed(2) : "-"}</td>
                <td>{col.min ?? "-"}</td>
                <td>{col.max ?? "-"}</td>
                <td>{col.mode ?? "-"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}