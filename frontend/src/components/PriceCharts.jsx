import { useEffect, useState } from "react";
import { fetchProcessed } from "../services/api";
import {
  LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer
} from "recharts";

export default function PriceChart() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchProcessed()
      .then(res => setData(res.data.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="card">
      <h2>📈 Price Trend</h2>

      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="coin_id" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="price" strokeWidth={2} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}