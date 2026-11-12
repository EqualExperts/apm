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
    @Test void contracts() throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        var response = client.send(HttpRequest.newBuilder(base.resolve("/hello")).GET().build(), HttpResponse.BodyHandlers.ofString());
        assertEquals(200, response.statusCode());
        assertEquals("{\"message\":\"hello\"}", response.body());
        assertTrue(response.headers().firstValue("content-type").orElse("").startsWith("application/json"));
        for (String route : new String[]{"/missing", "/failure"}) {
            var other = client.send(HttpRequest.newBuilder(base.resolve(route)).GET().build(), HttpResponse.BodyHandlers.ofString());
            assertEquals(route.equals("/missing") ? 404 : 503, other.statusCode());
        }
    }
}
