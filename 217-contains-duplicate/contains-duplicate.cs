public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        Array.Sort(nums);
        for(int i = 1; i < nums.Length; i ++){
            Console.WriteLine(nums[i]);
            if(nums[i] == nums[i - 1]){
                Console.WriteLine("duplicates:");
                Console.WriteLine(nums[i]);
                Console.WriteLine(nums[i - 1]);
                return true;
            }
        }
        return false;
    }
}