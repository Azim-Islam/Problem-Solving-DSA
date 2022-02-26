use std::process::exit;


fn main(){
    let mut string = String::new();
    let mut input_s = String::new();



    std::io::stdin().read_line(&mut input_s).unwrap();
    std::io::stdin().read_line(&mut string).unwrap();
    let string = string.trim().to_string().chars().collect::<Vec<char>>();
    


    let values: Vec<i64> = input_s.trim().split_whitespace().map(|x| x.parse::<i64>().unwrap()).collect::<Vec<i64>>();
    let mut first_half: Vec<char> = Vec::new();
    let mut last_half: Vec<char> = Vec::new();
    let mut middle: Vec<char> = Vec::new();
    let mut mismatches: i64 = 0;
    
    let (n, mut k) = (values[0], values[1]);

    for i in 0..(n / (2 as i64)){
        first_half.push(string[i as usize].clone());
        last_half.push(string[(n-i-1) as usize].clone());
        if string[(n-i-1) as usize] != string[i as usize]{
            mismatches += 1;
        }
    }


    for i  in 0..(n as usize/ (2 as usize)){
        if (k-2 >= 0) && (first_half[i].max(last_half[i]) != '9') && (mismatches <= k - 1){
            if first_half[i] != last_half[i]{
                mismatches -= 1;
            }
            first_half[i] = '9';
            last_half[i] = '9';
            k -= 2;
        }
        else if k-1 >= 0{
            if first_half[i] != last_half[i]{
                first_half[i] = first_half[i].max(last_half[i]).clone();
                last_half[i] = first_half[i].max(last_half[i]).clone();
                k -= 1;
                mismatches -= 1;
            }
        }
        else if k < 1 && mismatches > 0 {
            println!("-1");
            exit(0);
        }
    }

    if n%2 == 1{
        middle.push(string[(n as usize)/(2 as usize)].clone());
        if k > 0{
            middle[0] = '9';
            k = k - 1;
        }
    }

    let answer = [first_half.into_iter().collect::<String>(), 
                        middle.into_iter().collect::<String>(), 
                        last_half.into_iter().collect::<String>()].join("");

    println!("{}", answer);
}