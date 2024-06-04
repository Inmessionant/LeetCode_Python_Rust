// https://www.bilibili.com/video/BV1hp4y1k7SV

use rand::Rng;
use std::{cmp::Ordering, io};

fn largest<T: PartialOrd + Copy>(list: &[T]) -> T {
    let mut largest = list[0];

    for &item in list.iter() {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn fnc1() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest(&number_list);
    println!("The largest number is {}", result);

    let char_list = vec!['y', 'm', 'a', 'q'];

    let result = largest(&char_list);
    println!("The largest char is {}", result);

    let secrect_number = rand::thread_rng().gen_range(1, 100); // [1, 100)
    print!("rand_number is: {}\n", secrect_number);

    loop {
        println!("please input a number:[0, 100)");
        let mut guess = String::new();
        io::stdin()
            .read_line(&mut guess)
            .expect("can't read a number!");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("invaild number, please input a number again!");
                continue;
            }
        };
        print!("you guess numvber is: {}\n", guess);

        match guess.cmp(&secrect_number) {
            Ordering::Less => println!(
                "guess_number {} is smaller than secrect number {}",
                guess, secrect_number
            ),
            Ordering::Equal => println!(
                "guess_number {} is equal to secrect number {}",
                guess, secrect_number
            ),
            Ordering::Greater => println!(
                "guess_number {} is larger than secrect number {}",
                guess, secrect_number
            ),
        }
    }
}

fn fnc2() {
    const MAX_ITEAMS: i32 = 10000;
    println!("const MAX_ITEAMS = {}", MAX_ITEAMS);

    let mut x = 2;
    println!("x = {}", x);
    x = 10;
    println!("x = {}", x);
}

fn func3_2() {
    let guess: isize = "32".parse().expect("not a number");
    println!("guess = {}", guess)
}

fn func3_3() {
    let tup = (1, 2, 3);
    let (x, y, z) = tup;
    println!("{} {} {}", x, y, z);
    println!("{} {} {}", tup.0, tup.1, tup.2);

    let a: [i32; 3] = [1, 2, 3];
    let a = [32; 10];

    for (idx, &item) in a.iter().enumerate() {
        print!("{} => {}\n", idx, item)
    }
}

fn func3_4() -> i32 {
    let x = 5;
    println!("before x = {}", x);
    let y = {
        let x = 1;
        println!("inside x = {}", x);
        x + 3
    };
    println!("outside x = {}", x);
    println!("outside y = {}", y);
    5
}

fn func3_5() {
    let number = 11;

    if number < 0 {
        println!("number < 0 number = {}", number);
    } else if number < 10 {
        println!("number < 10 number = {}", number);
    } else {
        println!("default number = {}", number);
    }

    let cur = if number < 100 { 5 } else { 6 };
    println!(" cur = {}", cur);
}

fn func3_6() {
    let mut cnt: i32 = 1000;
    loop {
        println!("cnt = {}", cnt);
        cnt -= 1;
        if cnt == 0 {
            break;
        }
    }

    cnt = 1000;

    while (cnt > 0) {
        println!("cnt = {}", cnt);
        cnt -= 1;
    }

    let a = [10, 20, 30, 40, 50];

    for val in a.iter() {
        println!("val = {}", val);
    }

    for number in (1..5).rev() {
        println!("number = {}", number);
    }
}

fn first_world(s: &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[..i];
        }
    }
    &s[..]
}

fn func4_3() {
    let s = String::from("Hello world");
    let idx = first_world(&s[..]);
    println!("{}", idx);
}

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

enum IPAddrKind {
    IPv4,
    IPv6,
}

struct IPAddr {
    ip_kind: IPAddrKind,
    address: String,
}

enum IPAddress {
    V4(u8, u8, u8, u8),
    V6(String),
}

fn router(ip_kind: IPAddr) {}

enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

impl Message {
    fn call(&self) {}
}

fn func6_1() {
    let home = IPAddr {
        ip_kind: IPAddrKind::IPv4,
        address: String::from("191.169.1.1"),
    };

    let home = IPAddress::V4(192, 168, 1, 1);

    let loopback = IPAddr {
        ip_kind: IPAddrKind::IPv6,
        address: String::from("::1"),
    };

    let loopback = IPAddress::V6(String::from("::1"));

    let quit = Message::Quit;
    let move_to: Message = Message::Move { x: 12, y: 24 };
    let write = Message::Write(String::from("hello"));
    let changecolor = Message::ChangeColor(255, 255, 255);

    move_to.call();
}

fn func6_2() {
    // Option<T> != T
    let x: i8 = 5;
    let y: Option<i8> = Some(5);

    // let z = x + y;
}

#[derive(Debug)]
enum UsState {
    Alabama,
    Alaska,
}

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState),
}

// println!("{}", func6_3(Coin::Quarter(UsState::Alaska)));
fn func6_3(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => {
            println!("Penny");
            1
        }
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter(state) => {
            println!("State quarter from {:?}", state);
            25
        }
    }
}

fn plus_one(x: Option<i32>) -> Option<i32> {
    match x { // 必须穷举所有可能
        None => None,
        Some(i) => Some(i+1),
    }
}

fn func6_3_2() {
    let five = Some(5);
    let six = plus_one(five);
    let none = plus_one(None);

    let v = 0u8;

    match v {
        1 => println!("1"),
        3 => println!("3"),
        5 => println!("5"),
        _ => println!("default"),
    }
}

fn func6_4() {
    let v = Some(3);

    if let Some(3) = v { // 只对v是Some(3)情况做处理，但放弃了所有穷举的可能性，可以搭配else()使用
        println!("three");
    } else {
        println!("others");
    }
}

fn func7_1() {

}

fn main() {
    func6_4();
}
