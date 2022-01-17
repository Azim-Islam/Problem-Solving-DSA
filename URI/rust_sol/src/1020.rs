use std::io;

fn input_integer() -> i64{
    let mut input_txt = String::new();
    io::stdin().read_line(&mut input_txt).expect("ERROR");
    let x : i64 = input_txt.trim().parse().expect("WOW");
    input_txt.clear();
    return x;
}

fn main(){
    let x = input_integer();
    let years = x/365;
    let months = (x - years*365 ) / 30;
    let days = x - years*365 -  months*30;
    println!("{} ano(s)\n{} mes(es)\n{} dia(s)", years, months, days);
}