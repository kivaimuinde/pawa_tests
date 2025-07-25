const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export async function sendQuery(question: string, sessionId = "default") {
  const res = await fetch(`${API_BASE}/api/v1/query?session_id=${sessionId}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question }),
  });

  if (!res.ok) {
    throw new Error("Failed to fetch AI response");
  }

  return res.json();
}

export async function fetchHistory(sessionId = "default") {
  const res = await fetch(`${API_BASE}/api/v1/history?session_id=${sessionId}`);

  if (!res.ok) {
    throw new Error("Failed to fetch history");
  }

  return res.json();
}
