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
	return (
		<div>
			<h1>NAME</h1>
			<p>ABOUT</p>
			<img src="IMAGE" width="100" height="100" />
		</div>
	)
}

export default ProjectListItem
