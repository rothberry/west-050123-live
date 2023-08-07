/**
 * @param {string} s
 * @return {boolean}
 * 
 * A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
 * 
 * Given a string s, return true if it is a palindrome, or false otherwise.


 */
var isPalindrome1 = function (s) {
	// ! FIRST
	// Assume there are NO SPACES and special characters don't count
	// ? We first would need to remove all the spaces and special characters
	// Reverse the string (O(N))
	// compare the reversed string to the original
	// return true if the same, false if not

	const betterString = s.replace(/[^A-Z0-9]/gi, "").toUpperCase()
	const revStr = betterString.split("").reverse().join("")
	// console.log({betterString, revStr})
	return revStr === betterString
}

const myReverse = (str) => {
	let splitStr = str.split("")
	let out = new Array(str.length)
	let i = str.length - 1
	while (i >= 0) {
		out[i](splitStr[i])
		i--
	}
	return out.join("")
}

const isPalindrome2 = (s) => {
	// ! SECOND
	// Have 2 trackers on the first (start) and last(end) index
	// loop
	//  Compare the start element to the end element
	//  if true
	//    move both indeces inward
	//    start idx plus one, end idx minus 1
	//  if false
	//    break loop and return false
	// if we successfully complete the loop return true

	const betterString = s.replace(/[^A-Z0-9]/gi, "").toUpperCase()
	let [left, right] = [0, betterString.length - 1]
	while (left < right) {
		let [leftEle, rightEle] = [betterString[left], betterString[right]]
		console.log({ left, leftEle, right, rightEle })
    if (leftEle === rightEle) {
      left++
      right--
    } else {
      return false
    }
	}
  return true
}

console.clear()
console.log("TESTING\n")
let [s1, s2, s3, s4, s5] = [
	"rar",
	"A man, a plan, a canal: Panama",
	"race a car",
	" ",
  "qwertyuiopJKHJFGSDKJGHKLAUSDGHLKASGKLSJGDFLSKJGDKLSFJGHLDSFJGHDLSFKJGHSL;DFJGHSDFKLJGHDFSKLJGHSDKLFJGDLSFKJGDLSKFJGDSFKLFJGDFLSKJGSDKLFJGHDSLKFJGHDFLSKJGHDKLSFJGHDFSKLJGHDKLSFJGHLDKSFJGHLSDFKJGHDLSFKJHGDFKLSJGHDLSKFGJHDFSKLJGHSDFKLJGHKSDLFJGHKLSDFJGHDKLSFFJHGLKSDFJGHDSKLFJGHKLSDFJGHGJFSDKLGFHJFSDGK"
]

console.log({ s1, return: isPalindrome2(s1) })
console.log({ s2, return: isPalindrome2(s2) })
console.log({ s3, return: isPalindrome2(s3) })
console.log({ s4, return: isPalindrome2(s4) })
console.log({ s5, return: isPalindrome2(s5) })
