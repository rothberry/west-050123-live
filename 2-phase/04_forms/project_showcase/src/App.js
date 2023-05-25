import { useState } from "react"

import Header from "./components/Header"
import ProjectContainer from "./components/ProjectContainer"

const App = () => {
	const [isDarkMode, setIsDarkMode] = useState(true)

	const dark = isDarkMode ? "App" : "App light"

	return (
		<div className={dark}>
			<Header isDarkMode={isDarkMode} setIsDarkMode={setIsDarkMode} />
			<ProjectContainer />
		</div>
	)
}

export default App
