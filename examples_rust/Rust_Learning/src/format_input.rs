/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2023. All rights reserved.
 * Description: 上机编程认证
 */

// 答题框内的代码仅为待实现代码，执行或提交代码时，仅包含待实现部分，不要包含其它代码。
// CodeCheck/Cmetrics工具也仅扫描待实现部分。
// 若需要完整框架用于本地调试，请点击答题框上面的“下载完整框架代码”进行下载。
/*
TimerSystem([8, 4, 11])
runTimerSystem(2)
timerStart(1)
timerStart(4)
runTimerSystem(8)
timerStart(0)
timerStart(2)
timerStart(1)
runTimerSystem(20)
timerStop(1)
runTimerSystem(30)

输出
null
[]
true
false
[[6, 1]]
true
true
true
[[12, 1], [16, 0], [16, 1], [19, 2], [20, 1]]
true
[[24, 0], [30, 2]]
 */
use std::collections::{BTreeMap, BTreeSet};

struct TimerSystem {
    timers_: BTreeMap<i32, i32>,
    start_times: BTreeMap<i32, i32>,
    stop_times: BTreeMap<i32, i32>,
    cur_time_: i32
}

impl TimerSystem {
    fn new(timers: Vec::<i32>) -> Self {
        let mut all_times = BTreeMap::new();
        for (i, v) in timers.iter().enumerate() {
            all_times.insert(i as i32, v.clone());
        }
        Self{timers_: all_times, start_times: BTreeMap::new(), stop_times: BTreeMap::new(),
            cur_time_: 0i32}
    }

    fn timer_start(&mut self, timer_id: i32) -> bool {
        if self.timers_.get(&timer_id) == Option::None {
            return false;
        }
        self.stop_times.remove(&timer_id);
        self.start_times.insert(timer_id, self.cur_time_);
        true
    }

    fn timer_stop(&mut self, timer_id: i32) -> bool {
        if self.timers_.get(&timer_id) == Option::None {
            return false;
        }
        self.start_times.remove(&timer_id);
        self.stop_times.insert(timer_id, self.cur_time_);
        true
    }

    fn run_timer_system(&mut self, now_time: i32) -> Vec::<(i32, i32)> {

        let mut res : Vec<(i32, i32)> = Vec::new();
        if self.start_times.is_empty() == true {
            self.cur_time_ = now_time;
            return vec![];
        }

        let mut start_ = now_time;
        for itm in self.start_times.iter() {
            let time = self.timers_.get(itm.0).unwrap();
            if self.cur_time_ == 0 {
                start_ = itm.1 + time;
            } else {
                if self.cur_time_ == time.clone() {
                    start_ = self.cur_time_ + time;
                } else {
                    start_ = itm.1 + time;
                }
            }
            println!("start {}", start_);
            loop {
                if start_ > now_time {
                    break;
                }
                res.push((start_, itm.0.clone()));
                start_ = start_ + time.clone();
            }
        }
        self.cur_time_ = now_time;
        res.sort_by(|a, b|{
            a.0.cmp(&b.0)
                .then(a.1.cmp(&b.1))
        });
        for itm in res.iter() {
            self.start_times.insert(itm.1, itm.0);
        }
        res
    }
}

// 以下为考题输入输出框架，此部分代码不建议改动；提交代码时请勿包含下面代码
mod io_formatter {

    use std::io::{stdin, stdout, BufRead, Result, Error, ErrorKind};
    use serde::Serialize;
    use serde_json::{from_str, Serializer};

    struct OutFormatter {}

    impl serde_json::ser::Formatter for OutFormatter {
        fn begin_array_value<W: ?Sized + std::io::Write>(&mut self, writer: &mut W, first: bool) -> Result<()> {
            if !first { writer.write(b", ")?; }
            Ok(())
        }
    }

    fn split_name_and_paras(line: &str) -> Result<(&str, String)> {
        let (name, paras) = line.split_once('(').ok_or(Error::from(ErrorKind::InvalidData))?;
        let paras = paras.trim_end().strip_suffix(')').ok_or(Error::from(ErrorKind::InvalidData))?;
        Ok((name.trim(), "[".to_string() + paras + "]"))
    }

    pub fn normal_process() -> Result<()> {
        let mut line = String::new();
        let mut handle = stdin().lock();
        let mut read_count = handle.read_line(&mut line)?;
        let (name, paras) = split_name_and_paras(&line)?;
        if name != "TimerSystem" { return Err(Error::from(ErrorKind::InvalidData)); }
        let (timers,): (Vec::<i32>,) = from_str(&paras)?;
        let mut timer_system = super::TimerSystem::new(timers);
        println!("null");
        let mut ser = Serializer::with_formatter(stdout(), OutFormatter{});
        while read_count != 0 {
            line.clear();
            read_count = handle.read_line(&mut line)?;
            if line.trim().len() == 0 { continue; }
            let (name, paras) = split_name_and_paras(&line)?;
            match name {
                "timerStart" => {
                    let (timer_id,): (i32,) = from_str(&paras)?;
                    timer_system.timer_start(timer_id).serialize(&mut ser).unwrap();
                }
                "timerStop" => {
                    let (timer_id,): (i32,) = from_str(&paras)?;
                    timer_system.timer_stop(timer_id).serialize(&mut ser).unwrap();
                }
                "runTimerSystem" => {
                    let (now_time,): (i32,) = from_str(&paras)?;
                    timer_system.run_timer_system(now_time).serialize(&mut ser).unwrap();
                }
                _ => {
                    return Err(Error::from(ErrorKind::InvalidData));
                }
            }
            println!("");
        }
        Ok(())
    }

}

fn main() {
    if let Err(_) = io_formatter::normal_process() {
        print!("Input format incorrect!");
    }
}