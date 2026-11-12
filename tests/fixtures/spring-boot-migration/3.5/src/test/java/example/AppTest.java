package example;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.test.web.servlet.MockMvc;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;
@SpringBootTest @AutoConfigureMockMvc
class AppTest { @Autowired MockMvc mvc;
@Test void jsonContract() throws Exception {mvc.perform(get("/hello")).andExpect(status().isOk()).andExpect(jsonPath("$.message").value("hello"));}
@Test void missingRoute() throws Exception {mvc.perform(get("/missing")).andExpect(status().isNotFound());}}
