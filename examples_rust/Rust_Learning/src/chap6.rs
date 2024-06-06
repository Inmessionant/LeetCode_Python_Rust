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
    match x {
        // 必须穷举所有可能
        None => None,
        Some(i) => Some(i + 1),
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

    if let Some(3) = v {
        // 只对v是Some(3)情况做处理，但放弃了所有穷举的可能性，可以搭配else()使用
        println!("three");
    } else {
        println!("others");
    }
}