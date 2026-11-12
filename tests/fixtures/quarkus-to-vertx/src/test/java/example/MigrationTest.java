package example;
import io.vertx.core.Vertx;
import java.net.URI;
import java.net.http.*;
import java.util.concurrent.TimeUnit;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
class MigrationTest {
    @Test void contractsAndLifecycle() throws Exception {
        Vertx vertx = Vertx.vertx();
        Service service = new Service(vertx);
        try {
            int port = service.start().toCompletionStage().toCompletableFuture().get(10, TimeUnit.SECONDS);
            URI base = URI.create("http://127.0.0.1:" + port);
            HttpClient client = HttpClient.newHttpClient();
            var response = client.send(HttpRequest.newBuilder(base.resolve("/hello")).GET().build(), HttpResponse.BodyHandlers.ofString());
            assertEquals(200, response.statusCode());
            assertEquals("{\"message\":\"hello\"}", response.body());
            assertTrue(response.headers().firstValue("content-type").orElse("").startsWith("application/json"));
            for (String route : new String[]{"/missing", "/failure"}) {
                var other = client.send(HttpRequest.newBuilder(base.resolve(route)).GET().build(), HttpResponse.BodyHandlers.ofString());
                assertEquals(route.equals("/missing") ? 404 : 503, other.statusCode());
            }
            service.stop().toCompletionStage().toCompletableFuture().get(10, TimeUnit.SECONDS);
            var failure = assertThrows(java.util.concurrent.ExecutionException.class, () -> vertx.eventBus().request("greeting", "ok").toCompletionStage().toCompletableFuture().get(10, TimeUnit.SECONDS));
            assertEquals(io.vertx.core.eventbus.ReplyFailure.NO_HANDLERS, ((io.vertx.core.eventbus.ReplyException) failure.getCause()).failureType());
        } finally {
            vertx.close().toCompletionStage().toCompletableFuture().get(10, TimeUnit.SECONDS);
        }
    }
}
