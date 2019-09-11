import java.util.*;
import java.io.*;

public class punto1 {

public class Taller8 {


    public void cola (Queue<String> neveras, Stack<String> solicitudes){
        
        while(!neveras.isEmpty() && !solicitudes.empty()){
            String nev = neveras.poll();
            String sol = solicitudes.pop();
            System.out.println("Entregar la nevera "+ nev + " al cliente " + sol);
        }
    }
    
    public int polaca  (String string){
        Stack<Integer> stack = new Stack<Integer>();
        for (int i=0; i<string.length();i++){
            if (Character.isDigit(i)){
                stack.push(Integer.parseInt(String.valueOf(i)));
            } else {
                int a = stack.pop();
                int b = stack.pop();
                if (string.charAt(i)=='+'){
                    int c = a+b;
                    stack.push(c);
                } else if (string.charAt(i)=='-'){
                    int c = b-a;
                    stack.push(c);
                } else if (string.charAt(i)=='*'){
                    int c = a*b;
                    stack.push(c);
                } else if (string.charAt(i)=='/'){
                    int c = b/a;
                    stack.push(c);
                }
            }
        }
        return stack.pop();
    }
}
    
}
