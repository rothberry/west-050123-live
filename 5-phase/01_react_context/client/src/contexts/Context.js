import { createContext, useEffect, useState } from "react"

export const Context = createContext()

const ContextProvider = (props) => {
	const [productions, setProductions] = useState([])
	const [currentUser, setUser] = useState(null)
	const [productionEdit, setProductionEdit] = useState([])

	const addProduction = (production) =>
		setProductions((current) => [...current, production])

	const updateProduction = (updated_production) =>
		setProductions((productions) =>
			productions.map((production) =>
				production.id == updated_production.id ? updated_production : production
			)
		)
	const deleteProduction = (deleted_production) =>
		setProductions((productions) =>
			productions.filter(
				(production) => production.id !== deleted_production.id
			)
		)

	const store = {
		testing: "test",
		productions: productions,
		setProductions,
		currentUser,
		setUser,
		productionEdit,
		setProductionEdit,
		addProduction,
		updateProduction,
    deleteProduction
	}

	return <Context.Provider value={store}>{props.children}</Context.Provider>
}

export default ContextProvider
