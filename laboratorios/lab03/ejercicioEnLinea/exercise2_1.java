import java.util.*;
import java.util.LinkedList;

public class Exercise2.1
{
    public static void WritingMachine(String text){

        LinkedList <String> list = new LinkedList();
        String start = "";
        String end = "";
        int count = 0;
        for(int i = 0; i < text.length()-1; i++){
            if(text.charAt(i)=='[' && start == ""){
                start = "[";
                for(int j = i + 1; j < text.length(); j++){
                    if(text.charAt(j) == '[' || text.charAt(j) == ']'){
                        start = "";
                        count = 0;
                        break;
                    } else {
                        list.add(count, text.substring(j,j+1));
                        count++;
                        i++;
                    }
                }
            } else if(text.charAt(i)==']' && end == ""){
                end = "]";
                for(int k = i + 1 ; k < text.length(); k++){
                    if(text.charAt(k) == ']' || text.charAt(k) == '['){
                        end = "";
                        break; 
                    } else if(text.charAt(k) != ']'){
                        list.addLast(text.substring(k, k + 1));
                        i++;
                    } else {
                        i++;
                    }
                }
            } else {
                list.add(i, text.substring(i, i + 1));
            }
        }
        for(int x = 0; x < list.size(); x++){
            System.out.print(list.get(x));
        }
    }
}
