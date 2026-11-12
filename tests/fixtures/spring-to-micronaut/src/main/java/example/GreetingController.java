package example;
import io.micronaut.http.annotation.*;
import io.micronaut.serde.annotation.Serdeable;
@Controller("/hello")
public class GreetingController {
    private final GreetingService service;
    public GreetingController(GreetingService service) { this.service = service; }
    @Get public Greeting hello() { return new Greeting(service.greeting()); }
    @Serdeable public record Greeting(String message) {}
}
