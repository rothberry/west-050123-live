import React, { useState } from "react"

const Header = ({ isDarkMode, setIsDarkMode }) => {
	// ? IN JS Events
	// Find the button; addEventListener("click", clickEventFunc)

	// SYNTAX
	// First => Define the State Variable
	// Next =>  define the SETTER FUNCTION
	// WE NEVER MODIFY THE STATE VAR DIRECTLY,
	// You must allow use the setter function to SET the new value
	// REACT will only see the change in State if it runs through the setter function
	// Setter functions areeeeeee ASYNCHRONOUS
	// Then => useState hook
	// Lastly => define the inital state

	// state = newState ❌
	// setState(newState) ✅
	// const [state, setterFunc] = useState(initialState)
	// * Lifted into App
	// const [isDarkMode, setIsDarkMode] = useState(true)

	const toggleDarkMode = (e) => {
		// console.log(isDarkMode)
		// setState(newState) => will overwrite state
    // console.log(isDarkMode)
		setIsDarkMode(!isDarkMode)
    // console.log(isDarkMode)
    // something that uses the isDarkmode, will be behind
		// setState((previousState) => { return newState })
		// setIsDarkMode(prevState => !prevState)
	}

	const whichMode = () => {
		// isDarkMode of true ? then "Dark Mode"
		// isDarkMode of false ? then "Light Mode"
		if (isDarkMode) {
			return "Dark"
		} else {
			return "Light"
		}
	}

	return (
		<header>
			<h1>
				<span className="logo">{"//"}</span>
				Project Showcase
			</h1>
			{/* <button onClick={(e) => console.log(e.target)}>Dark Mode</button> */}
			<button onClick={toggleDarkMode}>
				{isDarkMode ? "Dark" : "Light"} Mode
			</button>
		</header>
	)
}

export default Header
