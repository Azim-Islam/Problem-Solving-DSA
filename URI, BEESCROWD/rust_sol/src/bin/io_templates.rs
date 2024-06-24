fn input_integer() -> i64{
    let mut input_txt = String::new();
    io::stdin().read_line(&mut input_txt).expect("ERROR");
    let x : i64 = input_txt.trim().parse().expect("WOW");
    input_txt.clear();
    return x;
}

fn input_float() -> f64{
    let mut input_txt = String::new();
    io::stdin().read_line(&mut input_txt).expect("ERROR");
    let x : f64 = input_txt.trim().parse().expect("WOW");
    input_txt.clear();
    return x;
}

