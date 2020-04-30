public class Solution
{
    public bool CanJump(int[] nums)
    {
        int furthest = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            if (i > furthest)
            {
                return false;
            }
            if (i + nums[i] > furthest)
            {
                furthest = i + nums[i];
            }
        }
        return true;
    }
}