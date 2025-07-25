interface MessageProps {
  question: string;
  answer: string;
}

export default function Message({ question, answer }: MessageProps) {
  return (
    <div className="mb-4 p-4 border rounded-xl shadow bg-white">
      <p className="text-sm text-gray-600">🧍‍♂️ <strong>You:</strong> {question}</p>
      <p className="mt-2 text-sm text-gray-800 whitespace-pre-wrap"><strong>🤖 AI:</strong> {answer}</p>
    </div>
  );
}
