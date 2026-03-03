public class UsaConcessionari {

	public static void main(String[] args) {

		Concessionari con = new Concessionari();



		Cotxe cotxe1 = new Cotxe("RT45YU67");

		cotxe1.setMarca("Fiat");

		cotxe1.setModel("500");

		con.nouCotxe(cotxe1);



		Cotxe cotxe2 = new Cotxe("RZ26YP03");

		cotxe2.setMarca("Seat");

		cotxe2.setModel("Panda");

		con.nouCotxe(cotxe2);



		Cotxe cotxe3 = new Cotxe("FT93DQ77");

		cotxe3.setMarca("Seat");

		cotxe3.setModel("Leon");

		con.nouCotxe(cotxe3);
		
		
		Cotxe cotxe4 = cotxe3;
		cotxe4.setMarca("Tesla");



		System.out.println(con);


		
		  Cotxe c = con.buscaCotxe("RZ26YP03");
		  
		  System.out.println(c);
		 
	}

}