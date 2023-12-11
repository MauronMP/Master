package mio.jersey.primero.modelo;
import jakarta.xml.bind.annotation.XmlRootElement;
@XmlRootElement
//JAX soporta una correspondencia automática desde una clase JAXB con anotaciones XML y JSON

public class Todo {
	private String resumen;
	private String descripcion;
	public String getResumen() {
		return resumen;
	}
	public void setResumen(String resumen) {
		this.resumen= resumen;
	}
	public String getDescripcion() {
		return descripcion;
	}
	public void setDescripcion(String resumen) {
		this.descripcion= resumen;
	}

}
