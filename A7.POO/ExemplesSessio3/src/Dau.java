import java.lang.Math;
public class Dau {

	public static final int CARES = 6;
	
	public static int tirada() {
		return (int)(Math.random()*CARES +1);
	}

	
	public static void main(String[] args) {
		System.out.println(Dau.tirada());
		
	}

}
