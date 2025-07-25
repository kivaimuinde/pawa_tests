"use client";

import { useEffect, useState } from "react";
import { sendQuery, fetchHistory } from "@/lib/api";
import Message from "./Message";
import Loader from "./Loader";
import { HistoryItem } from "@/types";

export default function ChatBox() {
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);
  const [messages, setMessages] = useState<HistoryItem[]>([]);
  const [error, setError] = useState<string | null>(null);
  const sessionId = "default"; // Can later use UUID or user ID

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!question.trim()) return;

    setLoading(true);
    setError(null);

    try {
      const response = await sendQuery(question, sessionId);
      setMessages((prev) => [...prev, { question, answer: response.answer }]);
      setQuestion("");
    } catch (err) {
      setError("Something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    const loadHistory = async () => {
      try {
        const data = await fetchHistory(sessionId);
        setMessages(data.history);
      } catch (err) {
        console.error("Failed to load history");
      }
    };

    loadHistory();
  }, []);

  return (
    <div className="max-w-2xl mx-auto mt-10 px-4">
      <h1 className="text-2xl font-bold mb-4 text-center">🌍 AI Travel Assistant</h1>
      <form onSubmit={handleSubmit} className="mb-4">
        <textarea
          className="w-full border rounded-lg p-3 text-sm resize-none"
          rows={4}
          placeholder="Ask a travel question..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />
        <button
          type="submit"
          className="mt-2 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition"
          disabled={loading}
        >
          {loading ? "Thinking..." : "Ask"}
        </button>
      </form>

      {error && <p className="text-red-500 mb-2">{error}</p>}
      {loading && <Loader />}

      <div>
        {messages.map((msg, idx) => (
          <Message key={idx} {...msg} />
        ))}
      </div>
    </div>
  );
}
