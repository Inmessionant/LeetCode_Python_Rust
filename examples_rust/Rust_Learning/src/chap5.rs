struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}

struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

fn buil_user(username: String, email: String) -> User {
    User {
        username: username,
        email: email,
        sign_in_count: 0,
        active: true,
    }
}

fn func5_1() {
    let mut user = User {
        email: String::from("123456@outlook.com"),
        username: String::from("zarek"),
        sign_in_count: 556,
        active: true,
    };

    user.email = String::from("allen@163.com");

    let mut user2 = buil_user(String::from("username"), String::from("email"));
    let mut user3 = User {
        email: String::from("value"),
        username: String::from("value"),
        ..user
    };

    let black = Color(0, 0, 0);
}

#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn cover(&self, other: &Rectangle) -> bool {
        self.width >= other.width && self.height >= other.height
    }

    fn square(size: u32) -> Rectangle {
        Rectangle {
            width: size,
            height: size,
        }
    }
}

fn func5_2() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    let rect2 = Rectangle {
        width: 10,
        height: 40,
    };

    let rect3 = Rectangle {
        width: 35,
        height: 55,
    };
    println!("{:#?}", rect1.cover(&rect2));
    println!("{:#?}", rect1.cover(&rect3));

    let square = Rectangle::square(40);
}
