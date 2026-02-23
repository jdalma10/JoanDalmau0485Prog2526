

/**
 * @author Pedro Garc�a 
 */
public class Cosa2 
{
	private int patas;
	private String nombre;

	public Cosa2(){
		this.nombre = "Cosa";
		this.patas = 4;
	}

	public Cosa2(String nombre, int patas)
	{
		this.nombre = nombre;
		this.patas = patas;
	}

	public void setPatas(int patas)
	{
		this.patas = patas;
	}
	public int getPatas()
	{
		return patas;
	}
	public void setNombre(String nombre)
		{
			this.nombre = nombre;
		}
	public String getNombre()
	{
		return nombre;
	}
	
	
}
