import React, { useState } from "react"

const PicForm = () => {
	const [formFile, setFormFile] = useState(null)
	const handleSubmit = (e) => {
		e.preventDefault()
		let formData = new FormData()
		formData.append("file", formFile)
		console.log(formData.get("file"))
		fetch("/upload", {
			method: "POST",
			headers: {
				"Content-Type": "multipart/form-data",
			},
      mode: "no-cors",
			body: formData,
		})
			.then((res) => res.json())
			.then(console.log)
			.catch((err) => console.log({ err }))
	}
	const handleChange = (e) => {
		const file = e.target.files[0]
		console.log(file)
		setFormFile(file)
	}

	return (
		<div>
			PicForm
			<form onSubmit={handleSubmit}>
				<label>
					Your pic: {"  "}
					<input type="file" onChange={handleChange} />
				</label>
				<input type="submit" value="ADD YOUR PIC" />
			</form>
		</div>
	)
}

export default PicForm
