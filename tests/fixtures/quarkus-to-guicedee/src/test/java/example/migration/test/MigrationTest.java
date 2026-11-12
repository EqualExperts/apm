package example.migration.test;
import example.migration.App;
import com.guicedee.client.IGuiceContext;
import org.junit.jupiter.api.Test;
import java.util.concurrent.TimeUnit;
import static org.junit.jupiter.api.Assertions.*;
class MigrationTest {
 @Test void discoveredBindingAndLifecycle() throws Exception {
  App.prepare();
  var context = IGuiceContext.instance();
  try {
   var injector = context.inject();
   context.getLoadingFinished().toCompletionStage().toCompletableFuture().get(60, TimeUnit.SECONDS);
   assertEquals("hello", injector.getInstance(String.class));
  } finally { context.destroy(); }
  assertDoesNotThrow(context::destroy);
 }
}
