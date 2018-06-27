import Foundation

let numbers = [11, 2, 5, -8, 0, 6]

let overTen = numbers.filter { (number: Int) -> Bool in
    return number > 10
}

print("Over ten numbers: \(overTen)")

let overFive = numbers.filter { number in
    return number > 5
}

print("Over five numbers: \(overFive)")

let overTwo = numbers.filter { number in number > 2 }

print("Over two numbers: \(overTwo)")

let overZero = numbers.filter { $0 > 0 }

print("Over zero numbers: \(overZero)")