int canJump(int* nums, int numsSize) {
    int furthest = 0;
    for (int i = 0; i < numsSize; i++) {
        if (i > furthest) {
            return 0;
        }
        if (i + nums[i] > furthest) {
            furthest = i + nums[i];
        }
    }
    return 1;
}
