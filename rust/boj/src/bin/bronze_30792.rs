fn main() {
    let mut nums = String::new();
    std::io::stdin().read_line(&mut nums).unwrap();

    let mut selected = String::new();
    std::io::stdin().read_line(&mut selected).unwrap();

    let selected = selected.trim().parse::<i32>().unwrap();

    let mut characters = String::new();
    std::io::stdin().read_line(&mut characters).unwrap();

    let mut characters: Vec<i32> = characters
        .split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();

    characters.push(selected);
    characters.sort();

    let nums = nums.trim().parse::<i32>().unwrap();
    let position = characters.iter().position(|&x| x == selected).unwrap() as i32 + 1;

    println!("{}", nums - position + 1);
}
