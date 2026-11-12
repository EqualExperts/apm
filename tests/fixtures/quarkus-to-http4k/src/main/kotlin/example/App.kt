package example

import org.http4k.core.*

fun app(greeting: (Boolean) -> String): HttpHandler = { request ->
    if (request.method != Method.GET || request.uri.path !in setOf("/hello", "/failure")) {
        Response(Status.NOT_FOUND)
    } else {
        try {
            val message = greeting(request.uri.path == "/failure")
            // This fixture has one fixed payload; production DTOs require a reviewed JSON codec.
            check(message == "hello")
            Response(Status.OK).header("content-type", "application/json").body("""{"message":"hello"}""")
        } catch (_: IllegalStateException) {
            Response(Status.SERVICE_UNAVAILABLE)
        }
    }
}
