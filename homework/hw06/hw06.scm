(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
    (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
    (cadr (cdr s))
)


(define (sign num)
  'YOUR-CODE-HERE
  (cond
      ((= num 0) 0)
      ((< num 0) -1)
      (else 1))
)


(define (square x) (* x x))

; (define (pow x y)
;   (define (helper exp ans)
;       (cond 
;             ((= exp y) ans) 
;             ((= y 0)) 1)
;             ((< (* 2 exp) y) (helper (* 2 exp) (square ans))
;             (else (helper (+ exp 1) (* x ans)))))
; (helper 1 x)
; )

(define (pow x y)
  (define (helper exp ans)
    (cond
      ((= y 0) 1)
      ((= exp y) ans)
      ((< (* 2 exp) y) (helper (* 2 exp) (square ans)))
      (else (helper (+ exp 1) (* x ans)))))
  (if (= x 1) 1 (helper 1 x))
 )


