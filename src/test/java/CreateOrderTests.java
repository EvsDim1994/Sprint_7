import assertion.AssertionOrder;
import io.qameta.allure.junit4.DisplayName;
import io.restassured.RestAssured;
import model.Order;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

@RunWith(Parameterized.class)
public class CreateOrderTests {
    private final String[] color;

    public CreateOrderTests(String[] color) {
    this.color = color;
    }

    @Parameterized.Parameters
    public static Object[][] getData() {
        return new Object[][]{
                {new String[]{"BLACK", "GREY"}},
                {new String[]{"BLACK"}},
                {new String[]{"GREY"}},
                {new String[]{}}
        };
    }

    private final Requests requests = new Requests();
    private final AssertionOrder assertionsOrder = new AssertionOrder();

    @Before
    public void setUp() {
        RestAssured.baseURI = Endpoints.BASE_URL;
    }

    @Test
    @DisplayName("Успешное создание заказа")
    public void createOrderTest() {
        var order = Order.makeOrder(color);
        assertionsOrder.successfullyCreateOrder(requests.createOrder(order));
    }
}
