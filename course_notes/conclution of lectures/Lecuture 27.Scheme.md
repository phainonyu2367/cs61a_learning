## Scheme
![[Pasted image 20260126111522.png]]
#### Fundamentals
expressions:
- Primitive expressions: 2, 3.3, true,  +, quotient,......
- Combinations: (quotient 10 2), (not true), ....
![[Pasted image 20260126111819.png]]

![[Pasted image 20260126112317.png]]
#### Special Forms
![[Pasted image 20260126112931.png]]
implement a square root function with scheme
```
(define (average x y)
	(/ (+ x y) 2)
)

(define (square x)
	(* x x)
)

(define (sqrt x)
	(
		(define (update guess)
			(if (= (square guess) x)
				guess
				(average guess (/ x guess))
			)
		)
	)
	(update 1)
)
```

## Scheme Interpreters
in project 4 you implements a scheme interpreter
you will do that by actually writing the code that executes the different procedues in scheme.

## Lambda Expressions
```
(lambda (<formal-parameters>) <body>)

# case
(define (plus4 x) (+ x 4))
(define plus4 (lambda (x) (+ x 4)))
```
## Example: Sierpinski's Triangle
there are built-in drawing functions in scheme
```
(fd 100) # forward
(rt 90) # right-turn 90
(fd 40)
(bk 100)
(lt 90)
(define (line) (fd 50))
(line)
(line)
(rt 90)
(define (twice fn) (fn) (fn))
(twice line)
```

`(load 'ex.scm)`

```
# ex.scm

(define (line) (fd 50))
(define (twice fn) (fn) (fn))
(define (repeat k fn)
	(fn)
	(if (> k 1) (repeat (- k 1) fn))
)
(define (tri fn)
	(repeat 3 (lambda () (fn) (lt 120))))
	
(define (sier d k)
	(tri (lambda () (if (= d 1) (fd k) (leg d k)))))

(define (leg d k)
	(sier (- d 1) (/ k 2))
	(penup) (fd k) (pendown)
)
```
![[Pasted image 20260126115650.png]]
