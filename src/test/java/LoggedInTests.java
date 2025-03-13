import assertion.AssertionsCourier;
import io.qameta.allure.junit4.DisplayName;
import io.restassured.RestAssured;
import model.Courier;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class LoggedInTests {
    private final Requests requests = new Requests();
    private final AssertionsCourier assertionsCourier = new AssertionsCourier();
    private int courierId;
    private Courier courier;

    @Before
    public void setUp() {
        RestAssured.baseURI = Endpoints.BASE_URL;
        courier = Courier.random();
        assertionsCourier.successfullyCreate(requests.createCourier(courier));
    }

    @Test
    @DisplayName("Успешная авторизация курьера")
    public void successLoggedInTest(){
        courierId = assertionsCourier.successfullyLoggedIn
                (requests.loginCourier(courier.getLogin(), courier.getPassword()));
    }

    @Test
    @DisplayName("Ошибка при авторизации курьера без передачи поля password")
    public void errorLoggedInTestIncorrectPassword(){
        var courier = Courier.random();
        courier.setPassword(null);
        assertionsCourier.unsuccessfullyLoggedIn
                (requests.loginCourier(courier.getLogin(), courier.getPassword()));
    }

    @Test
    @DisplayName("Ошибка при авторизации курьера без передачи поля login")
    public void errorLoggedInTestIncorrectLogin(){
        var courier = Courier.random();
        courier.setLogin(null);
        assertionsCourier.unsuccessfullyLoggedIn
                (requests.loginCourier(courier.getLogin(), courier.getPassword()));
    }

    @Test
    @DisplayName("Ошибка при авторизации курьера c неправильным паролем")
    public void errorLoggedInUnCreatedPassword(){
        var courier = Courier.random();
        courier.setPassword("1111");
        assertionsCourier.missingDataLoggedIn
                (requests.loginCourier(courier.getLogin(), courier.getPassword()));
    }

    @Test
    @DisplayName("Ошибка при авторизации курьера c неправильным логином")
    public void errorLoggedInTestUnCreatedLogin(){
        var courier = Courier.random();
        courier.setLogin("1111");
        assertionsCourier.missingDataLoggedIn
                (requests.loginCourier(courier.getLogin(), courier.getPassword()));
    }


    @After
    public void deleteCourier() {
        if (courierId > 0) {
            assertionsCourier.successfullyDelete(requests.deleteCourier(courierId));
        }
    }
}
