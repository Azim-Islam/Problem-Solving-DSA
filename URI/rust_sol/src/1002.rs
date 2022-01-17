use std::io;

fn input_float() -> f64{
    let mut input_txt = String::new();
    io::stdin().read_line(&mut input_txt).expect("ERROR");
    let x : f64 = input_txt.trim().parse().expect("WOW");
    input_txt.clear();
    return x;
}

fn main(){
    let y : f64 = input_float();
    println!("A={:.4}", 3.14159*(f64::powf(y, 2.0)));
}