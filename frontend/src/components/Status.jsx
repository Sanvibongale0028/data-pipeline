import { useEffect, useState } from "react";
import { fetchStatus } from "../services/api";

export default function Status() {
  const [status, setStatus] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchStatus()
      .then(res => {
        setStatus(res.data.data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setError("Failed to fetch status");
        setLoading(false);
      });
  }, []);

  if (loading) return <p>⏳ Checking Status...</p>;
  if (error) return <p>❌ {error}</p>;

  return (
    <div>
      <h2>📌 Status</h2>
      <p>Raw: {status.raw_exists ? "✅" : "❌"}</p>
      <p>Processed: {status.processed_exists ? "✅" : "❌"}</p>
    </div>
  );
}