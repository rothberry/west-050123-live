/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const isAnagram = (s, t) => {
	// ! first
	// sort both strings
	// return if they are exactly equal

	// let sSort = s.split("").sort().join("")
	// let tSort = t.split("").sort().join("")
	// return sSort === tSort

	// ! Second
	// create a counter obj
	// loop the length of the strings
	//  for each loop
	//    at the s idx ADD to the counter obj
	//    at the t idx subtract to the counter obj
	// after the loop
	//  check of all entires are zero

	// outliers => if s and t are not the same length return false

	if (s.length !== t.length) {
		return false
	}

	let obj = {}

	for (let i = 0; i < s.length; i++) {
		const sEle = s[i]
		const tEle = t[i]
		// add sEle
		obj[sEle] ? (obj[sEle] += 1) : (obj[sEle] = 1)
		console.log({ sEle, add: obj })
		obj[tEle] ? (obj[tEle] -= 1) : (obj[tEle] = -1)
		console.log({ tEle, sub: obj }, "\n")
	}

	return Object.values(obj).every((x) => x === 0)
}

console.clear()

console.log("TESTING....\n")
let s = "anagram"
let t = "nagaram"
console.log({ s, t, sol: isAnagram(s, t) })

s = "ooooo"
t = "uuuuu"
console.log({ s, t, sol: isAnagram(s, t) })

s = "rat"
t = "car"
console.log({ s, t, sol: isAnagram(s, t) })
