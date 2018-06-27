# AddLineNumbers
Scripts to add line numbers to text files.

## Requirements
- Python 2.x or Python 3.x

## Restriction
- It doesn't process files recursive in directory
- Line number range is from 1 to 999

## Usage
### Adding line number for single file
```
$ cd linenumber
$ python line_for_file.py
Usage: python line_for_file.py [input] [output]
$
$ python line_for_file.py ../example/in/sample01.swift ../example/out/sample01.swift
```

- example/in/sample01.swift(original)
```
import Foundation

let score1: Int = 23

let score2 = 35

var sum = 0
sum = score1 + score2

if sum > 100 {
    print("Pass: \(sum)")
} else {
    print("Fail: \(sum)")
}
```

- example/out/sample01.swift(processed)
```
  1. import Foundation
  2. 
  3. let score1: Int = 23
  4. 
  5. let score2 = 35
  6. 
  7. var sum = 0
  8. sum = score1 + score2
  9. 
 10. if sum > 100 {
 11.     print("Pass: \(sum)")
 12. } else {
 13.     print("Fail: \(sum)")
 14. }
```

### Adding line number for files in directory
```
$ cd linenumber
python line_for_dir.py 
Usage: python line_for_dir.py [input_directory] [output_directory]
$
$ python line_for_fir.py ../example/in ../example/out
['sample01.swift', 'sample02.swift']
```
