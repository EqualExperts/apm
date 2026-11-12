package example;
import io.vertx.core.*;
import io.vertx.core.eventbus.MessageConsumer;
import io.vertx.core.http.HttpServer;
import io.vertx.core.json.JsonObject;
import io.vertx.ext.web.Router;
public class Service {
    private final Vertx vertx;
    private HttpServer server;
    private MessageConsumer<String> consumer;
    public Service(Vertx vertx) { this.vertx = vertx; }
    public Future<Integer> start() {
        consumer = vertx.eventBus().consumer("greeting", message -> {
            if ("fail".equals(message.body())) message.fail(1, "unavailable");
            else message.reply("hello");
        });
        Router router = Router.router(vertx);
        router.get("/hello").handler(ctx -> vertx.eventBus().<String>request("greeting", "ok")
            .onSuccess(reply -> ctx.response().putHeader("content-type", "application/json").end(new JsonObject().put("message", reply.body()).encode()))
            .onFailure(ctx::fail));
        router.get("/failure").handler(ctx -> vertx.eventBus().request("greeting", "fail")
            .onSuccess(reply -> ctx.response().end())
            .onFailure(error -> ctx.response().setStatusCode(503).end()));
        server = vertx.createHttpServer().requestHandler(router);
        return consumer.completion().compose(ignored -> server.listen(0, "127.0.0.1"))
            .map(HttpServer::actualPort)
            .recover(error -> stop().compose(ignored -> Future.failedFuture(error)));
    }
    public Future<Void> stop() {
        return server.close().compose(ignored -> consumer.unregister());
    }
}
