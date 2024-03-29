import React from "react"
import ReactDOM from "react-dom"

import App from "./App"
import { BrowserRouter as Router } from "react-router-dom"
import ContextProvider from "./contexts/Context"

ReactDOM.render(
	<Router>
		<ContextProvider>
			<App />
		</ContextProvider>
	</Router>,
	document.getElementById("root")
)
