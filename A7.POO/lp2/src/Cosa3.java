

/**
 * @author Pedro García 
 *
 */
public class Cosa3 
{
	private int patas;
	private String nombre;
	private static int cuernos = 3;
	

	public Cosa3(String nombre, int patas)
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
	
	public static int getCuernos()
	{
		return cuernos;
	}
	
	public static void setCuernos(int numero)
	{
		cuernos = numero;
	}	
	
	
	
	
}

