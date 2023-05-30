import { useState } from "react"

import Header from "./components/Header"
import ProjectContainer from "./components/ProjectContainer"
import ProjectForm from "./components/ProjectForm"



const App = () => {
	const [projects, setProjects] = useState([])
	const [isDarkMode, setIsDarkMode] = useState(true)

	const dark = isDarkMode ? "App" : "App light"

	return (
		<div className={dark}>
			<Header isDarkMode={isDarkMode} setIsDarkMode={setIsDarkMode} />
			<ProjectForm setProjects={setProjects} />
			<ProjectContainer projects={projects} setProjects={setProjects} />
		</div>
	)
}

export default App
