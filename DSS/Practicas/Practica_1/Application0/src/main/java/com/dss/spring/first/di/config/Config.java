package com.dss.spring.first.di.config;
import java.util.Date;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.beans.factory.annotation.Qualifier;
@Configuration
@ComponentScan(basePackages = { "com.dss.spring.first.di.model" })
public class Config {
	@Bean
    public Long getId() {
        return Long.valueOf(0);
    }
    @Bean
    @Qualifier("summary")
    public String getSummary() {
        return "Spring: prueba de Inyeccion de Dependencias muy basica";
    }
    @Bean
    @Qualifier("description")
    public String getDescription() {
        return "Spring: prueba de Inyeccion de Dependencias y todo lo demas";
    }
    @Bean
    public Boolean isDone() {
        return Boolean.FALSE;
    }
    @Bean
    public Date getDueDate() {
        return new Date();
    }
}
