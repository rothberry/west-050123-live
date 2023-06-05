import { useState, useEffect } from "react"

import Header from "./components/Header"
import ProjectContainer from "./components/ProjectContainer"
import ProjectForm from "./components/ProjectForm"
import ProjectEditForm from "./components/ProjectEditForm"


const App = () => {
	const [projects, setProjects] = useState([])
	const [isDarkMode, setIsDarkMode] = useState(true)

	useEffect(() => {
		fetchAllProjects()
	}, [])

	const fetchAllProjects = () => {
		fetch("http://localhost:4000/projects")
			.then((res) => res.json())
			.then((projects) => setProjects(projects))
	}

	const onUpdateProjects = (updatedProject) => {
		setProjects((prevProj) =>
			prevProj.map((proj) =>
				proj.id === updatedProject.id ? updatedProject : proj
			)
		)
	}

	const onDeleteProject = (id) => {
		setProjects((prevProj) => prevProj.filter((proj) => id !== proj.id))
	}

	const dark = isDarkMode ? "App" : "App light"

	return (
		<div className={dark}>
			<Header isDarkMode={isDarkMode} setIsDarkMode={setIsDarkMode} />
			<ProjectForm setProjects={setProjects} />
			<ProjectEditForm
				editProject={projects[0]}
				onUpdateProjects={onUpdateProjects}
			/>
			<ProjectContainer
				projects={projects}
				onUpdateProjects={onUpdateProjects}
				onDeleteProject={onDeleteProject}
			/>
		</div>
	)
}

export default App
