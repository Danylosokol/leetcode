/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    console.log(nums1)
    console.log(nums2)
    let indx1 = m - 1, indx2 = n - 1, currIndx = nums1.length - 1;
    console.log(indx1, indx2, currIndx)
    while(indx1 >= 0 && indx2 >= 0){
        console.log("current indx1: ", indx1, nums1[indx1])
        console.log("current indx2: ", indx2, nums2[indx2])
        if(nums1[indx1] >= nums2[indx2]){
            console.log("setting nums1 element")
            console.log(nums1)
            nums1[currIndx] = nums1[indx1]
            indx1--
            console.log(nums1)
        }else{
            console.log("setting nums2 element")
            console.log(nums1)
            nums1[currIndx] = nums2[indx2]
            indx2--
            console.log(nums1)
        }
        currIndx--
    }
    console.log(indx1, indx2)
    console.log(nums1)
    while(indx1 >= 0 && currIndx >= 0){
        nums1[currIndx] = nums1[indx1]
        indx1--
        currIndx--
    }

    while(indx2 >= 0 && currIndx >= 0){
        nums1[currIndx] = nums2[indx2]
        indx2--
        currIndx--
    }
};