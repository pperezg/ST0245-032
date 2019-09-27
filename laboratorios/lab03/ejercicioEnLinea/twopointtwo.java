import java.util.*;
import java.io.*;

public class twopointtwo
{
    public static Stack<Integer>[] blocks;
    public static void createBlocks(int n){
        blocks = new Stack[n];
        for (int i=0; i<n;i++){
            blocks[i]= new Stack<Integer>();
            blocks[i].push(i);
        }
    }
    
    public static int locate(int a){
        int positionA = 0;
        for(int i=0; i<blocks.length;i++){
            if (blocks[i].search(a)!=-1){
                positionA = i;
            }
        }
        return positionA;
    }

    public static void moveAontoB(int a, int b){
        int locA = locate(a);
        int locB = locate(b);
        while(blocks[locA].search(a)!=1){
            int towards = blocks[locA].peek();
            blocks[towards].add(blocks[locA].pop());
        }
        while(blocks[locB].search(b)!=1){
            int towards = blocks[locB].peek();
            blocks[towards].add(blocks[locB].pop());
        }
        blocks[locB].push(blocks[locA].pop());
    }
    
    public static void moveAoverB(int a, int b){
        int locA = locate(a);
        int locB = locate(b);
        while(blocks[locA].search(a)!=1){
            int towards = blocks[locA].peek();
            blocks[towards].add(blocks[locA].pop());
        }
        blocks[locB].push(blocks[locA].pop());
    }
    
    public static void pileAontoB(int a, int b){
        int locA = locate(a);
        int locB = locate(b);
        while(blocks[locB].search(b)!=1){
            int towards = blocks[locB].peek();
            blocks[towards].add(blocks[locB].pop());
        }
        Stack<Integer> aux = new Stack<Integer>();
        while(blocks[locA].search(a)!=1){
            aux.push(blocks[locA].pop());
        }
        blocks[locB].push(blocks[locA].pop());
        while(!aux.empty()){
            blocks[locB].push(aux.pop());
        }
    }
    
    public static void pileAoverB(int a, int b){
        int locA = locate(a);
        int locB = locate(b);
        Stack<Integer> aux = new Stack<Integer>();
        while(blocks[locA].search(a)!=1){
            aux.push(blocks[locA].pop());
        }
        blocks[locB].push(blocks[locA].pop());
        while(!aux.empty()){
            blocks[locB].push(aux.pop());
        }
    }
    
    static void PrintStack(Stack<Integer> s)  
    {  
        if (s.isEmpty())  
            return;   
        int x = s.peek();
        s.pop();
        PrintStack(s); 
        System.out.print(x + " ");  
        s.push(x);  
    }  
    
    public static void main() throws FileNotFoundException {
        Scanner scn = new Scanner(new File("instrucciones.txt"));
        int n = Integer.parseInt(scn.nextLine());
        createBlocks(n);
        while(scn.hasNextLine()){
            String line = scn.nextLine();
            if(line.equals("quit")){
                break;
            }
            String[] dividedLine = line.split(" ");
            int a = Integer.parseInt(dividedLine[1]);
            int b = Integer.parseInt(dividedLine[3]);
            if(dividedLine[0].equals("move")){
                if (dividedLine[2].equals("onto")){
                    moveAontoB(a,b);
                } else if (dividedLine[2].equals("over")){
                    moveAoverB(a,b);
                }
            } else if (dividedLine[0].equals("pile")){
                if (dividedLine[2].equals("onto")){
                    pileAontoB(a,b);
                } else if (dividedLine[2].equals("over")){
                    pileAoverB(a,b);
                }
            }
        }
        
        for(int i=0;i<blocks.length;i++){
            System.out.print(i+": ");
            PrintStack(blocks[i]);
            System.out.println();
        }
    }
}
