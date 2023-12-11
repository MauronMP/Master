package mio.jersey.segundo.modelo;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.PUT;
import jakarta.ws.rs.DELETE;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.PathParam;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.FormParam;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Request;
import jakarta.ws.rs.core.Response;
import jakarta.ws.rs.core.UriInfo;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.io.PrintWriter;
import jakarta.servlet.ServletRequest;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpServletRequest;
//import jakarta.servlet.ServletException;
import jakarta.xml.bind.*;


@Path("/todos")
public class TodosRecurso {
  //Devolvera la lista de todos lo elementos contenidos en el proveedor al 
  //navegador del usuario.
  @Context
  UriInfo uriInfo;
  @Context
  Request request;
  String id;
  
  // Devolvera la lista de todos lo elementos contenidos en el proveeedor 
  //a las aplicaciones cliente 
  
  @GET
  @Produces(MediaType.APPLICATION_JSON)
  public List<Todo> getTodosBrowser() {
    List<Todo> todos = new ArrayList<Todo>();
    todos.addAll(TodoDAO.INSTANCE.getModel().values());
    return todos;
  }
  @GET
  @Produces({MediaType.TEXT_HTML,MediaType.APPLICATION_XML})
  public List<Todo> getTodos(){
	  List<Todo> todos = new ArrayList<Todo>();
	  todos.addAll(TodoDAO.INSTANCE.getModel().values());
	  return todos;
  }
  @GET
  @Path("cont")
  @Produces(MediaType.TEXT_PLAIN)
  public String getCount() {
	    int cont = TodoDAO.INSTANCE.getModel().size();
	    return String.valueOf(cont);
  }
  @PUT
  @Consumes(MediaType.TEXT_XML)
  public Response putTodo(JAXBElement<Todo> todo) {
      Todo c = todo.getValue();
      return putAndGetResponse(c);
  }
  @DELETE
  public void deleteTodo() {
      Todo c = TodoDAO.INSTANCE.getModel().remove(id);
      if(c==null)
          throw new RuntimeException("Delete: Todo con identificador " + id +  " no se encuentra");
  }
//Para enviar datos al servidor como un formulario Web
  @POST
  @Produces(MediaType.TEXT_HTML)
  @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
  public void newTodo(@FormParam("id") String id,
   @FormParam("resumen") String resumen,
   @FormParam("descripcion") String descripcion,
   @Context HttpServletResponse servletResponse) throws IOException {
    Todo todo = new Todo(id, resumen);
    if (descripcion != null) {
      todo.setDescripcion(descripcion);
    }
    TodoDAO.INSTANCE.getModel().put(id, todo);
  servletResponse.sendRedirect("../crear_todo.html");
  }
  //////////////////////////
  private Response putAndGetResponse(Todo todo) {
      Response res;
      if(TodoDAO.INSTANCE.getModel().containsKey(todo.getId())) {
          res = Response.noContent().build();
      } else {
          res = Response.created(uriInfo.getAbsolutePath()).build();
      }
      TodoDAO.INSTANCE.getModel().put(todo.getId(), todo);
      return res;
  }
  
  
  
//Para poder pasarle argumentos a las operaciones en el servidor
//Permite por ejemplo escribir http://localhost:8080/p2-rest/rest/todos/1
 @Path("{todo}")
 public TodoRecurso getTodo(@PathParam("todo") String id) {
    return new TodoRecurso(uriInfo, request, id);
  }
}
