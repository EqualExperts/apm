package example;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
@SpringBootApplication
@RestController
public class App { @GetMapping("/hello") public java.util.Map<String,String> hello(){return java.util.Map.of("message","hello");} }
