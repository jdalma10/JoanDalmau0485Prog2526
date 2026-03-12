import java.util.*;
public class ArrayListProva {

	public static void main(String[] args) {
		
		
		ArrayList<String> llista = new ArrayList<>();
		
		llista.add("Hola");
		llista.add("Adeu!");
		
		System.out.println(llista.size());
		
		for(String s:llista) {
			System.out.println(s);
		}
		
		llista.remove(1);
		
		Iterator<String> it =  llista.iterator();		
		while (it.hasNext()){
			System.out.println(it.next());
		}
		
		
		System.out.println(llista.get(0));
		
		System.out.println(llista.indexOf("Hola"));
		
	}

}
