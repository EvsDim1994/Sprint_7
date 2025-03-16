import io.qameta.allure.Step;
import io.restassured.response.Response;
import model.Courier;
import model.Order;

import static io.restassured.RestAssured.given;

public class Requests extends Client {

    @Step("Send POST request to /api/v1/courier")
    public Response createCourier(Courier courier){
        return spec()
                .body(courier)
                .when()
                .post(Endpoints.CREATE_COURIER);
    }

    @Step("Send DELETE request to /api/v1/courier/:id")
    public Response deleteCourier(int courierId){
        return spec()
                .delete(Endpoints.DELETE, courierId);
    }

    @Step("Send POST request to /api/v1/courier/login")
    public Response loginCourier(String login, String password){
        return spec()
                .body(new Courier(login, password))
                .when()
                .post(Endpoints.AUTH);
    }

    @Step("Send POST request to api/v1/orders")
    public Response createOrder(Order order){
        return spec()
                .body(order)
                .when()
                .post(Endpoints.CREATE_ORDER);
    }

    @Step("Send GET request to api/v1/orders")
    public Response getOrders(){
        return spec()
                .get(Endpoints.GET_ORDER);
    }
}
