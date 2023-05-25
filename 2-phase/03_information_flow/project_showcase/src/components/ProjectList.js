import ProjectListItem from "./ProjectListItem"
import { useState } from "react"

const ProjectList = ({ projects }) => {
	// const [searchQuery, setSearchQuery] = useState("")

	// const searchResults = projects.filter((project) => {
	// 	return project.name.toLowerCase().includes(searchQuery.toLowerCase())
	// })

  // const handleOnChange = (e) => setSearchQuery(e.target.value)
	const projectListItems = projects.map((project) => (
		<ProjectListItem key={project.id} {...project} />
	))


	return <ul className="cards">{projectListItems}</ul>
}

export default ProjectList
