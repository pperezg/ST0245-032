public boolean groupSum6(int start, int[] nums, int target) {
    if (start==nums.length){
      if (target==0){
        return true;
      } else {
        return false;
      }
    } else if (nums[start]==6){
      return (groupSum6(start+1, nums, target-nums[start]));
    } else {
      return (groupSum6(start+1, nums, target-nums[start]) || groupSum6(start+1, nums, target));
    }
  }

  public boolean groupNoAdj(int start, int[] nums, int target) {
    if (start==nums.length){
      if (target==0){
        return true;
      } else {
        return false;
      }
    } else if (start<nums.length-1){
      return (groupNoAdj(start+2, nums, target-nums[start]) || groupNoAdj(start+1, nums, target));
    } else {
      return (groupNoAdj(start+1, nums, target-nums[start]) || groupNoAdj(start+1, nums, target));
    }
  }

  public boolean groupSum5(int start, int[] nums, int target) {
    if (start==nums.length){
      if (target==0){
        return true;
      } else {
        return false;
      }
    } else if (nums[start]%5==0 && start<nums.length-1 &&nums[start+1]==1){
      return groupSum5(start+2, nums, target-nums[start]);
    } else if (nums[start]%5==0){
      return groupSum5(start+1, nums, target-nums[start]);
    } else {
      return (groupSum5(start+1,nums,target-nums[start]) || groupSum5(start+1,nums,target));
    }
  }

  public boolean groupSumClump(int start, int[] nums, int target) {
    if(start >= nums.length)
        return target == 0;
    int i = start;
    int sum = 0;
    while(i < nums.length && nums[start] == nums[i]) {
        sum += nums[i];
        i++;
    }
    if(groupSumClump(i, nums, target - sum))
        return true;
    if(groupSumClump(i, nums, target))
        return true;
    return false;
}

public boolean splitArray(int[] nums) {
    return splitArrayHelper(0, nums, 0, 0);
}

public boolean splitArrayHelper(int start, int[] nums, int group1, 
    int group2) {
    if(start >= nums.length)
        return group1 == group2;
            
    if(splitArrayHelper(start+1, nums, group1 + nums[start], group2))
        return true;
                      
    if(splitArrayHelper(start+1, nums, group1, group2 + nums[start]))
        return true;
                                
    return false;
}