package example;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import org.springframework.stereotype.Service;
@SpringBootApplication
@RestController
public class App {
    private final GreetingService service;
    public App(GreetingService service) { this.service = service; }
    @GetMapping("/hello") public java.util.Map<String,String> hello() { return java.util.Map.of("message", service.greeting()); }
}
@Service
class GreetingService { public String greeting() { return "hello"; } }
