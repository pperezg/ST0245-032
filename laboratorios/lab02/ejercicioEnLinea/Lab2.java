
public class Lab2
{
    //  Array 2
    
    public int countEvens(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.length; i++)
            if (nums[i] % 2 == 0) count++;
        return count;
    }
    
    public int sum13(int[] nums) {
        int total = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 13) total += nums[i];
            else if (i <= nums.length - 1) i++;
        }
        return total;
    }
    
    public boolean only14(int[] nums) {
      for (int i = 0; i < nums.length; i++)
            if (nums[i] != 1 && nums[i] != 4) return false;
      return true;
    }
    
    public boolean isEverywhere(int[] nums, int val) {
        boolean result = true;
        for (int i = 0; i <=nums.length-2;i++){
            if ( (nums[i] != val) && (nums[i+1] != val))
            result = false;
        }
        return result;
    }
    
    public String[] fizzBuzz(int start, int end) {
        int k = end - start;
        String[] resultado = new String[k];
        int posicion = 0;
        for (int i = start; i < end; i++) {
            boolean fizz = i % 3 == 0;
            boolean buzz = i % 5 == 0;
          if (fizz && buzz) resultado[posicion] = "FizzBuzz";
            else if (fizz) resultado[posicion] = "Fizz";
            else if (buzz) resultado[posicion] = "Buzz";
            else resultado[posicion] = String.valueOf(i);
            posicion++;
        }
        return resultado;
    }
    
    // Array 3
    
    public int maxSpan(int[] nums) {
        int m = 0;
        for(int left = 0;left < nums.length; left++) {
          for(int right = left;right < nums.length;right++) {
            if(nums[left] == nums[right] && (right - left) + 1 > m) {
              m = right - left + 1;
            }
          }
        }
        return m;
    }
    
    public int[] fix34(int[] nums) {
      for (int i = 0; i < nums.length; i++)
            if (nums[i] == 3) {
                int temp = nums[i + 1];
                nums[i + 1] = 4;
                for (int j = i + 2; j < nums.length; j++)
                    if (nums[j] == 4) nums[j] = temp;
            }
        return nums;
    }
    
    public boolean canBalance(int[] nums) {
      int a = 0;
      int b = 0;
      for(int c = 0; c < nums.length; c++) {
        a += nums[c];
      }
      if(a == b) {
        return true;
      }
      for (int c = 0; c < nums.length; c++ ) {
        a -= nums[c];
        b += nums[c];
        if(a == b) {
          return true;
        }
      }
      return false;
    }
    
    public int[] squareUp(int n) {
      int[] result = new int[n * n];
      int x = n-1, pass = 1, index = 0;
      if(n == 0) { return result; }
      for(int i = n-1; i < result.length; i+=n) {
         index = i;
         for(int k = 1; k <= pass; k++) {
           if(k == 0) { break; }
           result[index] = k;
           index--;
         }
         pass++;
      }
      return result;
    }
    
    public int maxMirror(int[] nums) {
      int longitud = nums.length;
      int cuenta= 0;
      int m = 0;
      for (int i = 0; i < longitud; i++){
        cuenta=0;
        for (int j = longitud-1; i + cuenta < longitud && j > -1; j--){
          if(nums[i+cuenta] == nums[j]){
            cuenta++;
          }
          else{
            if (cuenta > 0){
              m = Math.max(cuenta,m);
              cuenta = 0;
            }
          }
        }
        m = Math.max(cuenta,m);
      }
      return m;
    }
}
