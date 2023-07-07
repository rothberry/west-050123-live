const Production = ({ title, genre, director, description, image }) => {
	return (
		<div>
			<hr />
			<h2>{title}</h2>
			<h2>{genre}</h2>
			<h2>{director}</h2>
			<img src={image} alt={title} />
			<p>{description}</p>
			<hr />
		</div>
	)
}

export default Production
