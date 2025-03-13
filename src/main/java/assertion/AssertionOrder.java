package assertion;

import io.qameta.allure.Step;
import io.restassured.response.Response;
import model.Order;

import java.util.List;

import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;

public class AssertionOrder {

    @Step("Check successfully create order")
    public void successfullyCreateOrder(Response response){
        int created = response.then()
                .assertThat()
                .statusCode(201)
                .extract()
                .path("track");
        assertTrue(created > 0);
    }

    @Step("Check successfully get orders")
    public void successfullyGetOrders(Response response){
        List<Order> orders = response.then()
                .assertThat()
                .statusCode(200)
                .extract()
                .path("orders");
        assertNotNull(orders);
        assertTrue(orders.size() > 0);
    }
}
