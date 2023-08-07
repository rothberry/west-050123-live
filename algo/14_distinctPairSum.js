// Given an input array and a target value k, return all distinct pairs of consecutive numbers that add up to k. A pair is distinct if no other pair contains the same numbers.

// The order of the pairs and order of the values in each pair does not matter, e.g. we consider [[2, 8], [7, 3]] to be the same as [[3, 7], [8, 2]].

// * FIRST
// create a pair tracking object
// iterate through arr
//  for each loop
	//  check if the current plus the next value is k
	//  AND check if we've already seen the current value in our obj
	//  AND check if we've already seen the NEXT value in our obj
	// 	Input into array as [lesserValue, greaterValue]
// After the loop return all the pairs as an array from the object
const distinctPairSum = (arr, k) => {

	const pairs = {}

	for (let i = 0; i < arr.length - 2; i++) {
		const current = arr[i]
		const next = arr[i + 1]
		const currentSum = current + next
		console.log({ current, next, currentSum })
		if (currentSum === k && !pairs[current] && !pairs[next]) {
			pairs[current] = [current, next]
			console.log(pairs)
		}
	}
	return Object.values(pairs)
}

console.clear()
console.log("TESTING>>>")
let arr1 = [0, 1, 1, 2, 0, 1, 1]
console.log(distinctPairSum(arr1, 2))
// Output: [[1, 1], [2, 0]]

let arr2 = [3, 4, 2, 1, 5, 2, 8, 2]
// [1,2,2,2,3,4,5,8]
console.log(distinctPairSum(arr2, 10))
// Output: [[2, 8]]

let arr3 = [1,1,1,2,2,2,3,4,2,1,4,4,5,23,5,5,3,5,12,10,5,5,25,3,5]
console.log(distinctPairSum(arr3, 5))
