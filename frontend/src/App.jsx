function App() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center max-w-sm w-full mx-auto px-6 text-center">
      <h1 className="text-4xl font-bold text-gray-800">又活了一天</h1>
      <p className="text-sm text-gray-400 mt-1 mb-6">Another Day Alive</p>
      <p className="text-base text-gray-500 leading-relaxed mb-10">
        不管今天过得怎样，你还在这里。<br />
        这件事本身，就值得被看见。
      </p>
      <button
        className="py-3 px-7 bg-green-700 hover:bg-green-800 text-white rounded-lg cursor-pointer"
        onClick={() => alert("打卡功能还没做好，但你点了，说明你来了。")}
      >
        今天也打卡了
      </button>
    </div>
  );
}

export default App;
