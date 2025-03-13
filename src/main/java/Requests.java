import io.qameta.allure.Step;
import io.restassured.response.Response;
import model.Courier;
import model.Order;

import static io.restassured.RestAssured.given;

public class Requests {

    @Step("Send POST request to /api/v1/courier")
    public Response createCourier(Courier courier){
        return given()
                .header("Content-type", "application/json")
                .log().all()
                .and()
                .body(courier)
                .when()
                .post(Endpoints.CREATE_COURIER);
    }

    @Step("Send DELETE request to /api/v1/courier/:id")
    public Response deleteCourier(int courierId){
        return given()
                .header("Content-type", "application/json")
                .log().all()
                .and()
                .when()
                .delete(Endpoints.DELETE, courierId);
    }

    @Step("Send POST request to /api/v1/courier/login")
    public Response loginCourier(String login, String password){
        return given()
                .header("Content-type", "application/json")
                .log().all()
                .and()
                .body(new Courier(login, password))
                .when()
                .post(Endpoints.AUTH);
    }

    @Step("Send POST request to api/v1/orders")
    public Response createOrder(Order order){
        return given()
                .header("Content-type", "application/json")
                .log().all()
                .and()
                .body(order)
                .when()
                .post(Endpoints.CREATE_ORDER);
    }

    @Step("Send GET request to api/v1/orders")
    public Response getOrders(){
        return given()
                .header("Content-type", "application/json")
                .log().all()
                .when()
                .get(Endpoints.GET_ORDER);
    }
}
