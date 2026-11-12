module example.migration.test {
 requires example.migration;
 requires com.guicedee.client;
 requires com.google.guice;
 requires org.junit.jupiter.api;
 opens example.migration.test to org.junit.platform.commons;
}
