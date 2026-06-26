import React from "react";
import Upload from "./Upload";
import ChatHistory from "./ChatHistory";

function App() {
  return (
    <div>
      <h1>Health RAG Chatbot</h1>
      <Upload />
      <ChatHistory />
    </div>
  );
}

export default App;