public int factorial(int n) {
 if (n==1){
   return 1;
 } else {
   return (n*factorial(n-1));
 }
}

public int fibonacci(int n) {
  if (n==0 || n==1){
    return n;
  } else {
    return (fibonacci(n-1)+fibonacci(n-2));
  }
}

public int triangle(int rows) {
  if (rows==0){
    return 0;
  } else {
    return (rows+triangle(rows-1));
  }
}

public int sumDigits(int n) {
  if (n==0){
    return 0;
  } else {
    return (n%10 + sumDigits(n/10));
  }
}


public int countX(String str) {
  if(str.length()==0){
    return 0;
  } else {
    if (str.charAt(0)=='x'){
      return (1+countX(str.substring(1)));
    } else {
      return (countX(str.substring(1)));
    }
  }
}
