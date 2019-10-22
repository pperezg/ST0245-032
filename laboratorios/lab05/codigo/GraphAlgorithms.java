import java.util.ArrayList;

public class GraphAlgorithms
{
    public int MaxSuccessors(Graph successors, int vertice){
        ArrayList<Integer> a= successors.getSuccessors(vertice);
        int max= successors.getSuccessors(a.get(0)).size();
        for(int x = 1;x < a.size();x++){
            int aux = successors.getSuccessors(x).size();
            if(aux > max) max= aux;
        }
        return max;
    }
}