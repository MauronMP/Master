package mio.jersey.segundo.cliente;
import java.net.URI;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.ws.rs.core.UriBuilder;
import jakarta.ws.rs.client.Client;
import jakarta.ws.rs.client.ClientBuilder;
import jakarta.ws.rs.client.Invocation;
import jakarta.ws.rs.client.WebTarget;
import jakarta.ws.rs.client.Entity;
import org.glassfish.jersey.client.ClientConfig;
import mio.jersey.segundo.modelo.Todo;
import jakarta.ws.rs.core.Form;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ClientConfig clientConfig = new ClientConfig();
		Client client = ClientBuilder.newClient(clientConfig);
		WebTarget webTarget = client.target(getBaseURI());
		//crearse un todo
		Todo todo = new Todo("99", "Este es el resumen de otro registro");
		WebTarget todoWebTarget = webTarget.path("rest");
		WebTarget helloworldWebTarget = todoWebTarget.path("todos");
		WebTarget helloworldWebTargetWithQueryParam = helloworldWebTarget.queryParam("greeting", "Hi World!");
		 //////////////////
		Invocation.Builder invocationBuilder = helloworldWebTargetWithQueryParam.request(MediaType.TEXT_XML);
		invocationBuilder.header("some-header", "true"); 
		Response response = invocationBuilder.put(Entity.entity(todo, MediaType.TEXT_XML));
		comprobacion(response,2,helloworldWebTarget);
	    //// Obtener un Todo a partir de su identificador = "99"
		WebTarget indicadorWebTarget= helloworldWebTarget.path("99");
		WebTarget indicadorWebTargetWithQueryParam = indicadorWebTarget.queryParam("greeting", "Hi World!");
		Invocation.Builder invocationBuilder4 = indicadorWebTargetWithQueryParam.request(MediaType.TEXT_XML);
		invocationBuilder4.header("some-header", "true");
		Response response4 = invocationBuilder4.get();
		comprobacion(response4,4,indicadorWebTargetWithQueryParam);
		//////// Eliminar el Todo con identificador 99
	    Response response5 = invocationBuilder4.delete();
	    comprobacion(response5,5,helloworldWebTargetWithQueryParam);
		////// Mostrar contenido para aplicaciones APPLICATION_JSON
		Invocation.Builder invocationBuilder6 = helloworldWebTargetWithQueryParam.request(MediaType.APPLICATION_JSON);
		invocationBuilder6.header("some-header", "true");
		Response response6 = invocationBuilder6.get();
		comprobacion(response6,6,helloworldWebTargetWithQueryParam);
		///////Insertar formulario y salvarlo como un html
		Form forma = new Form();
		forma.param("i","4");
		forma.param("resumen", "Demostración del cliente lib para formularios");
		Invocation.Builder invocationBuilder7 = helloworldWebTargetWithQueryParam.request(MediaType.TEXT_HTML);
		invocationBuilder7.header("some-header", "true");
		Response response7 = invocationBuilder7.post(Entity.entity(forma,MediaType.APPLICATION_FORM_URLENCODED));
		System.out.println("Formulario respuesta " + response7.getStatus());
		System.out.println(response7.readEntity(String.class));
		
	}
	private static void comprobacion(Response response, int i, WebTarget t) {
		System.out.println("Mostrar el código de respuesta:"+i);
		System.out.println(response.getStatus());
		// Mostrar contenido para aplicaciones JSON
		WebTarget t1 = t.queryParam("greeting", "Hi World!");
		Invocation.Builder invocationBuilder = t1.request(MediaType.APPLICATION_JSON);
		invocationBuilder.header("some-header", "true"); 
		Response response2 = invocationBuilder.get();
		System.out.println("Mostrar el código de respuesta:"+(i+1));
		System.out.println(response2.getStatus());
		// Mostrar contenido para aplicaciones APPLICATION_XML
		System.out.println("Mostrar contenido del recurso como HTML");
		System.out.println(response2.readEntity(String.class));	
	
	}
	
	private static URI getBaseURI(){
		return UriBuilder.fromUri("http://localhost:8080/p2-rest/").build();
	}

}
