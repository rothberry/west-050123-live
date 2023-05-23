import { useState } from "react"
import Header from "./components/Header"
import ProjectForm from "./components/ProjectForm"
import ProjectList from "./components/ProjectList"

import projects from "./projects"

/* 
  1. What are props?
  - Properties
  - Just an Object that we pass down from parent to child
  - <Header key={value} />
    - props.key => value

  2. What data can you pass down as props?
  - Anything!
    - <Test string={strings} array={[]} obj={obj} func={() => doSomething}
    - props.func()

  2.5 Why must we use arrow functions when passing function down as props?
    - Arrow function BINDs itself to the component that it was defined in
*/

/* 
  !STATE!
  1. What is State in React?
  - Dynamic Variables
  - State is variables that can change
  - When there's a change in State, that's when react will trigger a re-render of that component tree
    - State change in App => everything re-renders
    - State change in ProjectList => just the List Items and List
  - State needs to live in the LOWEST POSSIBLE COMPONENT

*/

const App = () => {
	// light/dark mode function toggle thingy
	const [isDarkMode, setIsDarkMode] = useState(true)

	return (
		<div className={`App${isDarkMode ? "" : " light"}`}>
			<Header isDarkMode={isDarkMode} setIsDarkMode={setIsDarkMode} />
			{/* <ProjectForm /> */}
			<ProjectList projects={projects} />
		</div>
	)
}

export default App
