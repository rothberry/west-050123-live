import Header from "./Header.js"
import Form from "./Form.js"
import ProjectList from "./ProjectList"
import projects from "./projects.js"

// console.log(projects)
const App = () => {

	// In order to have the Header DYNAMICALLY render the amount of projects without re-importing all the projects, we need to PASS DOWN THE AMOUNT AS **PROPS**
	return (
		<div>
			{/* pass down the `amount` of props to header */}
			<Header amount={projects.length} otherThing={"waooow"}/>
			<Form />
			<ProjectList projects={projects}/>
		</div>
	)
}

export default App
