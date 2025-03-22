import io.qameta.allure.junit4.DisplayName;
import model.Order;
import org.junit.Test;

import java.util.List;

import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;

public class GetOrderTests extends BaseTest {

    @Test
    @DisplayName("Успешное получение заказов")
    public void createOrderTest() {
        List<Order> orders = requests.getOrders()
                .then()
                .assertThat()
                .statusCode(200)
                .extract()
                .path("orders");
        assertNotNull(orders);
        assertTrue(orders.size() > 0);
    }
}
