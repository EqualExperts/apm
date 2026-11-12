package example;

import jakarta.inject.Inject;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;
import java.util.Map;

@Path("/hello")
public class GreetingResource {
    private final GreetingService service;

    @Inject
    public GreetingResource(GreetingService service) { this.service = service; }

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Map<String, String> hello() { return Map.of("message", service.greeting()); }
}
