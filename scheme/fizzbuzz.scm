(define (fizzbuzz n)
  (if (= n 1)
    1
    (begin
      (cond
        ((and (zero? (remainder n 3)) (zero? (remainder n 5))) (display "fizzbuzz"))
        ((zero? (remainder n 3)) (display "fizz"))
        ((zero? (remainder n 5)) (display "buzz"))
        (else (display n))
      )
      (display "\n")
      (fizzbuzz (- n 1))
    )
  )
)
