const Header = ({ isDarkMode, setIsDarkMode }) => {

	const handleClick = () => setIsDarkMode(!isDarkMode)

	const buttonTextContent = isDarkMode ? "Dark Mode" : "Light Mode"

	return (
		<header>
			<h1>
				<span className="logo">{"//"}</span>
				Project Showcase
			</h1>
			<div className="navigation">
				<button>All Projects</button>
				<button>Add Project</button>
			</div>
			<button onClick={handleClick}>{buttonTextContent}</button>
		</header>
	)
}

export default Header
