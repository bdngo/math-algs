(define (f x) (expt x 2))
(define (g x) (- (* 3 x) 2))
(define (func x) (- (f x) (g x)))
(define interval '(1.5 10))

(define (cadr x) (car (cdr x)))

(define (sgn x)
  (cond
    ((< x 0) 1)
    ((zero? x) 0)
    (else 1)
  )
)

(define (find-zeroes function interval)
  (define (fz-helper interval zero)
    (if (zero? (function zero))
      zero
      (let
        ((left-bound (function (car interval)))
        (right-bound (function (cadr interval)))
        (mid-bound (function (/ (+ (car interval) (cadr interval)) 2))))
        (cond
          ((not (eq? (sgn left-bound) (sgn mid-bound))) (fz-helper (list left-bound mid-bound) (/ (+ (car interval) (cdr interval)) 2)))
          ((not (eq? (sgn right-bound) (sgn mid-bound))) (fz-helper (list mid-bound right-bound) (/ (+ (car interval) (cdr interval)) 2)))
        )
      )
    )
  )
  (fz-helper interval 0)
)

