import React, { useState } from "react"
import { useNavigate } from "react-router-dom"
import styled from "styled-components"

function Authentication({ setUser }) {
	const [signUp, setSignUp] = useState(false)
	const [name, setName] = useState("")
	const [email, setEmail] = useState("")
	const history = useNavigate()

	const handleClick = () => setSignUp((signUp) => !signUp)
	// 3.✅ Finish building the authentication form with formik
	// 3.1 handle the value, onchange and onsubmit of the form
	// 3.2 on submit create a POST.
	// 3.3 There is a button that toggles the component between login and sign up.
	// if signUp is true use the path '/users' else use '/login' (we will be writing login soon)
	// Complete the post and test our '/users' route
	// 3.4 On a successful POST add the user to state (setUser is passed down from app through props) and redirect to the Home page.
	// 4.✅ return to server/app.py to build the next route

	const handleAuth = (e) => {
		e.preventDefault()
		console.log({ name, email })
		const postReqObj = {
			method: "POST",
			headers: {
				"Content-type": "application/json",
			},
			body: JSON.stringify({ name, email }),
		}
		fetch(signUp ? "/users" : "/login", postReqObj)
			.then((res) => res.json())
			.then((newUser) => {
				console.log({ newUser })
				if (!newUser.errors) {
					setUser(newUser)
					history("/")
				} else {
					console.log(newUser.errors)
				}
			})
	}

	return (
		<>
			<h2 style={{ color: "red" }}> {"Errors Here!!"}</h2>
			<h2>Please Log in or Sign up!</h2>
			<h2>{signUp ? "Already a member?" : "Not a member?"}</h2>
			<button onClick={handleClick}>
				{signUp ? "Log In!" : "Register now!"}
			</button>
			<Form onSubmit={handleAuth}>
				<label>Username</label>
				<input
					type="text"
					name="name"
					value={name}
					onChange={(e) => setName(e.target.value)}
				/>
				{signUp && (
					<>
						<label>Email</label>
						<input
							type="email"
							name="email"
							value={email}
							onChange={(e) => setEmail(e.target.value)}
						/>
					</>
				)}
				<input type="submit" value={signUp ? "Sign Up!" : "Log In!"} />
			</Form>
		</>
	)
}

export default Authentication

export const Form = styled.form`
	display: flex;
	flex-direction: column;
	width: 400px;
	margin: auto;
	font-family: Arial;
	font-size: 30px;
	input[type="submit"] {
		background-color: #42ddf5;
		color: white;
		height: 40px;
		font-family: Arial;
		font-size: 30px;
		margin-top: 10px;
		margin-bottom: 10px;
	}
`
