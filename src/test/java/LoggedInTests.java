import io.qameta.allure.junit4.DisplayName;
import model.Courier;
import org.junit.Before;
import org.junit.Test;

import static org.hamcrest.Matchers.equalTo;
import static org.junit.Assert.assertNotEquals;

public class LoggedInTests extends BaseTest {
    private Courier courier;

    @Before
    public void setUp() {
        courier = Courier.random();
        requests.createCourier(courier)
                .then()
                .assertThat()
                .statusCode(201)
                .extract()
                .path("ok");
    }

    @Test
    @DisplayName("Успешная авторизация курьера")
    public void successLoggedInTest(){
        courierId = requests.loginCourier(courier.getLogin(), courier.getPassword())
                .then()
                .assertThat()
                .statusCode(200)
                .extract()
                .path("id");
        assertNotEquals(0, courierId);
    }

    @Test
    @DisplayName("Ошибка при авторизации курьера без передачи поля password")
    public void errorLoggedInTestIncorrectPassword(){
        var courier = Courier.random();
        courier.setPassword(null);
        requests.loginCourier(courier.getLogin(), courier.getPassword())
                .then()
                .assertThat()
                .statusCode(400)
                .body("message", equalTo("Недостаточно данных для входа"));
    }

    @Test
    @DisplayName("Ошибка при авторизации курьера без передачи поля login")
    public void errorLoggedInTestIncorrectLogin(){
        var courier = Courier.random();
        courier.setLogin(null);
        requests.loginCourier(courier.getLogin(), courier.getPassword())
                .then()
                .assertThat()
                .statusCode(400)
                .body("message", equalTo("Недостаточно данных для входа"));
    }

    @Test
    @DisplayName("Ошибка при авторизации курьера c неправильным паролем")
    public void errorLoggedInUnCreatedPassword(){
        var courier = Courier.random();
        courier.setPassword("1111");
        requests.loginCourier(courier.getLogin(), courier.getPassword())
                .then()
                .assertThat()
                .statusCode(404)
                .body("message", equalTo("Учетная запись не найдена"));
    }

    @Test
    @DisplayName("Ошибка при авторизации курьера c неправильным логином")
    public void errorLoggedInTestUnCreatedLogin(){
        var courier = Courier.random();
        courier.setLogin("1111");
        requests.loginCourier(courier.getLogin(), courier.getPassword())
                .then()
                .assertThat()
                .statusCode(404)
                .body("message", equalTo("Учетная запись не найдена"));
    }
}
