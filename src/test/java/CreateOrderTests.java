import assertion.AssertionOrder;
import io.qameta.allure.junit4.DisplayName;
import model.Order;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import static org.junit.Assert.assertTrue;

@RunWith(Parameterized.class)
public class CreateOrderTests extends BaseTest {
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

    @Test
    @DisplayName("Успешное создание заказа")
    public void createOrderTest() {
        var order = Order.makeOrder(color);
        int created = requests.createOrder(order)
                .then()
                .assertThat()
                .statusCode(201)
                .extract()
                .path("track");
        assertTrue(created > 0);
    }
}
