import { useState, useEffect } from "react"
import { Routes, Route } from "react-router"
import Home from "./components/Home"


const App = () => {
	return (
    <Routes>
      <Route path="/" element={<Home />}/>
    </Routes>
  )
}

export default App