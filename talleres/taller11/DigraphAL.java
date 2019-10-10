import java.util.ArrayList;
import java.util.LinkedList;
public class DigraphAL extends Graph
{

    ArrayList<LinkedList<Pair>> list = new ArrayList<>();
    
    public DigraphAL(int size)
    {
        super(size);
        for(int i=0; i<size;i++){
            list.add(new LinkedList());
        }
    }

    public void addArc(int source, int destination, int weight)
    {
        Pair pair = new Pair(destination, weight);
        LinkedList<Pair> a = list.get(source);
        a.add(pair);
        list.add(source, a);
    }

    public int getWeight(int source, int destination)
    {
        LinkedList<Pair> a = list.get(source);
        for(int i=0;i<a.size();i++){
            if(a.get(i).getvertice() == destination){
                return a.get(i).getpeso();
            }
            break;
        }
        return 0;
    }

    public ArrayList<Integer> getSuccessors(int vertice)
    {
        LinkedList<Pair> a = list.get(vertice);
        ArrayList<Integer>sucesor = new ArrayList<>();
        for(int i=0; i<a.size();i++){
            if(a.get(i).peso!=0){
                sucesor.add(a.get(i).vertice);
            }
        }
        return sucesor;
    }
}