package com.example.demo;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;
import com.dss.spring.first.di.model.*;
import java.util.Date;
@SpringBootApplication
public class Application1Application {

	public static void main(String[] args) {
		SpringApplication.run(Application1Application.class, args);
	}

    public CommandLineRunner jpaSample(TodoRepository todoRepo) {
      return (args) -> {
	//Almacenar los 2 "instancias" de Todo en la base de datos H2   
    todoRepo.save(new Todo("Test"));
    Todo todo = new Todo("Test detallado");
    Date date = new Date();
    todo.setDueDate(date);
    todo.setDescription("Descripcion detallada");
    todoRepo.save(todo);
    RestTemplate restTemplate = new RestTemplate();
    //Ahora los vamos a obtener del servidor REST	   
    Todo firstTodo = restTemplate.getForObject("http://localhost:8080/rest/tasks/1", Todo.class);
    Todo secondTodo = restTemplate.getForObject("http://localhost:8080/rest/tasks/2", Todo.class);
    System.out.println(firstTodo);
    System.out.println(secondTodo);   
    //Ejemplo de POST al servidor REST
    Todo newTodo = new Todo("Nuevo Todo");
    newTodo.setDescription("Todo anadido por la API rest");
    newTodo.setDone(true);
    //Envio y validacion
    ResponseEntity<Todo> postForEntity = 
    restTemplate.postForEntity("http://localhost:8080/rest/tasks/", newTodo, Todo.class);
    System.out.println(postForEntity); 
    };
  }

}
