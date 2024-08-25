/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    let indx1 = m - 1, indx2 = n - 1, currIndx = nums1.length - 1;

    while(indx1 >= 0 && indx2 >= 0){
        if(nums1[indx1] >= nums2[indx2]){
            nums1[currIndx] = nums1[indx1]
            indx1--
        }else{
            nums1[currIndx] = nums2[indx2]
            indx2--
        }
        currIndx--
    }

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