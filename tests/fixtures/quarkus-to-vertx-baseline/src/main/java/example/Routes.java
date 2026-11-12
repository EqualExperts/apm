package example;
import jakarta.enterprise.context.ApplicationScoped;
import jakarta.enterprise.event.Observes;
import jakarta.inject.Inject;
import io.quarkus.vertx.ConsumeEvent;
import io.vertx.core.Vertx;
import io.vertx.core.json.JsonObject;
import io.vertx.ext.web.Router;
@ApplicationScoped
public class Routes {
    @Inject Vertx vertx;
    @ConsumeEvent("greeting") String greeting(String body) {
        if ("fail".equals(body)) throw new IllegalStateException("unavailable");
        return "hello";
    }
    void routes(@Observes Router router) {
        router.get("/hello").handler(ctx -> vertx.eventBus().<String>request("greeting", "ok")
            .onSuccess(reply -> ctx.response().putHeader("content-type", "application/json").end(new JsonObject().put("message", reply.body()).encode()))
            .onFailure(ctx::fail));
        router.get("/failure").handler(ctx -> vertx.eventBus().request("greeting", "fail")
            .onSuccess(reply -> ctx.response().end())
            .onFailure(error -> ctx.response().setStatusCode(503).end()));
    }
}
