(define (collatz n)
  (cond
    ((= n 1) (cons 1 nil))
    ((even? n) (cons n (collatz (/ n 2))))
    (else (cons n (collatz (+ (* 3 n) 1))))
  )
)
