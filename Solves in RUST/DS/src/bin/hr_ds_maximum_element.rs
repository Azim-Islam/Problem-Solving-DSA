use std::vec::Vec;
fn main() {
    let mut inp_s = String::new();
    std::io::stdin().read_line(&mut inp_s).unwrap();
    let n: u64 = inp_s.trim().parse().unwrap();
    let mut stack: Vec<u64> = Vec::new();
    let mut max_val: u64 = 0;
    let mut max_values: Vec<u64> = Vec::new();

    for _ in 0..n {
        inp_s.clear();
        std::io::stdin().read_line(&mut inp_s).unwrap();
        let inputs = inp_s.split_whitespace().collect::<Vec<_>>();
        if inputs[0] == "1" {
            let val: u64 = inputs[1].trim().parse().unwrap();
            max_val = if val > max_val { val } else { max_val };
            stack.push(max_val);
        } else if inputs[0] == "2" {
            let popped = stack.pop().unwrap();
            if popped == max_val {
                match stack.last() {
                    None => {
                        max_val = 0;
                    }
                    _ => {
                        max_val = stack.last().unwrap().clone();
                    }
                }
            }
        } else {
            max_values.push(stack.last().unwrap().clone());
        }
    }

    for i in max_values {
        println!("{}", i);
    }
    
}
