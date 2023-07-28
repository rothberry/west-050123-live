/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */

const merge1 = (nums1, nums2) => {
	// ! FIRST
	// ? ASSUME:
	//  no trailing zeros
	// Combine both arrays into nums1 
	// run sort algo on array
	// return nums1
	// Space O(1) / Time O(n*log(n))
	nums1.push(...nums2)
	return nums1.sort()
}

const merge2 = (nums1, m, nums2, n) => {
	// ! SECOND
	// ? ASSUME:
	//  can make new array,
	//  no trailing zeros
	// create new array
	// iterate m + n times
	//  whichever ele is smaller
	//    push into output
	//    increase idx of the one we added
	// return output
	// Space O(n) / Time O(n+m)
	
	// let out = new Array(m + n, or nums1.length)
	let out = []
	let i = 0,
	j = 0
	while (i < m || j < n) {
		let ele1 = nums1[i]
		let ele2 = nums2[j]
		if (ele1 <= ele2) {
			out.push(ele1)
			i++
		} else {
			out.push(ele2)
			j++
		}
	}
	return out
}

const merge3 = (nums1, m, nums2, n) => {
	// ! Third
	// Merge in place 2 pointer
	// 1 idx for nums1, 1 for nums2
	// iterate up to m + n
	// for each
	// 	if the nums1[i] is less nums2[j]
	// 		continue and increase i
	// 	if the nums2[j] is less nums1[i]
	// 		insert nums2[j]
	// 		pop off a zero
	// 		continue and increase j
	// return nothing!
	// Space O(1) / Time O(n+m)


}

console.clear()
console.log("TESTING...\n")

console.log(merge1([1, 2, 3], [2, 5, 6]))
console.log(merge2([1, 2, 3], 3, [2, 5, 6], 3))
console.log(merge2([1, 2, 3, 3, 3], 5, [2, 5, 6], 3))
