package gov.nih.nci.bento.controller;

import gov.nih.nci.bento.model.ConfigurationDAO;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.boot.web.server.LocalServerPort;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.test.context.junit4.SpringRunner;

import static org.assertj.core.api.Assertions.assertThat;
import static org.springframework.boot.test.context.SpringBootTest.WebEnvironment.RANDOM_PORT;

@RunWith(SpringRunner.class)
@SpringBootTest(webEnvironment=RANDOM_PORT)
public class GraphQLControllerTest {

    @Autowired
    private ConfigurationDAO config;

    @LocalServerPort
    private int port;

    @Autowired
    private TestRestTemplate restTemplate;


    @Test
    public void init_Test() {
    }

    @Test
    public void getVersion_Test() {
        String url = "http://localhost:" + port + "/version";
        ResponseEntity<String> responseEntity = restTemplate.getForEntity(url, String.class);
        assertThat(responseEntity.getStatusCode()).isEqualTo(HttpStatus.OK);
        assertThat(responseEntity.getBody()).isEqualTo("Bento API Version: "+config.getBentoApiVersion());
    }


    @Test
    public void getGraphQLResponseByGET_Test() {
    }

    @Test
    public void getGraphQLResponse_Test() {
    }
}