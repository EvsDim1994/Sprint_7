import io.qameta.allure.junit4.DisplayName;
import model.Courier;
import org.junit.Test;

import static org.hamcrest.Matchers.equalTo;
import static org.junit.Assert.assertNotEquals;
import static org.junit.Assert.assertTrue;

public class CreateCourierTests extends BaseTest {

    @Test
    @DisplayName("Успешное создание курьера")
    public void createCourierTest() {
        var courier = Courier.random();
        boolean created = requests.createCourier(courier)
                .then()
                .assertThat()
                .statusCode(201)
                .extract()
                .path("ok");
        assertTrue(created);
        courierId = requests.loginCourier(courier.getLogin(), courier.getPassword())
                .then()
                .assertThat()
                .statusCode(200)
                .extract()
                .path("id");
        assertNotEquals(0, courierId);
    }

    @Test
    @DisplayName("Создание курьера с повторяющимеся данными")
    public void createCourierWithTheSameDate(){
        var courier = Courier.random();
        requests.createCourier(courier)
                .then()
                .assertThat()
                .statusCode(201);
        courierId = requests.loginCourier(courier.getLogin(), courier.getPassword())
                .then()
                .assertThat()
                .statusCode(200)
                .extract()
                .path("id");
        assertNotEquals(0, courierId);
        requests.createCourier(courier)
                .then()
                .assertThat()
                .statusCode(409)
                .body("message", equalTo("Этот логин уже используется"));
    }

    @Test
    @DisplayName("Создание курьера без логина")
    public void createCourierWithOutLogin(){
        var courier = Courier.random();
        courier.setLogin(null);
        requests.createCourier(courier)
                .then()
                .assertThat()
                .statusCode(400)
                .body("message", equalTo("Недостаточно данных для создания учетной записи"));
    }

    @Test
    @DisplayName("Создание курьера без пароля")
    public void createCourierWithOutPassword(){
        var courier = Courier.random();
        courier.setPassword(null);
        requests.createCourier(courier)
                .then()
                .assertThat()
                .statusCode(400)
                .body("message", equalTo("Недостаточно данных для создания учетной записи"));
    }
}
