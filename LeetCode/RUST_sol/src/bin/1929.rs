impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = vec![0; nums.len()*2];
        for i in (0..nums.len()){
            ans[i] = nums[i];
            ans[i+nums.len()] = nums[i];
        }
        return ans;
    }
}