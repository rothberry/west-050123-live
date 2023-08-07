const bubbleSort = (arr) => {
	// iterate through the arr
	//  compare the current element vs the next element
	//    if the current is bigger
	//      then we swap
	// go through swapping until the array is Fully sorted

	let swapped = false
	let counter = 0

	for (let i = 0; i < arr.length; i++) {
		swapped = false
		for (let j = 0; j < arr.length - 1 - i; j++) {
			counter++
			// console.log({ i, j, cur: arr[j], next: arr[j + 1] })
			if (arr[j] > arr[j + 1]) {
				console.log("swap")
				// * Javascript Swap
				// [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]
				// * Any language swap
				let temp = arr[j]
				arr[j] = arr[j + 1]
				arr[j + 1] = temp
				swapped = true
			}
		}
		console.log(arr)

		if (!swapped) {
			break
		}
	}
	console.log(`DONE with ${counter} operations`)
	return arr
}

const testDotSort = (arr) => {
	return arr.sort((a, b) => {
		console.log({ a, b })
		return a - b
	})
}

console.clear()
console.log("TESTING...")
// console.log(testDotSort([4, 3, 2, 1]))
// console.log(testDotSort([1, 2, 3, 4]))

console.log(bubbleSort([4, 3, 2, 1]))
console.log(bubbleSort([1, 2, 3, 4]))
let length = 100
console.log(
	bubbleSort(Array.from({ length }, () => Math.floor(Math.random() * length)))
)
