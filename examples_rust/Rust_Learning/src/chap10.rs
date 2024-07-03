use std::{fmt::{Debug, Display}, iter::Sum};



pub fn chap10_1() {
    fn largest<T: PartialOrd + Copy>(list: &[T]) -> T {
        let mut largest_number = list[0];
        for &val in list.iter() {
            if val > largest_number {
                largest_number = val;
            }
        }
        largest_number

    }

    let numbers = vec![10, 20, 15, 70];
    let result = largest(&numbers);
    println!("the largest number is {}", result);

    struct Point<T> {
        x: T,
        y: T,
    }

    impl<T> Point<T> {
        fn x(&self) -> &T {
            &self.x
        }
        
    }

    let integer = Point{x: 5, y: 10};
    let float = Point{x: 5.0, y: 10.0};


    enum Option<T> {
        Some(T),
        None,
    }

    enum Result<T, E> {
        Ok(T),
        Err(E),
    }


}


pub fn chap10_3() {
    // trait
    pub trait Summary {
        fn summary(&self) -> String;
        // fn summary1(&self) -> String;
    }

    struct NewsArticle {
        pub headline: String,
        pub location: String,
        pub author: String,
        pub content: String,
    }

    struct Tweet {
        pub headline: String,
        pub location: String,
        pub author: String,
        pub content: String,
    }

    impl Summary for NewsArticle {
        fn summary(&self) -> String {
            return format!("NewsArticle {}, by {} ({})", self.headline, self.author, self.location)
        }
    }

    impl Summary for Tweet {
        fn summary(&self) -> String {
            return format!("Tweet {}, by {} ({})", self.headline, self.author, self.location)
        }
    }

    pub fn notify(item: impl Summary) {
        println!("breaking news! {}", item.summary());
    }

    pub fn notify1(item: impl Summary + Display) {
        println!("breaking news! {}", item.summary());
    }

    pub fn notify2<T: Summary>(item: T) { // 多参数时候比较直观
        println!("breaking news! {}", item.summary());
    }

    pub fn notify3<T: Summary + Display>(item: T) { // 多参数时候比较直观
        println!("breaking news! {}", item.summary());
    }
    
    
    let news_article = NewsArticle {
        headline: "ebooks".to_string(),
        location: "xian".to_string(),
        author: "JL".to_string(),
        content: "hello, world".to_string(), 
    };

    let tweet: Tweet = Tweet {
        headline: "ebooks".to_string(),
        location: "xian".to_string(),
        author: "JL".to_string(),
        content: "hello, world".to_string(), 
    };

    notify(news_article);
    notify(tweet);


    pub fn notify_bith<T: Summary + Display, U: Clone + Debug>(a: T, b: U) -> String {
        "hello".to_string()
    }

    pub fn notify_bith1<T, U>(a: T, b: U) -> String 
    where
        T: Summary + Display,
        U: Clone + Debug
    {
        "hello".to_string()
    }

    
}

pub fn chap10_5() {
    let string1 = String::from("abcd");
    let string2 = "xyz";

    let result  = longest(string1.as_str(), string2);

    println!("the longest string is {}", result);

    fn longest<'a>(x: &'a str, y: &'a str) -> &'a str{
        if x.len() > y.len() {
            x
        } else {
            y
        }
    }
}