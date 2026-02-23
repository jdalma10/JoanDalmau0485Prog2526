import java.io.*;

/**
 * @author Pedro García 
 *
 */
public class Wrapper {

	public static void main(String[] args) throws Exception{
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in)); 
		
		System.out.println("Introduce Texto:");
		String linea = in.readLine();
		System.out.println(linea);
		
		System.out.println("Introduce Entero:");
		linea = in.readLine();
		int x = Integer.parseInt(linea);
		System.out.println(x);
		
		Integer Ix = new Integer(x);
		int z = Ix.intValue();
		
		String Sx =String.valueOf(z);
		String Sz = Ix.toString();
		
		
		
		
	}
}
