package example

import org.http4k.core.*
import org.http4k.server.SunHttp
import org.http4k.server.asServer
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.Assertions.*
import java.net.URI
import java.net.http.*
import java.time.Duration

class MigrationTest {
    private val handler = app { fail -> if (fail) error("unavailable") else "hello" }
    @Test fun pureHandlerContract() {
        assertEquals(Status.OK, handler(Request(Method.GET, "/hello")).status)
        assertEquals(Status.SERVICE_UNAVAILABLE, handler(Request(Method.GET, "/failure")).status)
    }
    @Test fun realHttpContract() {
        val server = handler.asServer(SunHttp(0)).start()
        try {
            val client = HttpClient.newHttpClient()
            for ((path, status) in mapOf("/hello" to 200, "/missing" to 404, "/failure" to 503)) {
                val request = HttpRequest.newBuilder(URI("http://localhost:${server.port()}$path")).timeout(Duration.ofSeconds(5)).GET().build()
                val response = client.send(request, HttpResponse.BodyHandlers.ofString())
                assertEquals(status, response.statusCode())
                if (path == "/hello") {
                    assertEquals("""{"message":"hello"}""", response.body())
                    assertTrue(response.headers().firstValue("content-type").orElse("").startsWith("application/json"))
                }
            }
        } finally { server.stop() }
    }
}
