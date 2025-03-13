package assertion;

import io.qameta.allure.Step;
import io.restassured.response.Response;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;
import static org.junit.Assert.assertNotEquals;
import static org.junit.Assert.assertTrue;

public class AssertionsCourier {

    @Step("Check successfully create courier")
    public void successfullyCreate(Response response){
        boolean created = response.then()
                .assertThat()
                .statusCode(201)
                .extract()
                .path("ok");
        assertTrue(created);
    }

    @Step("Check successfully delete courier")
    public void successfullyDelete(Response response){
        boolean delete = response.then()
                .assertThat()
                .statusCode(200)
                .extract()
                .path("ok");
        assertTrue(delete);
    }

    @Step("Check successfully login courier")
    public int successfullyLoggedIn(Response response){
        int id = response.then()
                .assertThat()
                .statusCode(200)
                .extract()
                .path("id");
        assertNotEquals(0, id);
        return id;
    }

    @Step("Check unsuccessfully create courier")
    public void unsuccessfullyCreate(Response response){
        response.then()
                .assertThat()
                .statusCode(400)
                .body("message", equalTo("Недостаточно данных для создания учетной записи"));

    }

    @Step("Check error for repeat create courier")
    public void errorForRepeatCourier(Response response){
        response.then()
                .assertThat()
                .statusCode(409)
                .body("message", equalTo("Этот логин уже используется"));

    }

    @Step("Check unsuccessfully loggedIn courier without data")
    public void unsuccessfullyLoggedIn(Response response){
        response.then()
                .assertThat()
                .statusCode(400)
                .body("message", equalTo("Недостаточно данных для входа"));
    }

    @Step("Check unsuccessfully loggedIn courier with incorrect data")
    public void missingDataLoggedIn(Response response){
        response.then()
                .assertThat()
                .statusCode(404)
                .body("message", equalTo("Учетная запись не найдена"));
    }
}
