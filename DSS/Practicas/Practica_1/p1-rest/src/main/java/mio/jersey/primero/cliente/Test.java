package mio.jersey.primero.cliente;
import java.net.URI;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.ws.rs.core.UriBuilder;
import jakarta.ws.rs.client.Client;
import jakarta.ws.rs.client.ClientBuilder;
import jakarta.ws.rs.client.Invocation;
import jakarta.ws.rs.client.WebTarget;
import org.glassfish.jersey.client.ClientConfig;

public class Test {

	public static void main(String[] args) {
		ClientConfig clientConfig = new ClientConfig();
		Client client = ClientBuilder.newClient(clientConfig);
		WebTarget webTarget = client.target(getBaseURI());
		WebTarget todoWebTarget = webTarget.path("rest");
		WebTarget helloworldWebTarget = todoWebTarget.path("todo");
		WebTarget helloworldWebTargetWithQueryParam = helloworldWebTarget.queryParam("greeting", "Hi World!");
		 
		Invocation.Builder invocationBuilder = helloworldWebTargetWithQueryParam.request(MediaType.TEXT_XML);
		invocationBuilder.header("some-header", "true"); 
		Response response = invocationBuilder.get();
		System.out.println("Mostrar el código de respuesta:");
		System.out.println(response.getStatus());
		// Mostrar contenido para aplicaciones TEXT_XML
		System.out.println("Mostrar contenido del recurso como Texto XML Plano");
		System.out.println(response.readEntity(String.class));
		
		Invocation.Builder invocationBuilder2 = helloworldWebTargetWithQueryParam.request(MediaType.APPLICATION_JSON);
		invocationBuilder.header("some-header", "true");
		Response response2 = invocationBuilder2.get();
		System.out.println("Mostrar el código de respuesta:");
		System.out.println(response2.getStatus());
		// Mostrar contenido para aplicaciones TEXT_XML
		System.out.println("Mostrar contenido del recurso como Texto JSON de Aplicación");
		System.out.println(response2.readEntity(String.class));
		
	}
	private static URI getBaseURI(){
		return UriBuilder.fromUri("http://localhost:8080/p1-rest").build();
	}
}
