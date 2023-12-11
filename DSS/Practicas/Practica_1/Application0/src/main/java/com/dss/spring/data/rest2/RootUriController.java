package com.dss.spring.data.rest2;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.GetMapping;
@Controller
public class RootUriController {
	@RequestMapping(value = "/index")
    public String index() {
      return "index";
    }
}
