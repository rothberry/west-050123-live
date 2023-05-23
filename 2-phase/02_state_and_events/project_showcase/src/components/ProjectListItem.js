import { useState } from "react"

const ProjectListItem = (props) => {
	const [clapCount, setClapCount] = useState(0)
	// const clapCount = 0

	const handleClaps = (e) => {
		// when this button is clicked, increase the clapCount by 1
		// setClapCount(clapCount + 1)
		setClapCount((prevState) => prevState + 1)
	}

	return (
		<li className="card">
			<figure className="image">
				<img src={props.project.image} alt={props.project.name} />
				{/* <button className="claps" onClick={() => setClapCount(clapCount + 1)}> */}
				<button className="claps" onClick={handleClaps}>
					👏{clapCount}
				</button>
			</figure>

			<section className="details">
				<h4>{props.project.name}</h4>
				<p>{props.project.about}</p>
				{props.project.link ? (
					<p>
						<a href={props.project.link}>Link</a>
					</p>
				) : null}
			</section>

			<footer className="extra">
				<span className="badge blue">Phase {props.project.phase}</span>
			</footer>
		</li>
	)
}

export default ProjectListItem
