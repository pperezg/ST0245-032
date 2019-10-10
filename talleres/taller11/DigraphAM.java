import java.util.ArrayList;

public class DigraphAM extends Graph
{
    int [][] matrix;
    public DigraphAM(int size)
    {
        super(size);
        matrix = new int[size][size];
    }
    public int getWeight(int source, int destination)
    {
        return matrix[source][destination];
    }

    public void addArc(int source, int destination, int weight)
    {
        matrix[source][destination]=weight;
    }

    public ArrayList<Integer> getSuccessors(int vertex)
    {
        ArrayList<Integer> a = new ArrayList<Integer>();
        for(int i = 0; i<size; i++) {
            if(matrix[vertex][i] != 0) {
                a.add(matrix[vertex][i]);
            }
        }
        return a;
    }
}