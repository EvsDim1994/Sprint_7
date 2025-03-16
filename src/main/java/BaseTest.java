import assertion.AssertionOrder;
import org.junit.After;

public class BaseTest {

    protected int courierId;

    protected final AssertionOrder assertionsOrder = new AssertionOrder();

    protected final Requests requests = new Requests();

    @After
    public void deleteCourier() {
        if (courierId > 0) {
            requests.deleteCourier(courierId)
                    .then()
                    .assertThat()
                    .statusCode(200)
                    .extract()
                    .path("ok");
        }
    }
}
