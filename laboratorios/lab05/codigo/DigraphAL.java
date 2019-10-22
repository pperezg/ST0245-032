import java.util.ArrayList;
import java.util.LinkedList;
import javafx.util.Pair;

/**
 * This class is an implementation of digraphs using adjacency lists
 * 
 * @author Santiago Cartagena and Paulina Pérez
 */
public class DigraphAL extends Graph
{
    ArrayList<LinkedList<Pair1>> list = new ArrayList<>();
    public DigraphAL(int size)
    {
        super(size);
        for(int x = 0; x < size;x++){
            list.add(new LinkedList());
        }
    }

    public void addArco(int fuente, int destino, int peso)

    {
        Pair1 pair = new Pair1(destino, peso);
        LinkedList<Pair1> a = list.get(fuente);
        a.add(pair);
        list.add(fuente, a);
    }

    public int getPeso(int fuente, int destino)

    {
        LinkedList<Pair1> a = list.get(source);
        for(int z = 0;z < a.size();z++){
            if(a.get(z).vertice == destino){
                return a.get(z).peso;
            }
            break;
        }
        return 0;
    }

    public ArrayList<Integer> getSuccessors(int vertice)
    {
        LinkedList<Pair1> a = list.get(vertice);
        ArrayList<Integer>successors = new ArrayList<>();
        for(int y = 0; y < a.size();y++){
            if(a.get(y).peso!=0){
                successors.add(a.get(y).vertice);
            }
        }
        return successors;
    }
}