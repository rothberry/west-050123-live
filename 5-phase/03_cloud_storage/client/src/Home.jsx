import React from "react"

const Home = ({ picture }) => {
	return (
		<div>
			id: {picture.public_id}
			<img src={picture.url} />
		</div>
	)
}

export default Home
