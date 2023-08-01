import { useState } from "react"
import "./App.css"
import { Route, Routes } from "react-router-dom"
import PicForm from "./PicForm"
import Home from "./Home"
import PictureContainer from "./PictureContainer"

function App() {
	const [pictures, setPictures] = useState([])
	const [picture, setPicture] = useState({})

	return (
		<>
			<Routes>
				<Route path="/new-picture" element={<PicForm />} />
				<Route path="/pictures" element={<PictureContainer />} />
				<Route path="/" element={<Home picture={picture} />} />
			</Routes>
		</>
	)
}

export default App
