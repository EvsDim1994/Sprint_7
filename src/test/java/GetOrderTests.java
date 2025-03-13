import assertion.AssertionOrder;
import io.qameta.allure.junit4.DisplayName;
import io.restassured.RestAssured;
import model.Order;
import org.junit.Before;
import org.junit.Test;

public class GetOrderTests {
    private final Requests requests = new Requests();
    private final AssertionOrder assertionsOrder = new AssertionOrder();

    @Before
    public void setUp() {
        RestAssured.baseURI = Endpoints.BASE_URL;
    }

    @Test
    @DisplayName("Успешное получение заказов")
    public void createOrderTest() {
        assertionsOrder.successfullyGetOrders(requests.getOrders());
    }
}
