import React from "react"

/* 
	From our projects.js data
	{
    id: 1,
    name: "Great Outdoors Guide",
    about: "Plan your next adventure to in the U.S. National Parks!",
    phase: 4,
    link: "https://great-outdoors-guide.netlify.app",
    image: "https://i.imgur.com/8GnP2Uw.png",
  },
*/

const ProjectListItem = (props) => {
	// console.log(props)
	return (
		<div>
			<h1>{props.project.name}</h1>
			<p>{props.project.about}</p>
			<img
				src={props.project.image}
				alt={props.project.name}
				width="500"
				height="300"
			/>
		</div>
	)
}

export default ProjectListItem
