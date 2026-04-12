package vn.tt.practice.orderservice.dto;

import java.io.Serializable;

import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class ProductDTO implements Serializable {

    private static final long serialVersionUID = 1L;

    private String id;
    private String name;
    private double price;
    private String description;
    private String image;
    private boolean checkToCart;
    private Integer rating;
    private Integer quantity;
    private String productCode;
}