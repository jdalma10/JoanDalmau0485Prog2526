
public class UsaHotel {

	public static void main(String[] args) {
		
		Hotel hotel = new Hotel("Jaume Hugue", 5);
		
		
		Habitacio h1 = new Habitacio(1,Categoria.normal, 2);
		Habitacio h2 = new Habitacio(2,Categoria.normal, 1);
		Habitacio h3 = new Habitacio(3,Categoria.luxe, 2);
		
		hotel.afegirHabitacio(h1);
		hotel.afegirHabitacio(h2);
		hotel.afegirHabitacio(h3);
		
		
		Client c1 = new Client("Joan", "333333", null);
		Client c2 = new Client("Maria", "444444", null);
		
		//Reserva r = new Reserva( hotel.getReserves().size()+1, c1, h1, 4);
		hotel.reservar(c1, h1, 4);
		
		System.out.println(hotel.disponibles());
		
		
		System.out.println("Preu " + ": " + hotel.calcularFactura("Joan"));
	

	}

}
