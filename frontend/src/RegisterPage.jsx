import { useState } from "react";

function RegisterPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState(null);

  async function handleRegister() {
    const res = await fetch("http://localhost:8000/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    });

    if (res.ok) {
      setMessage("注册成功！");
    } else {
      setMessage("注册失败，请重试。");
    }
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center max-w-sm w-full mx-auto px-6">
      <h1 className="text-2xl font-bold text-gray-800 mb-6">注册</h1>

      <input
        className="w-full border rounded px-3 py-2 mb-3"
        placeholder="用户名"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        className="w-full border rounded px-3 py-2 mb-4"
        type="password"
        placeholder="密码"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <button
        className="w-full py-2 bg-green-700 hover:bg-green-800 text-white rounded"
        onClick={handleRegister}
      >
        注册
      </button>

      {message && <p className="mt-4 text-sm text-gray-500">{message}</p>}
    </div>
  );
}

export default RegisterPage;