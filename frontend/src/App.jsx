// import { useState } from "react";
// import "./App.css";

// import RawTable from "./components/RawTable";
// import ProcessedTable from "./components/ProcessedTable";
// import SummaryCard from "./components/SummaryCard";
// import Status from "./components/Status";
// import ConsistencyTable from "./components/ConsistencyTable";
// import EncodingTable from "./components/EncodingTable";
// import PriceChart from "./components/PriceCharts";
// import DataProfile from "./components/DataProfile";

// function App() {
//   const [view, setView] = useState("raw");

//   return (
//     <div className="container">

//       <h1>🚀 Data Preprocessing Dashboard</h1>

//       {/* Top Cards */}
//       <div className="grid">
//         <div className="card"><Status /></div>
//         <div className="card"><SummaryCard /></div>
//       </div>

//       {/* Toggle */}
//       <div className="button-group">
//         <button
//           className={view === "raw" ? "active" : ""}
//           onClick={() => setView("raw")}
//         >
//           📥 Raw Data
//         </button>
//         <button
//           className={view === "processed" ? "active" : ""}
//           onClick={() => setView("processed")}
//         >
//           ⚙️ Processed Data
//         </button>
//       </div>

//       {/* Table */}
//       <div className="card">
//         {view === "raw" ? <RawTable /> : <ProcessedTable />}
//       </div>

//       {/* Chart */}
//       <div className="card">
//         <PriceChart />
//       </div>

//       {/* Analytics */}
//       <div className="grid">
//         <ConsistencyTable />
//         <EncodingTable />
//       </div>

//       {/* Profile */}
//       <div className="section">
//         <DataProfile />
//       </div>

//     </div>
//   );
// }

// export default App;

import { useState } from "react";
import "./App.css";

import RawTable from "./components/RawTable";
import ProcessedTable from "./components/ProcessedTable";
import SummaryCard from "./components/SummaryCard";
import Status from "./components/Status";
import PriceChart from "./components/PriceCharts"; // ⚠️ FIX NAME
import DataProfile from "./components/DataProfile";

function App() {
  const [view, setView] = useState("raw");

  return (
    <div className="container">

      <h1>🚀 Data Preprocessing Dashboard</h1>

      {/* Top Cards */}
      <div className="grid">
        <div className="card"><Status /></div>
        <div className="card"><SummaryCard /></div>
      </div>

      {/* Toggle */}
      <div className="button-group">
        <button
          className={view === "raw" ? "active" : ""}
          onClick={() => setView("raw")}
        >
          📥 Raw Data
        </button>

        <button
          className={view === "processed" ? "active" : ""}
          onClick={() => setView("processed")}
        >
          ⚙️ Processed Data
        </button>
      </div>

      {/* TABLE */}
      {/* <div className="card">
        {view === "raw" ? <RawTable /> : <ProcessedTable />}
      </div> */}

      {/* CHART (optional: show only for processed) */}
      {view === "processed" && (
        <div className="card">
          <PriceChart />
        </div>
      )}

      {/* DATA PROFILE (ONLY THIS — dynamic) */}
      <div className="section">
        <DataProfile type={view} />
      </div>

    </div>
  );
}

export default App;