import java.util.*;
import java.io.*;

public class punto1_3 {

    public void cola (Queue<String> neveras, Stack<String> solicitudes){
        
        while(!neveras.isEmpty() && !solicitudes.empty()){
            String nev = neveras.poll();
            String sol = solicitudes.pop();
            System.out.println("Entregar la nevera "+ nev + " al cliente " + sol);
        }
    }
}
