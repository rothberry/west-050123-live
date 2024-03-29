import styled from "styled-components"
import ProductionCard from "./ProductionCard"
import { useContext } from "react"
import { Context } from "../contexts/Context"

function ProductionContainer(/* { productions } */) {
	const { productions } = useContext(Context)
	return (
		<div>
			<Title>
				<span>F</span>latIron Theater <span>C</span>ompany
			</Title>
			<CardContainer>
				{productions.map((production) => (
					<ProductionCard key={production.id} production={production} />
				))}
			</CardContainer>
		</div>
	)
}

export default ProductionContainer

const Title = styled.h1`
	text-transform: uppercase;
	font-family: Arial, sans-serif;
	width: 70px;
	font-size: 70px;
	line-height: 0.8;

	transform: scale(0.7, 1.4);

	span {
		color: #42ddf5;
	}
`

const CardContainer = styled.ul`
	display: flex;
	flex-direction: column;
`
