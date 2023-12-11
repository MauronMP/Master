package mio.jersey.primero.modelo;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;
//Esta clase solo devuelve una instancia de la clase Todo
@Path("/todo")
public class TodoRecurso {
	//Este método se llamrá si existe una petición XML desde el cliente
	@GET
	@Produces({MediaType.APPLICATION_ATOM_XML, MediaType.APPLICATION_JSON})
	public Todo getXML() {
		Todo todo = new Todo();
		todo.setResumen("Este es mi primer Todo");
		todo.setDescripcion("Este es mi primer Todo");
		return todo;
	}
	@GET
	@Produces({MediaType.TEXT_XML})
	public Todo getHTML() {
		Todo todo = new Todo();
		todo.setResumen("Este es mi primer Todo");
		todo.setDescripcion("Este es mi primer Todo");
		return todo;
	}
}