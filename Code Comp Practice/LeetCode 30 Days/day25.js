var canJump = function (nums) {
  let furthest = 0;
  for (let i = 0; i < nums.length; i++) {
    if (i > furthest) {
      return false;
    }
    if (i + nums[i] > furthest) {
      furthest = i + nums[i];
    }
  }
  return true;
};
