#Summary of Chapter 7: Regular Expression:


* Regex:

* You use `()` to breakdown groups. You can group regex using parenthesis.

`\d` will get you digits.

* The `\(` and `\)` escape characters in the raw string passed to re.compile() 
will match actual parenthesis characters.

* You can use the pipe `|` character when you want to match one or many elements in a regular expression.
The pipe character will return only the first instance of a match. You can also escape pipe characters

* The question mark (?) is used for optional matching.  Using ? in brackets you can add an optional group tp your regex.

* The Asterix character `*` will match zero or more.

* The plus (+) sign is used to match one or more.

* Curly braces can be used to match repitions. For eg. (Ha){3} will match 'HaHaHa' and will not match 'HaHa'. You can use `,` to specify a range.
Python Regex has a greedy and non greedy matching when using a range. In instances where the matching is ambigious python will return the longest macthed string. You can choose the shortest match in a range by using a question mark at the end of the match:  `(Ha){3}?`

* NB: Question marks have to meaning in python. i) To specify an optional group. ii) To declaring a non-greedy matching.


* `findall()` Method: The findall method will return a list of all found searches. When the findall is used on a group, it will return a list of tuples.


* Character Class in Regex: 
i) `\d` : Any numeric digits 0-9
ii) `\D` : Any character that is not a numeric. This will include all alphabets and special characters.
iii) `\w`: Match any word, letters, numbers, including underscore
iv) `\W` : Any character that is not number, letter or underscore
v)`\s` : Any space, tab or newline character.
vi) `\S` : Any character that is not space, tab or newline


* Making your own Character classes: You can make your own character classes by using square brackets. 
The caret `^` sign is used to negate (invert) the match you want if put in a square bracket

* 