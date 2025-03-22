package response;

import model.AvailableStation;
import model.Order;
import model.PageInfo;

import java.util.List;

public class OrderResponse {
    private List<Order> orders;
    private PageInfo pageInfo;
    private List<AvailableStation> availableStations;
}
