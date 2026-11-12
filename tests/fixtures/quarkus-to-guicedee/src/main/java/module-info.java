module example.migration {
 requires com.guicedee.guicedinjection;
 requires com.guicedee.client;
 requires com.google.guice;
 exports example.migration;
 opens example.migration to com.google.guice;
 provides com.guicedee.client.services.lifecycle.IGuiceModule with example.migration.Bindings;
}
