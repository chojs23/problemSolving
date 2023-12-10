fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let inputs = input
        .split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect::<Vec<i32>>();

    let mut result = 0;

    for (idx, input) in inputs.iter().enumerate() {
        if idx == 0 {
            continue;
        }
        if inputs[0] <= input + 1000 {
            result += 1;
        }
    }

    print!("{}", result);
}
