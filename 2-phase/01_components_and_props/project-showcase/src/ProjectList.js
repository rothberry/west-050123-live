import React from "react"
import ProjectListItem from "./ProjectListItem"
// // import projects from "./projects.js"

// console.log(projects[0])
// const firstProj = projects[0]
// const secProj = projects[1]

const ProjectList = ({ projects }) => {
	// const { projects } = props
	// In order to display all the comps for each object in the `projects` array, we need to use .MAP instead of forEach
	// .forEach DOES NOT HAVE A RETURN
	// .map will return a list of all the Components

	const mappedProjectsFunc = () => {
		return projects.map((projectObj) => {
			return <ProjectListItem project={projectObj} key={projectObj.id} />
		})
	}

	const mappedProjectsFuncOneLineish = () =>
		projects.map((projectObj) => (
			<ProjectListItem project={projectObj} key={projectObj.id} />
		))

	const mappedProjects = projects.map((projectObj) => {
		return <ProjectListItem project={projectObj} key={projectObj.id} />
	})

	const mappedProjectsOneLiner = projects.map((projectObj) => (
		<ProjectListItem project={projectObj} key={projectObj.id} />
	))

	return (
		<div id="project-list">
			<h1>Projects?</h1>
			{/* <ProjectListItem project={firstProj}/>
			<ProjectListItem project={secProj}/> */}
			{/* <div id={firstProj.id}>
				<h1>{firstProj.name}</h1>
				<img
					src={firstProj.image}
					alt={firstProj.name}
					width="500"
					height="300"
				/>
				<p>{firstProj.about}</p>
			</div> */}
			{/* {mappedProjectsFunc()} */}
			{/* {mappedProjectsFuncOneLineish()} */}
			{/* {mappedProjects} */}
			{mappedProjectsOneLiner}
		</div>
	)
}
export default ProjectList
