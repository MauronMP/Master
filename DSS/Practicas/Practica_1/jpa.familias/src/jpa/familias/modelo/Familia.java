package jpa.familias.modelo;
import java.util.ArrayList;
import java.util.List;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
@Entity
public class Familia {
	@Id
    @GeneratedValue(strategy = GenerationType.TABLE)
    private int id;
    private String descripcion;
    
    @OneToMany(mappedBy = "familia")
    private final List<Persona> miembros = new ArrayList<Persona>();
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public List<Persona> getMiembros() {
        return miembros;
    }
}
