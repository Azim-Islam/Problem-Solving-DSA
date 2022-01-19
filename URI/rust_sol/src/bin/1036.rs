use std::{io, panic};

fn main(){
    let mut input_s = String::new();
    io::stdin().read_line(&mut input_s).unwrap();
    let values: Vec<f64> = input_s.split_ascii_whitespace().map(|x| x.parse::<f64>().expect("Wrong Input")).collect();
    let (A, B, C) = (values[0], values[1], values[2]); 
    let R1 = (-B + (B.powi(2) - 4.0*A*C).sqrt())/(2.0*A);
    let R2 = (-B - (B.powi(2) - 4.0*A*C).sqrt())/(2.0*A);

    if R1.is_infinite() || R2.is_infinite() || R1.is_nan() || R2.is_nan() {
        println!("Impossivel calcular");
    }
    else{
        println!("R1 = {:.5}\nR2 = {:.5}", R1, R2);
    }
}