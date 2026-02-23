/**
 * @author Pedro Garc�a 
 *
 * To change the template for this generated type comment go to
 * Window>Preferences>Java>Code Generation>Code and Comments
 */
public class Arrays
{

  public static void main(String[] args) {
    
    int[] lista = new int[5];
    
    for (int i=0; i<lista.length; i++)
      lista[i]=i;
      
    for (int i=0; i<lista.length; i++)
      System.out.println(lista[i]);
    
    int[] lista2 = {11, 12, 13, 14, 15};      
    
    for (int i=0; i<lista2.length; i++)
      System.out.println(lista2[i]);
    
    int[][] matrix = new int[3][3];
    
    for (int j=0; j<3; j++)
      for (int k=0; k<3; k++)
        matrix[j][k] = j + k;
    
    for (int j=0; j<3; j++){
      for (int k=0; k<3; k++){
        System.out.print(matrix [j][k] + " "); 
      }   
    System.out.println();
    }
    
  }
}
