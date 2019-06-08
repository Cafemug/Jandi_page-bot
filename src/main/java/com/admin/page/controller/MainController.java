package com.admin.page.controller;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MainController {
    @PostMapping(value = "/user")
    public String postUser() {
        return "hello world";
    }
    @GetMapping(value = "/user")
    public String getUser() {
        return "hello world";
    }
    @GetMapping(value = "/commit")
    public String getCommit() {
        return "hello world";
    }

}
