use std::iter::Sum;



pub fn chap10_1() {
    // fn largest<T: std::cmp::PartialOrd>(list: &[T]) -> T {
    //     let mut largest_number = list[0];
    //     for &val in list {
    //         if val > largest_number {
    //             largest_number = val;
    //         }
    //     }
    //     largest_number

    // }

    // let numbers = vec![10, 20, 15, 70];
    // let result = largest(&numbers);
    // println!("the largest number is {}", result);

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

    impl Summary for NewsArticle {
        fn summary(&self) -> String {
            return format!("{}, by {} ({})", self.headline, self.author, self.location)
        }
    }

    let news = NewsArticle {
        headline: "ebooks".to_string(),
        location: "xian".to_string(),
        author: "JL".to_string(),
        content: "hello, world".to_string(), 
    };

    print!("summary: {}", news.summary());
}