
public class Main {

	public static void main(String[] args) {
		
		Company company1 = new Company();
		UserWithoutOffer usuari1 = new UserWithoutOffer("Joel", "44414", 2);
		UserWithOffer1 usuari2 = new UserWithOffer1("Joan", "44414", 2);
		
		company1.add(usuari1);
		company1.add(usuari2);
		
		Conections c1 = new Conections("10","10");
		Conections c2 = new Conections("10","10");

		usuari1.add(c1);
		usuari2.add(c2);
		
		company1.listusers();

	}

}
