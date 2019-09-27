import java.util.*;

public class BinaryTree {
  public Node root;
  public void insertar(int n) {
        insertarAux(root, n);
  }
  
  public void insertarAux(Node node, int n) {
      if(n < node.data && node.left == null){
            Node left = new Node(n);
            node.left = left;
      }else if(n < node.data){
            insertarAux(node.left, n);
      }else if(n > node.data && node.right == null){
            Node right = new Node(n);
            node.right = right;
      }else{
            insertarAux(node.right, n);
      }
  }
  
  public boolean buscar(int n) {
     return buscarAux(root, n);
  }
  
  public boolean buscarAux(Node node, int n) {
        if(node.data == n){
            return true;
        }
        
        if(node == null){
            return false;
        }
        
        if(n > node.data){
            return buscarAux(node.right, n);
        }else{
            return buscarAux(node.left, n);
        }

  } 
  
  public void borrar(int n) {
        borrarAux(root, n);
  }
  
  public void borrarAux(Node node, int n) {
      if (node.left.data==n || node.right.data==n){
          if(node.left.data==n){
              Node aux = node.left.left;
              node.left = node.left.right;
              Node j = node.left;
              while(j.left!=null){
                  j = j.left;
              }
              j.right=aux;
          } else if(node.right.data==n){
              Node aux = node.right.right;
              node.left = node.right.left;
              Node j = node.right;
              while(j.right!=null){
                  j = j.right;
              }
              j.left=aux;
          }
      } else {
          borrarAux(node.left, n);
          borrarAux(node.right, n);
      }
  }
  private void recursivePrintAUX(Node node){
        if (node!= null)
        {
            
            recursivePrintAUX(node.left);

            recursivePrintAUX(node.right);

            System.out.println(node.data);

        }
    }
}


        



    

 

