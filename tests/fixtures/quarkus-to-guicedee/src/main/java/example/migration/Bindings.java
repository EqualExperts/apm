package example.migration;
import com.google.inject.AbstractModule;
import com.guicedee.client.services.lifecycle.IGuiceModule;
public class Bindings extends AbstractModule implements IGuiceModule<Bindings> {
 @Override protected void configure() { bind(String.class).toInstance("hello"); }
}
