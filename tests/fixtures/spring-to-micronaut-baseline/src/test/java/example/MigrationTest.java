package example;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.server.LocalServerPort;
import java.net.URI;
import java.net.http.*;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class MigrationTest {
    @LocalServerPort int port;
    @Test void httpContracts() throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        URI base = URI.create("http://localhost:" + port);
        var response = client.send(HttpRequest.newBuilder(base.resolve("/hello")).GET().build(), HttpResponse.BodyHandlers.ofString());
        assertEquals(200, response.statusCode());
        assertEquals("{\"message\":\"hello\"}", response.body());
        assertTrue(response.headers().firstValue("content-type").orElse("").startsWith("application/json"));
        var missing = client.send(HttpRequest.newBuilder(base.resolve("/missing")).GET().build(), HttpResponse.BodyHandlers.ofString());
        assertEquals(404, missing.statusCode());
    }
}
