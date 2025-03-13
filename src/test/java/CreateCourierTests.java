import assertion.AssertionsCourier;
import io.qameta.allure.junit4.DisplayName;
import io.restassured.RestAssured;
import model.Courier;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class CreateCourierTests {
    private final Requests requests = new Requests();
    private final AssertionsCourier assertionsCourier = new AssertionsCourier();
    private int courierId;

    @Before
    public void setUp() {
        RestAssured.baseURI = Endpoints.BASE_URL;
    }


    @Test
    @DisplayName("Успешное создание курьера")
    public void createCourierTest() {
        var courier = Courier.random();
        assertionsCourier.successfullyCreate(requests.createCourier(courier));
        courierId = assertionsCourier.successfullyLoggedIn
                (requests.loginCourier(courier.getLogin(), courier.getPassword()));
    }

    @Test
    @DisplayName("Создание курьера с повторяющимеся данными")
    public void createCourierWithTheSameDate(){
        var courier = Courier.random();
        assertionsCourier.successfullyCreate(requests.createCourier(courier));
        courierId = assertionsCourier.successfullyLoggedIn
                (requests.loginCourier(courier.getLogin(), courier.getPassword()));
        assertionsCourier.errorForRepeatCourier(requests.createCourier(courier));
    }

    @Test
    @DisplayName("Создание курьера без логина")
    public void createCourierWithOutLogin(){
        var courier = Courier.random();
        courier.setLogin(null);
        assertionsCourier.unsuccessfullyCreate(requests.createCourier(courier));
    }

    @Test
    @DisplayName("Создание курьера без пароля")
    public void createCourierWithOutPassword(){
        var courier = Courier.random();
        courier.setPassword(null);
        assertionsCourier.unsuccessfullyCreate(requests.createCourier(courier));
    }

    @After
    public void deleteCourier() {
        if (courierId > 0) {
            assertionsCourier.successfullyDelete(requests.deleteCourier(courierId));
        }
    }
}
