package com.admin.page;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@SpringBootApplication
public class PageApplication {
    @GetMapping(value = "/hi")
    public String sayHello() {
        return "hello world";
    }

    public static void main(String[] args) {
        SpringApplication.run(PageApplication.class, args);
    }

}
