package example.migration;
import com.guicedee.client.IGuiceContext;
import com.guicedee.client.utils.LogUtils;
import com.guicedee.guicedinjection.GuiceApplication;
public class App {
 public static void prepare() {
  IGuiceContext.registerModule("example.migration");
  IGuiceContext.instance().getConfig().setServiceLoadWithClassPath(true);
 }
 public static void main(String[] args) { LogUtils.addHighlightedConsoleLogger(); GuiceApplication.run(App::prepare); }
}
