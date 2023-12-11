package mio.jersey.segundo.modelo;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.PUT;
import jakarta.ws.rs.DELETE;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Request;
import jakarta.ws.rs.core.Response;
import jakarta.ws.rs.core.UriInfo;
import jakarta.xml.bind.*;

public class TodoRecurso {
	@Context
    UriInfo uriInfo;
    @Context
    Request request;
    String id;
    public TodoRecurso(UriInfo uriInfo, Request request, String id) {
        this.uriInfo = uriInfo;
        this.request = request;
        this.id = id;
    }
  //para integracion con las aplicaciones
    @GET
    @Produces({MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON})
    public Todo getTodo() {
        Todo todo = TodoDAO.INSTANCE.getModel().get(id);
        if(todo==null)
            throw new RuntimeException("Get: Todo con identificador " + id +  " no se encuentra");
        return todo;
    }
    // para integracion con navegadores
    @GET
    @Produces(MediaType.TEXT_XML)
    public Todo getTodoHTML() {
        Todo todo = TodoDAO.INSTANCE.getModel().get(id);
        if(todo==null)
            throw new RuntimeException("Get: Todo con identificador " + id +  " no se encuentra");
        return todo;
    }
    @PUT
    @Consumes(MediaType.APPLICATION_XML)
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
}
