function twoNumberSum(array, targetSum) {
    // Write your code here.
    for (let i = 0; i < array.length - 1; i++) {
      let x = array[i]
      if (x = targetSum)
      for (let j = 0; j < array.length; j++) {
        let y = array[j + 1 + i]
        if (x + y == targetSum) {
          console.log(`[${x}, ${y}]`)
        }
        
      }
    }
  }

  twoNumberSum([15], 15)