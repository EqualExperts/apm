package example;
import io.quarkus.test.junit.QuarkusTest;
import io.quarkus.test.common.http.TestHTTPResource;
import java.net.URI;
import java.net.http.*;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
@QuarkusTest
class MigrationTest {
    @TestHTTPResource URI base;
    @Test void httpContracts() throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        var response = client.send(HttpRequest.newBuilder(base.resolve("/hello")).timeout(java.time.Duration.ofSeconds(5)).GET().build(), HttpResponse.BodyHandlers.ofString());
        assertEquals(200, response.statusCode());
        assertEquals("{\"message\":\"hello\"}", response.body());
        assertTrue(response.headers().firstValue("content-type").orElse("").startsWith("application/json"));
        var missing = client.send(HttpRequest.newBuilder(base.resolve("/missing")).timeout(java.time.Duration.ofSeconds(5)).GET().build(), HttpResponse.BodyHandlers.ofString());
        assertEquals(404, missing.statusCode());
    }
}
