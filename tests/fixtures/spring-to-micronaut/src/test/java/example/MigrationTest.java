package example;
import io.micronaut.context.ApplicationContext;
import io.micronaut.runtime.server.EmbeddedServer;
import java.net.http.*;
import java.util.Map;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
class MigrationTest {
    @Test void httpContracts() throws Exception {
        try (EmbeddedServer server = ApplicationContext.run(EmbeddedServer.class, Map.of("micronaut.server.port", -1))) {
            HttpClient client = HttpClient.newHttpClient();
            var response = client.send(HttpRequest.newBuilder(server.getURI().resolve("/hello")).GET().build(), HttpResponse.BodyHandlers.ofString());
            assertEquals(200, response.statusCode());
            assertEquals("{\"message\":\"hello\"}", response.body());
            assertTrue(response.headers().firstValue("content-type").orElse("").startsWith("application/json"));
            var missing = client.send(HttpRequest.newBuilder(server.getURI().resolve("/missing")).GET().build(), HttpResponse.BodyHandlers.ofString());
            assertEquals(404, missing.statusCode());
        }
    }
}
