import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/api"
});

export const fetchRaw = () => API.get("/raw-data");
export const fetchProcessed = () => API.get("/processed-data");
export const fetchSummary = () => API.get("/summary");
export const fetchStatus = () => API.get("/status");
export const fetchConsistency = () => API.get("/consistency-check");
export const fetchEncoding = () => API.get("/categorical-encoding");
export const fetchAnalysis = () => API.get("/analysis");
export const fetchProfile = () => API.get("/profile");