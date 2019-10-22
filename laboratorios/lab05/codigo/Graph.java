import java.util.ArrayList;

public abstract class Graph
{
   protected int size;
   public  Graph(int vertices) 
   {
       size = vertices;
   }

   public  abstract void addArc(int fuente, int destino, int peso);

   public abstract ArrayList<Integer> getSuccessors(int vertice);

   public abstract int getPeso(int fuente, int destino);

   public  int size() {
       return size;
    }
}