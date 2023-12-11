package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import com.dss.spring.first.di.config.*;
import com.dss.spring.first.di.model.*;
@SpringBootApplication
public class Application0Application {

	public static void main(String[] args) {
		//SpringApplication.run(Application0Application.class, args);
		AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(Config.class);
        ITodo todo = context.getBean(ITodo.class);
        System.out.println(todo);
        ITodo todo2 = context.getBean(ITodo.class);
        System.out.println(todo2);
        context.close();
	}

}
