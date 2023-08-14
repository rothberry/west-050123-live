/**
 * @param {number[]} nums
 * @return {number}
 * ? Given an integer array nums,
 * ? find the contiguous subarray (containing at least one number)
 * ? which has the largest sum and return its sum.
 * !DONE
 */

const maxSubArrayBruteForce = (nums) => {
	// Check every single sum available, choose the max
	// Loop over the array twice
	// Push the sum of i to j into an output array
	// return the max of the output array
	// ? Outliers
	// * if length is 1 return nums[0]

	let counter = 0
	let output = [...nums]
	for (let i = 0; i < nums.length; i++) {
		for (let j = i + 1; j < nums.length; j++) {
			let localSum = nums.slice(i, j).reduce((prev, cur) => {
				return prev + cur
			}, 0)
			counter++
			// console.log(localSum);
			output.push(localSum)
		}
	}
	console.log({ output, numsLength: nums.length, counter })
	return Math.max(...output)
}

const maxSubArray = (nums) => {
	// ! SECOND
	// * Kadane's Algo
	// * As we loop throught the arr, we are defining the max sum at that index
	// * Then when we move onto the next index, we just need to take the max of either the current element OR the prev max sum plus the current element

	// Create a starting sum of just the first element
	// Create an output array of all the max sums at index

	// loop over length of array
	// check max between current value and previous max + current value
	// max(current, prev + current) => new value
	// Return the max of the output array

	let prevSum = nums[0]
	let curMax = prevSum
	const outputArr = [prevSum]

	for (let endIdx = 1; endIdx < nums.length; endIdx++) {
		const current = nums[endIdx]
		prevSum = Math.max(current, prevSum + current)
		curMax = Math.max(curMax, prevSum)
		console.log({ endIdx, current, prevSum, nxt: prevSum + current, curMax })
		outputArr.push(prevSum)
	}
	// console.log(outputArr)
	// return Math.max(...outputArr)
	return curMax
}

// * Output: 6
// * Explanation: [4,-1,2,1] has the largest sum = 6.
const a1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
const a2 = [1, -3, 2, 1, -1]
let [length, min, max] = [10, -1000, 0]

const aRand = Array.from({ length }, () =>
	Math.floor(Math.random() * (max - min) + min)
)
console.clear()
console.log("TESTING...\n")
console.log(maxSubArray(a1))
console.log(maxSubArray(a2))
console.log(aRand)
console.log(maxSubArray(aRand))
// console.log(maxSubArrayBruteForce([1]));
